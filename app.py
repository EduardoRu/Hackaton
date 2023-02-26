import streamlit as st
import pandas as pd
import numpy as np
import firestoreCrud as fsCRUD
import json

# LLamado de datos para firebase

docs = fsCRUD.getDocument()

#jsonData = {el.id: el.to_dict() for el in docs}

for e in docs:
    st.markdown(e.to_dict()["nom_mina"])

# Estructura de la pagina

st.title('Aplicación para el monitorieo de la mina')

st.header('La tecnología va de la mano para un trabajador en el conocimiento para prevenirse de los riesgos')
st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi feugiat nisl lacinia blandit suscipit. Nullam ac viverra ligula, non blandit augue. Fusce pharetra turpis quam, vel varius ipsum ornare at. Praesent vehicula, orci eget imperdiet pharetra, nisi lacus scelerisque est, quis placerat nisl nisl bibendum nulla. Aliquam lectus eros, porttitor et accumsan id, placerat in leo. Integer eu eros ligula. Mauris et tortor justo. Nam ut cursus quam. Etiam posuere massa vitae blandit congue. Aenean varius sit amet lacus porttitor placerat. Vivamus sit amet orci elementum, molestie felis eu, dictum justo. Fusce maximus ligula in ultrices varius. Vivamus vitae condimentum felis. Praesent ut eros et enim congue venenatis.')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)