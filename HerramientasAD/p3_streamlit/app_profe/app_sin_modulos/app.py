# 1. Librerias -------------------------------------------------------
import streamlit as st
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import calendar
import json
from datetime import datetime
import warnings
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from prophet import Prophet


# 2. Configuración de la página ---------------------------------------
st.set_page_config(
    page_title="Análisis de Compras Públicas Ecuador",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title("📊 Análisis de Compras Públicas Ecuador")
st.markdown("---")


st.sidebar.header("🔍 Filtros de Consulta")


provincias = [
    "AZUAY", "BOLIVAR", "CAÑAR", "CARCHI", "CHIMBORAZO", "COTOPAXI", 
    "EL ORO", "ESMERALDAS", "GALAPAGOS", "GUAYAS", "IMBABURA", 
    "LOJA", "LOS RIOS", "MANABI", "MORONA SANTIAGO", "NAPO", 
    "ORELLANA", "PASTAZA", "PICHINCHA", "SANTA ELENA", 
    "SANTO DOMINGO DE LOS TSACHILAS", "SUCUMBIOS", "TUNGURAHUA", 
    "ZAMORA CHINCHIPE"
]


tipos_contratacion = [
    "Licitación", "Cotización", "Menor Cuantía", "Ínfima Cuantía",
    "Subasta Inversa", "Régimen Especial", "Contratación Directa",
    "Consultoría", "Obra", "Bien", "Servicio"
]


todos_los_anios = st.sidebar.checkbox("📅 Analizar todos los años (2015-2025)")


year = st.sidebar.selectbox("📅 Año:", options=list(range(2015, 2026)), index=5)
provincia = st.sidebar.selectbox("🏢 Provincia:", options=["Todas"] + sorted(provincias), index=0)
tipo_contratacion = st.sidebar.selectbox("📋 Tipo de Contratación:", options=["Todos"] + sorted(tipos_contratacion), index=0)


if 'df_data' not in st.session_state:
    st.session_state.df_data = None
if 'last_query' not in st.session_state:
    st.session_state.last_query = None


# 3. Métodos ----------------------------------------------------------
def construir_parametros(year, provincia, tipo):
    params = {"year": str(year)}
    if provincia != "Todas":
        params["region"] = provincia.upper()
    if tipo != "Todos":
        params["type"] = tipo
    return params


def obtener_datos(year, provincia, tipo):
    url = "https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/api/get_analysis"
    params = construir_parametros(year, provincia, tipo)
    try:
        response = requests.get(url, params=params, timeout=30)
        if response.status_code != 200:
            return None, f"Error HTTP {response.status_code}: {response.reason}"
        try:
            data = response.json()
        except json.JSONDecodeError:
            return None, "Error: La respuesta no es un JSON válido"
        if not data:
            return None, "No se encontraron datos para los filtros seleccionados"
        df = pd.DataFrame(data)
        if df.empty:
            return None, "Los datos obtenidos están vacíos"
        return df, None
    except requests.exceptions.Timeout:
        return None, "Error: Tiempo de espera agotado."
    except requests.exceptions.ConnectionError:
        return None, "Error: No se pudo conectar con la API."
    except Exception as e:
        return None, str(e)


def limpiar_datos(df):
    if df is None or df.empty:
        return None, "No hay datos para procesar"
    try:
        df_clean = df.copy()
        column_mapping = {
            'monto': 'total', 'amount': 'total', 'valor': 'total',
            'tipo': 'internal_type', 'type': 'internal_type', 'categoria': 'internal_type',
            'contratos': 'contracts', 'cantidad': 'contracts', 'count': 'contracts',
            'mes': 'month', 'fecha': 'date'
        }
        for old_name, new_name in column_mapping.items():
            if old_name in df_clean.columns and new_name not in df_clean.columns:
                df_clean[new_name] = df_clean[old_name]
        for col in ['total', 'contracts', 'month']:
            if col in df_clean.columns:
                df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
        if 'month' not in df_clean.columns:
            if 'date' in df_clean.columns:
                df_clean['date'] = pd.to_datetime(df_clean['date'], errors='coerce')
                df_clean['month'] = df_clean['date'].dt.month
            else:
                df_clean['month'] = (df_clean.index % 12) + 1
        if 'total' in df_clean.columns:
            df_clean = df_clean.dropna(subset=['total'])
            df_clean = df_clean[df_clean['total'] > 0]
        if 'internal_type' in df_clean.columns:
            df_clean = df_clean.dropna(subset=['internal_type'])
            df_clean = df_clean[df_clean['internal_type'].str.strip() != '']
        if 'contracts' not in df_clean.columns:
            df_clean['contracts'] = 1
        if df_clean.empty:
            return None, "No quedan datos válidos"
        return df_clean, None
    except Exception as e:
        return None, f"Error limpiando datos: {str(e)}"


# 4. Consultar Datos --------------------------------------------------
if st.sidebar.button("🔄 Consultar Datos", type="primary"):
    with st.spinner("Consultando datos de la API..."):
        if todos_los_anios:
            dataframes = []
            errores = []
            for y in range(2015, 2026):
                df, error = obtener_datos(y, provincia, tipo_contratacion)
                if df is not None:
                    df['anio'] = y
                    dataframes.append(df)
                else:
                    errores.append(f"{y}: {error}")
            if dataframes:
                df_all = pd.concat(dataframes, ignore_index=True)
                df_clean, clean_error = limpiar_datos(df_all)
                if clean_error:
                    st.error(f"❌ {clean_error}")
                else:
                    st.success(f"✅ {len(df_clean)} registros cargados.")
                    st.session_state.df_data = df_clean
                    st.session_state.last_query = "todos_los_anios"
            else:
                st.error("❌ No se obtuvieron datos para ningún año.")
                for e in errores:
                    st.warning(e)
        else:
            df, error = obtener_datos(year, provincia, tipo_contratacion)
            if error:
                st.error(f"❌ {error}")
            else:
                df_clean, clean_error = limpiar_datos(df)
                if clean_error:
                    st.error(f"❌ {clean_error}")
                else:
                    st.success(f"✅ {len(df_clean)} registros cargados.")
                    st.session_state.df_data = df_clean
                    st.session_state.last_query = f"{year}_{provincia}_{tipo_contratacion}"


# 5. Visualización de datos -------------------------------------------
if st.session_state.df_data is not None:
    df_clean = st.session_state.df_data


    st.markdown("## 📊 Visualización de Datos")
    tabs_vis = st.tabs(["Gráfica de Barras", "Gráfica de Líneas", "Gráfica de Pastel", "Gráfica de Dispersión", "Tipos por Mes"])


    with tabs_vis[0]:
        st.subheader("Gráfica de Barras: Total por Tipo de Contratación")
        if 'internal_type' in df_clean.columns and 'total' in df_clean.columns:
            df_bar = df_clean.groupby('internal_type')['total'].sum().reset_index()
            fig_bar = px.bar(df_bar, x='internal_type', y='total', title="Totales por Tipo de Contratación",
                             labels={'internal_type': 'Tipo de Contratación', 'total': 'Monto Total ($)'})
            st.plotly_chart(fig_bar, use_container_width=True)


    with tabs_vis[1]:
        st.subheader("Gráfica de Líneas: Evolución Mensual de Montos Totales")
        if 'month' in df_clean.columns and 'total' in df_clean.columns:
            df_line = df_clean.groupby('month')['total'].sum().reset_index()
            df_line['mes'] = df_line['month'].apply(lambda x: calendar.month_name[x])
            fig_line = px.line(df_line, x='mes', y='total', title="Evolución Mensual del Monto Total",
                               labels={'mes': 'Mes', 'total': 'Monto Total ($)'}, markers=True)
            st.plotly_chart(fig_line, use_container_width=True)


    with tabs_vis[2]:
        st.subheader("Gráfica de Pastel: Proporción de Contratos por Tipo")
        if 'internal_type' in df_clean.columns and 'contracts' in df_clean.columns:
            df_pie = df_clean.groupby('internal_type')['contracts'].sum().reset_index()
            fig_pie = px.pie(df_pie, values='contracts', names='internal_type',
                             title="Proporción de Contratos por Tipo")
            st.plotly_chart(fig_pie, use_container_width=True)


    with tabs_vis[3]:
        st.subheader("Gráfica de Dispersión: Relación Total vs Contratos")
        if 'contracts' in df_clean.columns and 'total' in df_clean.columns:
            fig_disp = px.scatter(df_clean, x='contracts', y='total', color='internal_type' if 'internal_type' in df_clean.columns else None,
                                  title="Relación entre Total y Cantidad de Contratos",
                                  labels={'contracts': 'Contratos', 'total': 'Monto Total ($)'})
            st.plotly_chart(fig_disp, use_container_width=True)


    with tabs_vis[4]:
        st.subheader("Gráfica de Línea: Tipos de Contrato por Mes")
        if all(col in df_clean.columns for col in ['month', 'internal_type', 'total']):
            df_tipo_mes = df_clean.groupby(['month', 'internal_type'])['total'].sum().reset_index()
            fig_tipo_mes = px.line(df_tipo_mes, x='month', y='total', color='internal_type',
                                   title="Tipos de Contrato por Mes",
                                   labels={'month': 'Mes', 'total': 'Monto Total ($)', 'internal_type': 'Tipo'},
                                   markers=True)
            fig_tipo_mes.update_xaxes(tickmode='linear', dtick=1)
            st.plotly_chart(fig_tipo_mes, use_container_width=True)


# 6. Aplicar modelos predictivos --------------------------------------
if st.session_state.df_data is not None:
    df_modelos = st.session_state.df_data.copy()
    if 'anio' not in df_modelos.columns and 'date' in df_modelos.columns:
        df_modelos['date'] = pd.to_datetime(df_modelos['date'], errors='coerce')
        df_modelos['anio'] = df_modelos['date'].dt.year
    st.markdown("---")
    st.header("🤖 Modelos Analíticos y Predictivos")


    tabs_modelos = st.tabs(["📈 Regresión", "🔍 Clasificación", "📊 Clustering", "⏳ Series Temporales"])


    # --- REGRESIÓN ---
    with tabs_modelos[0]:
        st.subheader("📈 Predicción del Monto Total")
        if all(col in df_modelos.columns for col in ['contracts', 'total', 'month']):
            df_reg = df_modelos[['contracts', 'month', 'total']].dropna()
            X = df_reg[['contracts', 'month']]
            y = df_reg['total']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


            model_reg = RandomForestRegressor(n_estimators=100, random_state=42)
            model_reg.fit(X_train, y_train)
            y_pred = model_reg.predict(X_test)


            st.write("**Métricas del Modelo:**")
            st.write(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")
            st.write(f"R² Score: {r2_score(y_test, y_pred):.2f}")


            fig_reg = px.scatter(x=y_test, y=y_pred, labels={'x': 'Valor Real', 'y': 'Predicción'},
                                 title="Predicción vs Valor Real")
            st.plotly_chart(fig_reg, use_container_width=True)
        else:
            st.warning("Faltan columnas necesarias para la regresión")


    # --- CLASIFICACIÓN ---
    with tabs_modelos[1]:
        st.subheader("🔍 Clasificación del Monto Total")
        df_clas = df_modelos[['contracts', 'month', 'total']].dropna().copy()
        df_clas['categoria'] = pd.cut(df_clas['total'], bins=[0, 10000, 100000, np.inf],
                                       labels=['Bajo', 'Medio', 'Alto'])
        X = df_clas[['contracts', 'month']]
        y = df_clas['categoria']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


        model_clf = RandomForestClassifier(n_estimators=100, random_state=42)
        model_clf.fit(X_train, y_train)
        y_pred = model_clf.predict(X_test)


        st.write(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
        cm = confusion_matrix(y_test, y_pred, labels=['Bajo', 'Medio', 'Alto'])
        st.write("Matriz de Confusión:")
        st.dataframe(pd.DataFrame(cm, index=['Bajo', 'Medio', 'Alto'], columns=['Bajo', 'Medio', 'Alto']))


    # --- CLUSTERING ---
    with tabs_modelos[2]:
        st.subheader("📊 Agrupamiento por Comportamiento de Contratación")
        df_clust = df_modelos[['contracts', 'month', 'total']].dropna()
        kmeans = KMeans(n_clusters=3, random_state=42)
        df_clust['cluster'] = kmeans.fit_predict(df_clust)


        fig_cluster = px.scatter(df_clust, x='contracts', y='total', color='cluster',
                                 title="Clústeres de Contrataciones")
        st.plotly_chart(fig_cluster, use_container_width=True)


    # --- SERIES TEMPORALES ---
    with tabs_modelos[3]:
        st.subheader("⏳ Predicción de Montos con Prophet")
        if 'anio' in df_modelos.columns and 'month' in df_modelos.columns:
            df_ts = df_modelos.groupby(['anio', 'month'])['total'].sum().reset_index()
            df_ts['fecha'] = pd.to_datetime(df_ts['anio'].astype(str) + '-' + df_ts['month'].astype(str) + '-01')
            df_ts = df_ts[['fecha', 'total']].rename(columns={'fecha': 'ds', 'total': 'y'})
            df_ts = df_ts[df_ts['y'] > 0]


            modelo_prophet = Prophet()
            modelo_prophet.fit(df_ts)


            futuro = modelo_prophet.make_future_dataframe(periods=6, freq='M')
            forecast = modelo_prophet.predict(futuro)


            fig_prophet = px.line(forecast, x='ds', y='yhat', title="Predicción de Montos Futuros")
            st.plotly_chart(fig_prophet, use_container_width=True)
        else:
            st.warning("Se necesitan columnas 'anio' y 'month' para construir la serie temporal")




# 7. Exportar los datos procesados a csv ------------------------------

