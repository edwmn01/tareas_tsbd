import requests
import pandas as pd
import streamlit as st

st.title('Compras Publicas al mes por año')
st.text('Estudiantes: Eduardo Mendieta, Freddy Montalvan.')

anio = st.selectbox('Elige el año:', [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])

url_base = 'https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/api/get_analysis'

print(anio)

params = {"year": anio}
response = requests.get(url_base, params=params)
response.raise_for_status()
data = response.json()

df = pd.DataFrame(data)

st.dataframe(df)

btn_descarga = st.download_button(f"Descargar reporte del año {anio}", df.to_csv(index=False), file_name=f"reporte_{anio}.csv")

if btn_descarga:
    st.success("Datos descargados correctamente.")