import streamlit as st
import modulos.procesos as prc
import modulos.graficas as grf

def configuracion_inicial_web():
    st.set_page_config(
        page_title="Rendimiento Estudiantil",  
        page_icon="🍃",            
        layout="wide"                       
    )

    st.title("Proyecto Final - Rendimiento Estudiantil")


def generar_sidebar_web():
    st.sidebar.markdown("## 📂 Navegación")

    opcion = st.sidebar.radio("", ("📊 Estadísticas", "🔮 Predicciones"), label_visibility="collapsed")

    if opcion == "📊 Estadísticas":
        tabs_categorias_estadisticas()
        
    elif opcion == "🔮 Predicciones":
        st.header("🔮 Predicciones")


def tabs_categorias_estadisticas():

    tabs_categorias = st.tabs(["Demográficas", "Salud", "Educación", "Financieros"])

    with tabs_categorias[0]:
        tabs_graficas_demograficas()

    with tabs_categorias[1]:
        pass

    with tabs_categorias[2]:
        pass

    with tabs_categorias[3]:
        pass


def tabs_graficas_demograficas():
    
    tabs_categorias = st.tabs(["Distribución por sexo", "Distribución por genero"])

    df = prc.df_general

    carreras = ['Todos'] + sorted(df['CarreraMatriculadoTEC'].unique().tolist())
    ciclos = ['Todos'] + sorted(df['CicloCarrera'].unique().tolist())
    periodos = ['Todos'] + sorted(df['PeriodoAcademico'].unique().tolist())

    filtro_carrera = st.selectbox("Carrera", carreras)
    filtro_ciclo = st.selectbox("Ciclo de Carrera", ciclos)
    filtro_periodo = st.selectbox("Periodo Académico", periodos)


    with tabs_categorias[0]:
        filtro_por_sexo( filtro_carrera,  filtro_ciclo, filtro_periodo)

    with tabs_categorias[1]:
        filtro_por_genero(filtro_carrera,  filtro_ciclo, filtro_periodo)

def filtro_por_sexo(filtro_carrera,  filtro_ciclo, filtro_periodo):
    df = prc.sexo_estudiantes_por_carrera()

    
    df_filtrado = df.copy()

    if filtro_carrera != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['CarreraMatriculadoTEC'] == filtro_carrera]

    if filtro_ciclo != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['CicloCarrera'] == filtro_ciclo]

    if filtro_periodo != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['PeriodoAcademico'] == filtro_periodo]

    st.header("Distribución de Sexo de Estudiantes")

    if df_filtrado.empty:
        st.warning("No hay datos para los filtros seleccionados.")
    else:
        st.plotly_chart(grf.pastel(df_filtrado, 'Sexo', 'Distribución por Sexo'), use_container_width=True)


def filtro_por_genero(filtro_carrera,  filtro_ciclo, filtro_periodo):
    df = prc.genero_estudiantes_por_carrera()

    df_filtrado = df.copy()

    if filtro_carrera != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['CarreraMatriculadoTEC'] == filtro_carrera]

    if filtro_ciclo != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['CicloCarrera'] == filtro_ciclo]

    if filtro_periodo != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['PeriodoAcademico'] == filtro_periodo]

    st.header("Distribución de Genero de Estudiantes")

    if df_filtrado.empty:
        st.warning("No hay datos para los filtros seleccionados.")
    else:
        st.plotly_chart(grf.pastel(df_filtrado, 'Genero', 'Distribución por Genero'), use_container_width=True)

