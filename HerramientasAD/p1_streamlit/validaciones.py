import re
from datetime import datetime
import streamlit as st

def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def validar_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def validar_telf(texto):
    patron = r'^\d{7,10}$'
    return re.match(patron, texto) is not None

def validar_formulario(nombre, apellido, email, telefono, direccion):
    campos_no_validos = []
    if not nombre:
        campos_no_validos.append('Nombre')
    if not apellido:
        campos_no_validos.append('Apellido')
    if not validar_email(email):
        campos_no_validos.append('Email')
    if not validar_telf(telefono):
        campos_no_validos.append('Teléfono')
    if not direccion:
        campos_no_validos.append('Dirección')
    
    if len(campos_no_validos) > 0:
        st.warning(f'Los siguientes campos no pueden estar en blanco o contener errores de formato:\n{", ".join(campos_no_validos)}.')
        return False
    
    return True
