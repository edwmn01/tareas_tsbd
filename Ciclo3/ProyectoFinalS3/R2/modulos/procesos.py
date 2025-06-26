import pandas as pd


df_general = pd.read_excel('/home/eduardo/Documentos/GH/justinGH/Proyecto-Final-Ciclo-3/Documentacion/Data/DatosLimpiosFichas2024-2_2025-1.xlsx')

def sexo_estudiantes_por_carrera():
    df_filtro = df_general[['Sexo', 'CarreraMatriculadoTEC', 'CicloCarrera', 'PeriodoAcademico']]
    print(df_filtro.head())
    return df_filtro

def genero_estudiantes_por_carrera():
    df_filtro = df_general[['Genero', 'CarreraMatriculadoTEC', 'CicloCarrera', 'PeriodoAcademico']]
    print(df_filtro.head())
    return df_filtro