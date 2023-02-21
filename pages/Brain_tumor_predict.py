import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="SaveYourLife Tumor Brain Predict",
    page_icon="🤯",
    initial_sidebar_state="collapsed",
    layout="wide"
)

st.markdown("<h1 style='text-align: center; color: white;'>Predicción de Tumores Cerebrales</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Proyecto Deep Learning</h2>", unsafe_allow_html=True)

df = pd.DataFrame( columns = ['Nombre', 'Apellidos','Edad', 'Sexo', 'Numero de la Seguridad Social','Ecg en reposo', 'imagen'])
image = 'img/cerebro_1.png'

col1, col2, col3 = st.columns(3)

with col1:
    st.write("")

with col2:
    st.image(image,  use_column_width= 'auto')

with col3:
    st.write("")

nombre = st.text_input("Introduce el nombre del paciente", max_chars=10, value="Pepe", help= 'Introduce el nombre del paciente')
apellidos = st.text_input("Introduce los apellidos del paciente", max_chars=30, value="Viruela Sarampión", help= 'Introduce los apellidos del paciente')

col1, col2 = st.columns(2)

with col1:
    edad = st.number_input("edad",step=1, value=20, help= 'Introduce la edad del paciente')
    numero_ss = st.text_input(" numero seguridad social", max_chars=11, help= 'Introduce el numero de la seguridad social')


with col2:
    sexo = st.selectbox("sexo", ("Hombre", "Mujer"), help= 'Introduce el sexo del paciente')
    ecg_reposo = st.selectbox("Resultados electrocardiográficos en reposo", ["Normal", "Tener anomalía de la onda ST-T", "Mostrando una hipertrofia ventricular izquierda probable"], help= 'Introduce los resultados del electrocardigrama en reposp del paciente')

# Function para leer y manipular imagenes
def load_image(img):
    im = Image.open(img)
    image = np.array(im)
    return image

# subir los ficheros de la imagen 
uploadFile = st.file_uploader(label="subir imagen", type=['jpg', 'png'])

# chequeando el formato de la iamgen
if uploadFile is not None:
    img = load_image(uploadFile)
    st.image(img)
    st.write("Imagen subida correctamente")
else:
    st.write("la imagen debe tener un formato JPG/PNG.")

if st.button("Calcular la salida"):
    input_data_num = [nombre, apellidos, edad, sexo, numero_ss, ecg_reposo, img]

    df = df.append(input_data_num, ingnore_index= True)
    print("hola")