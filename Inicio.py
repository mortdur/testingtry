import requests
from requests.api import request
import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import hydralit_components as hc
import datetime
def main():
    st.set_page_config(page_title="Mi página con Streamlit y Bootstrap")

# Crear un contenedor con Streamlit
with st.container():
    # Agregar la barra de navegación de Bootstrap
    st.markdown(
        """
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <div class="container-fluid">
            <a class="navbar-brand" href="#">Mi página</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav">
                <li class="nav-item">
                  <a class="nav-link active" aria-current="page" href="#">Inicio</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Acerca de</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Contacto</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
        """,
        unsafe_allow_html=True
    )

    # Agregar el formulario de búsqueda
    st.markdown(
        """
        <form class="d-flex">
          <input class="form-control me-2" type="search" placeholder="Buscar" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Buscar</button>
        </form>
        """
        , unsafe_allow_html=True
    )

# Agregar contenido adicional
st.header("Bienvenidos a mi página")
st.write("Esta es una página creada con Streamlit y Bootstrap.")

if __name__ == "__main__":
    main()
