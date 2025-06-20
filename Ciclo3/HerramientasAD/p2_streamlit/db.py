import mysql.connector

def conectar_db():
    try:
        conexion = mysql.connector.connect(
            user='root',
            password='1999',
            host='localhost',
            database='usuariosdb',
        )
        return conexion
    except mysql.connector.Error as err:
        return None
    

def crear_tablas():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT PRIMARY KEY,
            name TEXT,
            username TEXT,
            email TEXT,
            phone TEXT,
            website TEXT
        )
        ''')
        conexion.commit()
        cursor.close()
        conexion.close()
        print('\nCreación de tablas con éxito!!\n')


def insertar_usuarios(usuario):
    crear_tablas()
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        sql = 'INSERT INTO users (id, name, username, email, phone, website) VALUES (%s, %s, %s, %s, %s, %s)'
        valores = ( usuario['id'], usuario['name'],
                    usuario['username'], usuario['email'],
                    usuario['phone'], usuario['website'])
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        print('\nUsuario registrado con éxito!!\n')

def obtener_usuarios():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        sql = 'SELECT * FROM users'
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultados
    else:
        print('\nFalló la conexión con la base de datos!!\n')
        return []


