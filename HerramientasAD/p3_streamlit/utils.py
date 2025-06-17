import requests


provincias = [
    'Todas',
    'AZUAY',
    'BOLIVAR',
    'CAÑAR',
    'CARCHI',
    'CHIMBORAZO',
    'COTOPAXI',
    'EL ORO',
    'ESMERALDAS',
    'GALAPAGOS',
    'GUAYAS',
    'LOS RIOS',
    'MANABI',
    'MORONA SANTIAGO',
    'NAPO',
    'ORELLANA',
    'PICHINCHA',
    'SUCUMBIOS',
    'TUNGURAHUA',
    'ZAMORA CHINCHIPE',
    'SANTA ELENA',
    'COTOPAXI',
    'SANTO DOMINGO DE LOS TSACHILAS',
    'PASTAZA',
    'LOJA'
]

anios_compras_publicas = ['Todos' ,'2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']

tipo_contratacion_compras_publicas = [
    'Todas',
    'Subasta Inversa Electrónica',
    'Catálogo electrónico - Mejor oferta',
    'Catálogo electrónico - Compra directa',
    'Obra artística, científica o literaria',
    'Menor Cuantía',
    'Cotización',
    'Contratos entre Entidades Públicas o sus subsidiarias',
    'Bienes y Servicios únicos',
    'Licitación de Seguros',
    'Contratacion directa',
    'Transporte de correo interno o internacional',
    'Repuestos o Accesorios',
    'Comunicación Social – Contratación Directa'
]

meses = {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre'
}


def get_data(url_base, years, region, type):
    data = []
    for year in years:
        params = {'year': year}
        if region: params['region'] = region
        if type: params['type'] = type

        response = requests.get(url_base, params=params)
        response.raise_for_status()
        year_data = response.json()

        for record in year_data:
            record['year'] = year
        
        data.extend(year_data)

    return data