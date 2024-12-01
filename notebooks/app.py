import pandas as pd
import plotly_express as px
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Dashboard de Vehículos",
    page_icon="🚗",
    layout="wide"
)

# Título principal
st.header("📊 Dashboard de Análisis de Vehículos")

# Cargar datos
try:
    car_data = pd.read_csv('vehicles_us.csv')
    
    # Botón para mostrar histograma del odómetro
    hist_button = st.button('Construir histograma de kilometraje')
    
    if hist_button:
        st.write('Histograma de la distribución del kilometraje en los vehículos')
        
        # Crear histograma
        fig = px.histogram(
            car_data, 
            x="odometer",
            title="Distribución del Kilometraje",
            labels={'odometer': 'Kilometraje', 'count': 'Cantidad de Vehículos'},
            color_discrete_sequence=['#1f77b4']  # Color azul para el histograma
        )
        
        # Actualizar el diseño
        fig.update_layout(
            bargap=0.1,  # Espacio entre barras
            showlegend=False,
            plot_bgcolor='white'
        )
        
        # Mostrar el gráfico
        st.plotly_chart(fig, use_container_width=True)
        
        # Mostrar estadísticas básicas
        st.write("### Estadísticas del kilometraje")
        stats = car_data['odometer'].describe()
        st.write(f"- Promedio: {stats['mean']:,.0f} km")
        st.write(f"- Mediana: {stats['50%']:,.0f} km")
        st.write(f"- Máximo: {stats['max']:,.0f} km")
        st.write(f"- Mínimo: {stats['min']:,.0f} km")

except FileNotFoundError:
    st.error("⚠️ Error: No se encontró el archivo 'vehicles_us.csv'. Por favor, asegúrate de que el archivo esté en el mismo directorio que este script.")