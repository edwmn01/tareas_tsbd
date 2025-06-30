#pip install streamlit-option-menu

import streamlit as st
from streamlit_option_menu import option_menu

# Menú tipo hamburguesa en el sidebar
with st.sidebar:
    seleccion = option_menu(
        "Menú",  # Título del menú
        ["Inicio", "Datos", "Acerca de"],  # Opciones
        icons=["house", "bar-chart", "info-circle"],  # Íconos (de Bootstrap)
        menu_icon="list",  # Ícono tipo hamburguesa
        default_index=0,
    )

# Contenido según opción seleccionada
if seleccion == "Inicio":
    st.title("Página de Inicio")
    st.write("Bienvenido a la página de inicio.")
elif seleccion == "Datos":
    st.title("Análisis de Datos")
    st.write("Aquí iría un gráfico, tabla, etc.")
elif seleccion == "Acerca de":
    st.title("Sobre esta App")
    st.write("Esta es una demo con menú hamburguesa.")

