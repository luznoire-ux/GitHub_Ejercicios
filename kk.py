# Hola KK
import plotly.express as px
  
import streamlit  
print("Hola KK")
print("streamlit",streamlit.__version__)


try:
    import nbformat
    print("La librería nbformat está instalada.")
    print(f"Versión de nbformat: {nbformat.__version__}")
except ImportError:
    print("La librería nbformat NO está instalada.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
