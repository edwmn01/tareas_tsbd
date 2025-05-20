import re
from datetime import datetime
import streamlit as st

    
def validar_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None


def es_numerico(texto, min_len, max_len):
    return texto.isdigit() and min_len <= len(texto) <= max_len


def validar_formulario(nombre, apellido, cedula, correo, telefono, direccion):
    campos_no_validos = []
    if not nombre:
        campos_no_validos.append('Nombre')
    if not apellido:
        campos_no_validos.append('Apellido')
    if not es_numerico(cedula, 10, 10):
        campos_no_validos.append('Cedula')
    if not validar_email(correo):
        campos_no_validos.append('Correo')
    if not es_numerico(telefono, 7, 10):
        campos_no_validos.append('Teléfono')
    if not direccion:
        campos_no_validos.append('Dirección')
    
    if len(campos_no_validos) > 0:
        st.warning(f'Los siguientes campos no pueden estar en blanco o contener errores de formato:\n{", ".join(campos_no_validos)}.')
        return False
    
    return True
