import streamlit as st
import pandas as pd
import plotly_express as px

# Leer el archivo CSV
car_data = pd.read_csv('C:/Users/Paramo/Proyecto_sprint-7/vehicles_us.csv')

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