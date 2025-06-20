import plotly.express as px


def pastel_sexo_estudiantes(df):
    fig = px.pie(
        df,
        names='Sexo',
        title='Distribución por Sexo',
    )

    return fig