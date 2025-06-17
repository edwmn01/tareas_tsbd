import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from prophet.plot import plot_plotly

# ================================ Funciones de configuración de gráficos ================================
def configure_bar_chart(fig, title, x_label, y_label, x_tick_angle=-90):
    fig.update_layout(
        barmode='stack',
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        xaxis_tickangle=x_tick_angle,
        legend_title_text='Tipo',
        width=900,
        height=600,
        margin=dict(t=50, b=150, l=50, r=50)
    )
    return fig


def configure_line_chart(fig, title, x_label, y_label, x_tick_angle=-45):
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        xaxis_tickangle=x_tick_angle,
        legend_title_text='Tipo Contratación',
        margin=dict(t=50, b=150, l=50, r=50),
        width=900,
        height=600
    )
    return fig


def configure_pie_chart(fig, title, hole=0):
    fig.update_layout(
        title=title,
        margin=dict(t=50, b=50, l=50, r=50),
        width=700,
        height=700
    )
    return fig


def configure_scatter_chart(fig, title, x_label, y_label):
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        legend_title_text='Tipo de Contratación',
        margin=dict(t=50, b=50, l=50, r=50),
        width=900,
        height=600
    )
    return fig


# ================================ Funciones de preparación de datos ================================
def group_by_month_type(df):
    return df.groupby(['mes_str', 'internal_type'])['total'].sum().reset_index()


def get_monthly_totals(df):
    return df.groupby('mes_str')['total'].sum().reset_index()


def get_totals_by_type(df):
    return df.groupby('internal_type')['total'].sum().reset_index()


# ================================ Funciones de generación de gráficos ================================
def total_por_mes_tipo(df):
    grouped = group_by_month_type(df)
    pivoted = grouped.pivot(index='mes_str', columns='internal_type', values='total').fillna(0)

    fig = go.Figure()
    for col in pivoted.columns:
        fig.add_trace(go.Bar(x=pivoted.index, y=pivoted[col], name=col))

    return configure_bar_chart(fig, 'Total por mes y tipo', 'Meses', 'Total')


def evolucion_mensual(df, meses):
    total_mes = get_monthly_totals(df)
    total_mes['mes_str'] = pd.Categorical(total_mes['mes_str'], categories=list(meses.values()), ordered=True)
    total_mes = total_mes.sort_values('mes_str')

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=total_mes['mes_str'], y=total_mes['total'], mode='lines+markers', name='Total'))

    return configure_line_chart(fig, 'Evolución Mensual de los Montos Totales', 'Mes', 'Monto Total')


def monto_total_por_tipo(df):
    totales_por_tipo = get_totals_by_type(df)

    N = 10
    top = totales_por_tipo.nlargest(N, 'total')
    otros_total = totales_por_tipo[~totales_por_tipo['internal_type'].isin(top['internal_type'])]['total'].sum()

    if otros_total > 0:
        otros = pd.DataFrame([{'internal_type': 'Otros', 'total': otros_total}])
        totales_por_tipo_final = pd.concat([top, otros], ignore_index=True)
    else:
        totales_por_tipo_final = top

    fig = go.Figure(data=[go.Pie(
        labels=totales_por_tipo_final['internal_type'],
        values=totales_por_tipo_final['total'],
        hole=0,
        hoverinfo='label+percent+value',
        textinfo='percent',
        textfont_size=14,
        sort=False,
        direction='clockwise',
        rotation=90
    )])

    return configure_pie_chart(fig, 'Distribución total por tipo de contratación')


def total_vs_numcontratos(df):
    resumen = df.groupby('internal_type').agg(
        monto_total=('total', 'sum'),
        numero_contratos=('total', 'count')
    ).reset_index()

    fig = px.scatter(
        resumen,
        x='monto_total',
        y='numero_contratos',
        color='internal_type',
        size_max=15,
        title='Monto Total vs Número de Contratos por Tipo de Contratación',
        labels={
            'monto_total': 'Monto Total',
            'numero_contratos': 'Número de Contratos',
            'internal_type': 'Tipo de Contratación'
        }
    )

    fig.update_traces(marker=dict(size=12, opacity=0.8))
    return configure_scatter_chart(fig, 'Monto Total vs Número de Contratos por Tipo de Contratación', 'Monto Total', 'Número de Contratos')


def total_contratos_por_tipo_mes(df):
    fig = px.line(
        df,
        x='mes_str',
        y='total',
        color='internal_type',
        markers=True,
        title='Total de Contratos por Tipo y Mes',
        labels={
            'mes_str': 'Mes',
            'total': 'Total',
            'internal_type': 'Tipo Contratación'
        }
    )

    return configure_line_chart(fig, 'Total de Contratos por Tipo y Mes', 'Mes', 'Total')


# ================================ Funciones de visualización de modelos ================================
def grafica_kmeans(df):
    fig = go.Figure(data=go.Scatter(
        x=df['total'], 
        y=df['contracts'],
        mode='markers',
        marker=dict(
            color=df['cluster'],
            colorscale='Viridis'
        )
    ))
    return configure_scatter_chart(fig, 'Clusters de Provincias/Contratos', 'Total', 'Contracts')


def grafica_prophet(model, forecast):
    fig = plot_plotly(model, forecast)
    return configure_line_chart(fig, 'Predicción de Montos', 'Fecha', 'Valor')


def grafica_clasificacion_RL(df):
    fig = px.scatter(df, x='total', y='contracts', color='year')
    return configure_scatter_chart(fig, 'Clasificación de Contratos por Valor', 'Total', 'Contracts')


def grafica_reduccion_PCA(df, pca_result):
    fig = px.scatter(x=pca_result[:,0], y=pca_result[:,1], color=df['cluster'])
    return configure_scatter_chart(fig, 'Visualización de Clusters con PCA', 'PCA 1', 'PCA 2')


def grafica_isolation_forest(df):
    fig = go.Figure(data=go.Scatter(
        x=df['total'], 
        y=df['contracts'],
        mode='markers',
        marker=dict(
            color=df['anomaly'],
            colorscale='RdBu'
        )
    ))
    return configure_scatter_chart(fig, 'Detección de Contratos Inusuales', 'Total', 'Contracts')
