import mysql.connector
import streamlit as st

def conectar_db():
    try:
        conexion = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='had_p1_streamlit_clientes',
        )
        return conexion
    except mysql.connector.Error as err:
        return None

def insertar_cliente(nombre, apellido, fecha_nac, email, sexo, telefono, direccion):
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        sql = 'INSERT INTO cliente (nombre, apellido, fecha_nacimiento, email, sexo, telefono, direccion) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        valores = (nombre, apellido, fecha_nac, email, sexo, telefono, direccion)
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        st.success('Cliente agregado exitosamente!')
    else:
        st.error('Falló la conexión con la base de datos!')
