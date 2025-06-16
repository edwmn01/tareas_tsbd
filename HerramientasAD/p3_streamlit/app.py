import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

import graficas as gf

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


print(df.columns.tolist())




df['mes_str'] = df['month'].map(meses).astype(str)
df.total = df.total.astype(float)

print(df.columns.tolist())
print(df.info())
# ====================================== GRÁFICAS ======================================
st.subheader(f'1. Total por mes y tipo - Año {anio}, provincia: {provincia}, tipo de contratación: {tipo_contratacion}')
st.plotly_chart(gf.total_por_mes_tipo(df), use_container_width=True)

st.subheader(f'2. Evolución Mensual - Año {anio}, provincia: {provincia}, tipo de contratación: {tipo_contratacion}')
st.plotly_chart(gf.evolucion_mensual(df, meses), use_container_width=True)

st.subheader(f'3. Monto total por tipo de contratación - Año {anio}, provincia: {provincia}, tipo de contratación: {tipo_contratacion}')
st.plotly_chart(gf.monto_total_por_tipo(df), use_container_width=True)

st.subheader(f'4. Monto Total vs Número de Contratos por Tipo de Contratación - Año {anio}, provincia: {provincia}, tipo de contratación: {tipo_contratacion}')
st.plotly_chart(gf.total_vs_numcontratos(df), use_container_width=True)

st.subheader(f'5. Total de Contratos por Tipo y Mes - Año {anio}, provincia: {provincia}, tipo de contratación: {tipo_contratacion}')
st.plotly_chart(gf.total_contratos_por_tipo_mes(df), use_container_width=True)