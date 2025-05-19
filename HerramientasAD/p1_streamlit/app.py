import streamlit as st
from db import insertar_cliente
from validaciones import validar_formulario

# =================== APP WEB ===================

st.title('Formulario de clientes')

nombre = st.text_input('Ingresa un nombre:')
apellido = st.text_input('Ingresa un apellido:')
fecha_nacimiento = st.date_input('Selecciona una fecha de nacimiento:')
email = st.text_input('Ingresa un email:')
sexo = st.radio('Selecciona el sexo:', ('Masculino', 'Femenino'))
telefono = st.text_input('Ingresa un teléfono:')
direccion = st.text_input('Ingresa una dirección:')

btn_guardar = st.button('Guardar')


if btn_guardar:
    if validar_formulario(nombre, apellido, email, telefono, direccion):
        insertar_cliente(nombre, apellido, fecha_nacimiento, email, sexo, telefono, direccion)
