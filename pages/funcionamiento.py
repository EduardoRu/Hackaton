import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="Funcionamiento de minas", page_icon="📈")
st.sidebar.header('Barra de navegación')

st.header('Monitoreo de datos')

st.markdown('Monitoro de datos de temperatura y humedad, dentro de la mina en conjunto de un vehiculo no tripulado (Drone)')

col1, col2 = st.columns(2)

st.header('Demostración de una mina', '10')
st.markdown('Simulación del dron, haciendo un recorrido dentro de una mina, recolectando datos')
image1 = Image.open('img/minas.png')
st.image(image=image1)
    

st.header('Datos arrojados por el drone')
st.markdown('Colección y envio de datos (Mostrados en la consola de una computadora)')
image2 = Image.open('img/monitor_Datos.png')
st.image(image=image2)