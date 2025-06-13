import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('Compras Públicas - Eduardo Mendieta')

anio = st.selectbox('Elige el año:', [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])

provincia = st.selectbox('Selecciona la provincia:', [
    'Todas',
    'AZUAY',
    'BOLIVAR',
    'CAÑAR',
    'CARCHI',
    'CHIMBORAZO',
    'COTOPAXI',
    'EL ORO',
    'ESMERALDAS',
    'GALAPAGOS',
    'GUAYAS',
    'LOS RIOS',
    'MANABI',
    'MORONA SANTIAGO',
    'NAPO',
    'ORELLANA',
    'PICHINCHA',
    'SUCUMBIOS',
    'TUNGURAHUA',
    'ZAMORA CHINCHIPE',
    'SANTA ELENA',
    'COTOPAXI',
    'SANTO DOMINGO DE LOS TSACHILAS',
    'PASTAZA',
    'LOJA'
])

tipo_contratacion = st.selectbox('Selecciona el tipo de contratación:', [
    'Todas',
    'Subasta Inversa Electrónica',
    'Catálogo electrónico - Mejor oferta',
    'Catálogo electrónico - Compra directa',
    'Obra artística, científica o literaria',
    'Menor Cuantía',
    'Cotización',
    'Contratos entre Entidades Públicas o sus subsidiarias',
    'Bienes y Servicios únicos',
    'Licitación de Seguros',
    'Contratacion directa',
    'Transporte de correo interno o internacional',
    'Repuestos o Accesorios',
    'Comunicación Social – Contratación Directa'
])

url_base = 'https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/api/get_analysis'

params = {"year": anio}
if provincia != 'Todas': params['region'] = provincia
if tipo_contratacion != 'Todas': params['type'] = tipo_contratacion

response = requests.get(url_base, params=params)
response.raise_for_status()
data = response.json()

df = pd.DataFrame(data)

st.subheader(f'Compras publicas del año: {anio}, provincia: {provincia.capitalize()}, tipo contratación: {tipo_contratacion}')
st.dataframe(df)

btn_descarga = st.download_button(f"Descargar reporte del año {anio}", df.to_csv(index=False), file_name=f"reporte_{anio}.csv")

if btn_descarga:
    st.success("Datos descargados correctamente.")


# ====================================== GRÁFICAS ======================================
print(df.columns.tolist())


meses = {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre'
}

df['mes_str'] = df['month'].map(meses).astype(str)
df.total = df.total.astype(float)

print(df.columns.tolist())
print(df.info())

# =============================== GRÁFICA 1 ===============================
st.subheader(f'1. Total por mes y tipo - Año {anio}, provincia: {provincia}, tipo de contratación: {tipo_contratacion}')
grouped = df.groupby(['mes_str', 'internal_type'])['total'].sum().reset_index()

pivoted = grouped.pivot(index='mes_str', columns='internal_type', values='total').fillna(0)


fig, ax = plt.subplots(figsize=(13, 7))

bottom = None
colors = plt.cm.tab20.colors 

for i, col in enumerate(pivoted.columns):
    ax.bar(pivoted.index, pivoted[col], bottom=bottom, label=col, color=colors[i % len(colors)])
    if bottom is None:
        bottom = pivoted[col]
    else:
        bottom += pivoted[col]

ax.set_title('Total por mes y tipo')
ax.set_xlabel('Meses')
ax.set_ylabel('Total')
plt.xticks(rotation=90)

ax.legend(
    title='Tipo',
    bbox_to_anchor=(1.05, 1),  
    loc='upper left',
    borderaxespad=0
)

plt.tight_layout()

st.pyplot(fig)

# =============================== GRÁFICA 2 ===============================
st.subheader(f'2. Evolución Mensual- Año {anio}, provincia: {provincia}, tipo de contratación: {tipo_contratacion}')

total_mes = df.groupby('mes_str')['total'].sum().reset_index()

total_mes['mes_str'] = pd.Categorical(total_mes['mes_str'], categories=list(meses.values()), ordered=True)
total_mes = total_mes.sort_values('mes_str')

sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
line_plot = sns.lineplot(data=total_mes, x='mes_str', y='total', marker='o')

line_plot.set_title('Evolución Mensual de los Montos Totales')
line_plot.set_xlabel('Mes')
line_plot.set_ylabel('Monto Total')

st.pyplot(plt)

# =============================== GRÁFICA 3 ===============================
st.subheader(f'3. Monto total por tipo de contratación - Año {anio}, provincia: {provincia}, tipo de contratación: {tipo_contratacion}')

totales_por_tipo = df.groupby('internal_type')['total'].sum().reset_index()

fig, ax = plt.subplots(figsize=(8, 8))

N = 10
top = totales_por_tipo.nlargest(N, 'total')
otros = pd.DataFrame([{
     'internal_type': 'Otros',
     'total': totales_por_tipo[~totales_por_tipo['internal_type'].isin(top['internal_type'])]['total'].sum()
 }])
totales_por_tipo = pd.concat([top, otros], ignore_index=True)


ax.pie(
    totales_por_tipo['total'],
    labels=totales_por_tipo['internal_type'],
    autopct='%1.1f%%',
    startangle=90,
    counterclock=False
)

ax.set_title('Distribución total por tipo de contratación')
ax.axis('equal')

st.pyplot(fig)

# =============================== GRÁFICA 4 ===============================
st.subheader(f'4. Monto Total vs Número de Contratos por Tipo de Contratación - Año {anio}, provincia: {provincia}, tipo de contratación: {tipo_contratacion}')
resumen = df.groupby('internal_type').agg(
    monto_total=('total', 'sum'),
    numero_contratos=('total', 'count')
).reset_index()


fig, ax = plt.subplots(figsize=(10, 6))

colors = plt.cm.tab20.colors
color_map = {tipo: colors[i % len(colors)] for i, tipo in enumerate(resumen['internal_type'])}

for tipo in resumen['internal_type']:
    datos = resumen[resumen['internal_type'] == tipo]
    ax.scatter(
        datos['monto_total'],
        datos['numero_contratos'],
        s=100,
        color=color_map[tipo],
        label=tipo,
        alpha=0.8
    )

ax.set_xlabel('Monto Total')
ax.set_ylabel('Número de Contratos')
ax.set_title('Monto Total vs Número de Contratos por Tipo de Contratación')

ax.legend(
    title='Tipo de Contratación',
    bbox_to_anchor=(1.05, 1),
    loc='upper left',
    borderaxespad=0
)

plt.tight_layout()

st.pyplot(fig)

# =============================== GRÁFICA 5 ===============================
st.subheader(f'5. Total de Contratos por Tipo y Mes - Año {anio}, provincia: {provincia}, tipo de contratación: {tipo_contratacion}')

plt.figure(figsize=(12, 6))
grafica_lineal = sns.lineplot(data=df, x='mes_str', y='total', hue='internal_type', marker='o')

grafica_lineal.set_title('Total de Contratos por Tipo y Mes')
grafica_lineal.set_xlabel('Mes')
grafica_lineal.set_ylabel('Total')
plt.xticks(rotation=45)
plt.legend(title='Tipo Contratación', bbox_to_anchor=(1.05, 1), loc='upper left')

st.pyplot(plt)