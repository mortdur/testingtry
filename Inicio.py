import requests
from requests.api import request
import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import hydralit_components as hc
import datetime

#make it look nice from the start
st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)

# specify the primary menu definition
menu_data = [
    {'icon': "far fa-copy", 'label':"Left End"},
    {'id':'Copy','icon':"🐙",'label':"Copy"},
    {'icon': "fa-solid fa-radar",'label':"Dropdown1", 'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Sub-item 1"},{'id':'subid12','icon': "💀", 'label':"Sub-item 2"},{'id':'subid13','icon': "fa fa-database", 'label':"Sub-item 3"}]},
    {'icon': "far fa-chart-bar", 'label':"Chart"},#no tooltip message
    {'id':' Crazy return value 💀','icon': "💀", 'label':"Calendar"},
    {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
    {'icon': "far fa-copy", 'label':"Right End"},
    {'icon': "fa-solid fa-radar",'label':"Dropdown2", 'submenu':[{'label':"Sub-item 1", 'icon': "fa fa-meh"},{'label':"Sub-item 2"},{'icon':'🙉','label':"Sub-item 3",}]},
]

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    login_name='Logout',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='sticky', #jumpy or not-jumpy, but sticky or pinned
)

if st.button('click me'):
  st.info('You clicked at: {}'.format(datetime.datetime.now()))


if st.sidebar.button('click me too'):
  st.info('You clicked at: {}'.format(datetime.datetime.now()))

#get the id of the menu item clicked
st.info(f"{menu_id}")
title_container = st.container()
col1, col2 = st.columns([3, 20])
image = Image.open('img/logo.png')
with title_container:
   with col1:
    st.image(image, width=130)
   with col2:
     st.markdown('<h1 style="color: #28cffe;">SaveYourLife</h1>',unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
   st.image('img/cerebro.png')
   with st.expander("Tumor cerebral"):
    st.text("Aqui podremos predecir si tenemos un tumor y de que tipo")

with col2:
   st.image('img/cerebro.png')
   with st.expander("Cancer de ma"):
    st.text("Aqui podremos predecir si tenemos cancer de mama y de que tipo")
with col3:
 col1, col2 = st.columns([20, 8])
with col1:
     st.markdown("""
      La página web del SaveYourLife de Predicción de Tumores es un sitio dedicado a brindar información y servicios relacionados con la detección temprana 
      y la predicción de tumores mediante el uso de inteligencia artificial. En la página principal, los visitantes pueden encontrar información sobre los 
      trabajos que realizamos, el equipo de investigación, las tecnologías utilizadas y los resultados obtenidos. También se destacan los servicios disponibles, 
      como la detección temprana de cáncer mediante la evaluación de imágenes médicas y la predicción del riesgo de desarrollar ciertos tipos de tumores. 
      
      Además, la página web ofrece acceso a herramientas y recursos para pacientes y profesionales de la salud, como la carga de imagenes para la evaluación médica
      y la visualización de resultados de investigaciones recientes.
      Los visitantes también pueden acceder a un blog de twitter actualizado regularmente con noticias, estudios y artículos relacionados con la investigación 
      de tumores y la inteligencia artificial.
      La página web de SaveYourLife de Predicción de Tumores es fácil de navegar y está diseñada para ser accesible tanto para expertos en el tema como para 
      el público en general. La plataforma es moderna y segura, y se encuentra respaldada por un equipo de expertos en tecnología y seguridad informática 
      para garantizar la protección de la información del usuario y la privacidad de los datos.
      """) 
# LINK TO THE CSS FILE
with open('.streamlit/style.css')as f:
 st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
