import pandas as pd

import plotly.graph_objects as go
import plotly.express as px


# =============================== GRÁFICA 1 ===============================
def total_por_mes_tipo(df):
    grouped = df.groupby(['mes_str', 'internal_type'])['total'].sum().reset_index()
    pivoted = grouped.pivot(index='mes_str', columns='internal_type', values='total').fillna(0)

    fig = go.Figure()

    for col in pivoted.columns:
        fig.add_trace(go.Bar(
            x=pivoted.index,
            y=pivoted[col],
            name=col
        ))

    fig.update_layout(
        barmode='stack',
        title='Total por mes y tipo',
        xaxis_title='Meses',
        yaxis_title='Total',
        xaxis_tickangle=-90,
        legend_title_text='Tipo',
        width=900,
        height=600,
        margin=dict(t=50, b=150, l=50, r=50)
    )

    return fig


# =============================== GRÁFICA 2 ===============================
def evolucion_mensual(df, meses):
    total_mes = df.groupby('mes_str')['total'].sum().reset_index()

    total_mes['mes_str'] = pd.Categorical(total_mes['mes_str'], categories=list(meses.values()), ordered=True)
    total_mes = total_mes.sort_values('mes_str')

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=total_mes['mes_str'],
        y=total_mes['total'],
        mode='lines+markers',
        name='Total'
    ))

    fig.update_layout(
        title='Evolución Mensual de los Montos Totales',
        xaxis_title='Mes',
        yaxis_title='Monto Total',
        xaxis_tickangle=-45,
        width=900,
        height=500,
        margin=dict(t=50, b=100, l=70, r=40)
    )

    return fig


# =============================== GRÁFICA 3 ===============================
def monto_total_por_tipo(df):
    totales_por_tipo = df.groupby('internal_type')['total'].sum().reset_index()

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

    fig.update_layout(
        title='Distribución total por tipo de contratación',
        margin=dict(t=50, b=50, l=50, r=50),
        width=700,
        height=700
    )

    return fig


# =============================== GRÁFICA 4 ===============================
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
    fig.update_layout(
        legend_title_text='Tipo de Contratación',
        margin=dict(t=50, b=50, l=50, r=50),
        width=900,
        height=600
    )

    return fig


# =============================== GRÁFICA 5 ===============================
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

    fig.update_layout(
        xaxis_tickangle=-45,
        legend_title_text='Tipo Contratación',
        margin=dict(t=50, b=150, l=50, r=50),
        width=900,
        height=600
    )

    return fig