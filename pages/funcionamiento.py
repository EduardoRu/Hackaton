import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Funcionamiento de minas", page_icon="馃搱")
st.sidebar.header('Barra de navegaci贸n')

st.header('Monitoreo de datos')

st.markdown('Monitoro de datos de temperatura y humedad, dentro de la mina en conjunto de un vehiculo no tripulado (Drone)')

col01, col02 = st.columns(2)
with col01:
    st.header('Recorrido Drone')
    st.markdown('El drone dar谩 un recorrido adjunto a sensores que apoyan el mejor reconocimiento y recolecci贸n de datos')
with col02:
    image0 = Image.open('img/recorrido_drone.jpeg')
    st.image(image=image0)

st.header('Demostraci贸n de una mina')
st.markdown('Simulaci贸n del dron, haciendo un recorrido dentro de una mina, recolectando datos')
image1 = Image.open('img/Cave.png')
st.image(image=image1)
    

st.header('Datos temperatura y humedad detectados por el drone')
st.markdown('Colecci贸n y envio de datos (Mostrados en la consola de una computadora)')

col3, col4 = st.columns(2)

with col3:
    image2 = Image.open('img/monitor_Datos.PNG')
    st.image(image=image2)
with col4:
    image02 = Image.open('img/scanMina.jpeg')
    st.image(image=image02)

st.header('Control estadistico')
st.markdown('Grafiaci贸n de datos estadisticos detectados por los sensores')

chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['Temperatura', 'Humedad'])

st.area_chart(chart_data)

st.header('Modelado 3D')
st.markdown('De acuerdo al recorrido del drone y recolecci贸n de imagenes, se creara un modelado 3D para la infromaci贸n general de la mina y la capacitaci贸n de mineros')
age3 = Image.open('img/modelado_3d.jpeg')
st.image(image=age3)

col1, col2 = st.columns(2)

with col1:
    st.header('Nube de puntos')
    st.markdown('Se pleanea hacer un recorrido con una nube de puntos para tener un mejor reconocimiento de gritas y profunidad de la mina')

with col2:
    age4 = Image.open('img/nube_puntos.jpeg')
    st.image(image=age4)