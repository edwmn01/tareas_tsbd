import mysql.connector
import streamlit as st

def conectar_db():
    try:
        conexion = mysql.connector.connect(
            user='root',
            password='1999',
            host='localhost',
            database='had_p1_streamlit_personas',
        )
        return conexion
    except mysql.connector.Error as err:
        return None

def insertar_persona(nombre, apellido, cedula, edad, correo, estado_civil, telefono, direccion, genero):
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        sql = 'INSERT INTO persona (nombre, apellido, cedula, edad, correo, estado_civil, telefono, direccion, genero) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        valores = (nombre, apellido, cedula, edad, correo, estado_civil, telefono, direccion, genero)
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        st.success('Persona agregada exitosamente!')
    else:
        st.error('Falló la conexión con la base de datos!')


def obtener_personas():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        sql = 'SELECT * FROM persona'
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultados
    else:
        st.error('Falló la conexión con la base de datos!')
        return []
