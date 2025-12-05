Descripción del Código
Este script de Python utiliza la biblioteca streamlit para crear una aplicación web interactiva destinada al análisis de un conjunto de datos de vehículos (vehicles_us.csv). La aplicación carga los datos y presenta varias visualizaciones para que el usuario pueda explorarlos.

A continuación se detalla lo que hace cada parte del código:

Configuración Inicial:

Importa las bibliotecas necesarias: pandas para la manipulación de datos, plotly.express para crear gráficos interactivos y streamlit para construir la aplicación web.
Aplica un estilo CSS simple para cambiar el color de fondo de la aplicación a un azul claro (#ADD8E6).
Carga de Datos y Visualización de la Tabla:

Muestra el encabezado principal: "Análisis de Datos de Vehículos".
Carga los datos desde el archivo vehicles_us.csv en un DataFrame de pandas.
Ofrece una casilla de verificación (checkbox) que permite al usuario decidir si quiere ver la tabla completa de datos. Si la marca, se muestra el DataFrame en la aplicación.
Gráfico de Barras: Tipos de Vehículo por Modelo:

Crea un gráfico de barras que muestra la cantidad de anuncios para cada modelo de vehículo.
Las barras están coloreadas según el tipo de vehículo (ej. "sedan", "SUV"), lo que permite comparar la popularidad de los diferentes tipos dentro de cada modelo.
Histograma: Condición vs. Año del Modelo:

Genera un histograma que distribuye la cantidad de vehículos según el año del modelo (model_year).
Las barras están coloreadas por la condición del vehículo (ej. "nuevo", "como nuevo", "bueno"), mostrando cómo varía la condición de los vehículos a lo largo de los años.
Histograma Interactivo: Comparación de Precios:

Esta es la sección más interactiva de la aplicación.
Presenta dos menús desplegables donde el usuario puede seleccionar dos modelos de vehículos diferentes de la lista.
Crea un histograma que superpone las distribuciones de precios (price) de los dos modelos seleccionados, facilitando su comparación directa.
Incluye una casilla de verificación para "normalizar" el histograma. Si se selecciona, el eje Y muestra el porcentaje en lugar del conteo de anuncios, lo que es útil para comparar modelos con cantidades de anuncios muy diferentes.
Muestra una advertencia si el usuario selecciona el mismo modelo en ambos menús.
