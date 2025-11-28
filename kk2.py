import pandas as pd
import plotly.express as px
import streamlit as st

# Lee el archivo CSV
car_data = pd.read_csv('C:/Users/MonoTono2/Documents/Curso_TripleTen/Proyectos/Sprint_7/GitHub_Ejercicios/datasets/vehicles_us.csv') # leer los datos

# Añadir un encabezado a la aplicación
st.header('Análisis de Datos de Vehículos')

# Crear un botón para el histograma
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
