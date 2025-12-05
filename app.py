# import time
import pandas as pd
import plotly.express as px
import streamlit as st
# from numpy.random import default_rng as rng
# import numpy as np

st.markdown(
    """
    <style>
    .stApp {
        background-color: #ADD8E6;
        
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header('Análisis de Datos de Vehículos')

#car_data = pd.read_csv('C:/Users/MonoTono2/Documents/Curso_TripleTen/Proyectos/Sprint_7/GitHub_Ejercicios/vehicles_us.csv')
car_data = pd.read_csv('vehicles_us.csv')


show_dataframe = st.checkbox('Mostrar tabla completa del conjunto de datos')

if show_dataframe:
    st.write('Tabla completa del conjunto de datos de vehículos en EE.UU.:')
    st.dataframe(car_data, width=1200, height=700)

st.header('Comparación de Tipos de Vehículo por Modelo')

# Crear el gráfico de barras apiladas
# Contamos las ocurrencias para que el gráfico tenga sentido
fig_bar = px.bar(car_data,
                 x='model',
                 color='type',
                 title='Cantidad de Vehículos por Modelo y Tipo',
                 labels={'model': 'Modelo del Vehículo', 'count': 'Cantidad de Anuncios', 'type': 'Tipo de Vehículo'})

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig_bar, use_container_width=True)

st.header('Histograma de Condición vs. Año del Modelo')

# Crear el histograma
fig_hist = px.histogram(car_data,
                        x='model_year',
                        color='condition',
                        title='Distribución de la Condición de Vehículos por Año del Modelo',
                        labels={'model_year': 'Año del Modelo', 'count': 'Cantidad de Vehículos', 'condition': 'Condición'})

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig_hist, use_container_width=True)

st.header('Comparación de Precios entre Modelos')

# Obtener la lista de modelos únicos para los menús desplegables
model_list = sorted(car_data['model'].unique())

# Crear dos menús desplegables para que el usuario seleccione los modelos
model_1 = st.selectbox('Selecciona el primer modelo:', model_list, index=0)
model_2 = st.selectbox('Selecciona el segundo modelo:', model_list, index=1)

# Añadir un checkbox para la normalización
normalize_hist = st.checkbox('Normalizar distribución (mostrar como %)')

# Filtrar el dataframe para incluir solo los dos modelos seleccionados
comparison_df = car_data[car_data['model'].isin([model_1, model_2])]

# Crear un histograma para comparar la distribución de precios
if not comparison_df.empty and model_1 != model_2:
    # Definir parámetros del gráfico basados en la normalización
    if normalize_hist:
        histnorm_val = 'percent'
        y_axis_label = 'Porcentaje de Distribución'
    else:
        histnorm_val = None  # El valor predeterminado es el conteo
        y_axis_label = 'Cantidad de Anuncios'

    fig_price_hist = px.histogram(
        comparison_df,
        x='price',
        color='model',
        title=f'Distribución de Precios: {model_1} vs. {model_2}',
        labels={'price': 'Precio (USD)', 'y': y_axis_label},
        histnorm=histnorm_val,
        barmode='overlay',  # Superpone los histogramas para una mejor comparación
        opacity=0.7
    )
    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_price_hist, use_container_width=True)
elif model_1 == model_2:
    st.warning('Por favor, selecciona dos modelos diferentes para comparar.')
