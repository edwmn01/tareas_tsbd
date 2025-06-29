import pandas as pd
import streamlit as st

import graficas as gf
import utils as utl
import modelos as mdl


st.title('Compras Públicas - Eduardo Mendieta')

anio_str = st.selectbox('Elige el año:', utl.anios_compras_publicas)
provincia = st.selectbox('Selecciona la provincia:', utl.provincias)
tipo_contratacion = st.selectbox('Selecciona el tipo de contratación:', utl.tipo_contratacion_compras_publicas)


url_base = 'https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/api/get_analysis'


data = utl.get_data(url_base, [int(i) for i in utl.anios_compras_publicas[1:]] if anio_str == 'Todos' else [int(anio_str)],
                    None if provincia == 'Todas' else provincia, None if tipo_contratacion == 'Todas' else tipo_contratacion)

df = pd.DataFrame(data)
df['mes_str'] = df['month'].map(utl.meses).astype(str)
df.total = df.total.astype(float)
print(df.columns.tolist())

st.subheader(f'Compras publicas del año: {anio_str}, provincia: {provincia.capitalize()}, tipo contratación: {tipo_contratacion}')
st.dataframe(df)

btn_descarga = st.download_button(f"Descargar reporte del año {anio_str}", df.to_csv(index=False), file_name=f"reporte_{anio_str}.csv")

if btn_descarga:
    st.success("Datos descargados correctamente.")


# ====================================== GRÁFICAS EN PESTAÑAS ======================================
st.subheader('Gráficas:')

tabs = st.tabs([
    "1. Total por mes y tipo",
    "2. Evolución Mensual",
    "3. Monto total por tipo",
    "4. Total vs Contratos",
    "5. Contratos por tipo y mes"
])

with tabs[0]:
    st.write(f'1. Total por mes y tipo - Año {anio_str}, provincia: {provincia}, tipo de contratación: {tipo_contratacion}')
    st.plotly_chart(gf.total_por_mes_tipo(df), use_container_width=True)

with tabs[1]:
    st.write(f'2. Evolución Mensual - Año {anio_str}, provincia: {provincia}, tipo de contratación: {tipo_contratacion}')
    st.plotly_chart(gf.evolucion_mensual(df, utl.meses), use_container_width=True)

with tabs[2]:
    st.write(f'3. Monto total por tipo de contratación - Año {anio_str}, provincia: {provincia}, tipo de contratación: {tipo_contratacion}')
    st.plotly_chart(gf.monto_total_por_tipo(df), use_container_width=True)

with tabs[3]:
    st.write(f'4. Monto Total vs Número de Contratos por Tipo de Contratación - Año {anio_str}, provincia: {provincia}, tipo de contratación: {tipo_contratacion}')
    st.plotly_chart(gf.total_vs_numcontratos(df), use_container_width=True)

with tabs[4]:
    st.write(f'5. Total de Contratos por Tipo y Mes - Año {anio_str}, provincia: {provincia}, tipo de contratación: {tipo_contratacion}')
    st.plotly_chart(gf.total_contratos_por_tipo_mes(df), use_container_width=True)


# ====================================== MODELOS ======================================
st.subheader('Modelos:')

tabs_mdl = st.tabs([
    "1. Clustering de Provincias/Contratos",
    "2. Predicción de Montos",
    "3. Clasificación de Contratos por Valor",
    "4. Clusters con PCA",
    "5. Detección de Contratos Inusuales"
])

with tabs_mdl[0]:
    st.plotly_chart(gf.grafica_kmeans(mdl.modelo_kmeans(df)), use_container_width=True)

with tabs_mdl[1]:
    model, forecast = mdl.modelo_prophet(df)
    st.plotly_chart(gf.grafica_prophet(model, forecast), use_container_width=True)

with tabs_mdl[2]:
    accuracy = mdl.modelo_regresion_logistica(df)
    res = 'El modelo no soporta un solo año para la clasificación.' if not accuracy else f'Accuracy: {accuracy:.2f}'
    st.write(res)
    st.plotly_chart(gf.grafica_clasificacion_RL(df), use_container_width=True)

with tabs_mdl[3]:
    st.plotly_chart(gf.grafica_reduccion_PCA(df, mdl.modelo_PCA(df)), use_container_width=True)

with tabs_mdl[4]:
    st.plotly_chart(gf.grafica_isolation_forest(mdl.modelo_isolation_forest(df)), use_container_width=True)
