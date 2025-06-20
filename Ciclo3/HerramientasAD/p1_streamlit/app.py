import streamlit as st
import pandas as pd
from db import insertar_persona, obtener_personas
from validaciones import validar_formulario

# =================== APP WEB ===================

st.title('Formulario de personas')

nombre = st.text_input('Ingresa un nombre:')
apellido = st.text_input('Ingresa un apellido:')
cedula = st.text_input('Ingresa una cedula:')
edad = st.slider('Ingresa una edad:', max_value=100, min_value=1)
correo = st.text_input('Ingresa un correo electrónico:')
estado_civil = st.selectbox('Elige el estado civil:', ['Soltero', 'Casado', 'Viudo', 'Divorciado', 'Union libre'])
telefono = st.text_input('Ingresa un teléfono:')
direccion = st.text_input('Ingresa una dirección:')
genero = st.radio('Selecciona el genero:', ('Masculino', 'Femenino'))

btn_guardar = st.button('Guardar')


if btn_guardar:
    if validar_formulario(nombre, apellido, cedula, correo, telefono, direccion):
        insertar_persona(nombre, apellido, cedula, edad, correo, estado_civil, telefono, direccion, genero)


st.title('Personas registradas en la base de datos')

df_personas = pd.DataFrame(obtener_personas(), columns=['ID', 'Nombre', 'Apellido', 'Cédula', 'Edad', 'Correo', 'Estado Civil', 'Teléfono', 'Dirección', 'Género'])
st.dataframe(df_personas)

