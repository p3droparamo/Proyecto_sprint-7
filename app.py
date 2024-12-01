import streamlit as st
import pandas as pd
import plotly_express as px
import os

# Obtener la ruta del directorio actual donde está el script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Intentar cargar el archivo usando diferentes rutas
try:
    # Primero intenta la ruta local específica
    car_data = pd.read_csv('C:/Users/Paramo/Proyecto_sprint-7/vehicles_us.csv')
except FileNotFoundError:
    try:
        # Si falla, intenta con ruta relativa al directorio actual
        csv_path = os.path.join(current_dir, 'vehicles_us.csv')
        car_data = pd.read_csv(csv_path)
    except FileNotFoundError:
        # Si aún falla, intenta con ruta simple (para Render)
        car_data = pd.read_csv('vehicles_us.csv')

# Crear el encabezado principal
st.header('Análisis de Datos de Vehículos')

# Crear sección para los gráficos
st.subheader('Visualización de Datos')

# Checkbox para el histograma
show_histogram = st.checkbox('Mostrar histograma del odómetro')
if show_histogram:
    st.write('Distribución de lecturas del odómetro en los vehículos')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Checkbox para el gráfico de dispersión
show_scatter = st.checkbox('Mostrar gráfico de dispersión precio vs. odómetro')
if show_scatter:
    st.write('Relación entre precio y kilometraje')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)