import streamlit as st

def configuracion_inicial_web():
    st.set_page_config(
        page_title="PFRendimientoC3",  
        page_icon="./recursos/img/favicon.png",            
        layout="wide"                       
    )

    st.title("Proyecto Final - Rendimiento Estudiantil")


def generar_sidebar_web():
    st.sidebar.markdown("## 📂 Navegación")

    opcion = st.sidebar.radio("", ("📊 Estadísticas", "🔮 Predicciones"), label_visibility="collapsed")

    if opcion == "📊 Estadísticas":
        generar_tabs_categorias_estadisticas()
        
    elif opcion == "🔮 Predicciones":
        st.header("🔮 Predicciones")


def generar_tabs_categorias_estadisticas():
    st.header("📊 Estadísticas")

    tabs_categorias = st.tabs(["Demográficas", "Salud", "Educación", "Financieros"])

    with tabs_categorias[0]:
        pass

    with tabs_categorias[1]:
        pass

    with tabs_categorias[2]:
        pass

    with tabs_categorias[3]:
        pass