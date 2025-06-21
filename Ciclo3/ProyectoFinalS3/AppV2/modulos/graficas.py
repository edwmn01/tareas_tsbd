import plotly.express as px


def pastel(df, nombre_col, titulo):
    fig = px.pie(df, names=nombre_col, title=titulo)
    return fig
