import requests
import pandas as pd
#   import streamlit as st
import db

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
else:
    print("Error al consumir la API")
    exit()


'''for user in users:
    db.insertar_usuarios(user)

print("Datos guardados exitosamente.")'''


df_usuarios = pd.DataFrame(db.obtener_usuarios(), columns=['id', 'name', 'username', 'email', 'phone', 'website'])

print(df_usuarios.head(5))

#st.title('Usuarios registrados en la base de datos')
#st.dataframe(df_usuarios)