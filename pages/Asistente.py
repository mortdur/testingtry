import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from selenium import webdriver

icon = Image.open('img/icon.png')
st.set_page_config(
	page_title = 'SaveYourLife Tumor Brain Predict!',
	page_icon = icon,
	layout = 'wide',
	initial_sidebar_state = 'collapsed',
	menu_items={
		'Get Help': 'https://streamlit.io',
		'Report a bug': 'https://github.com',
		'About':'About your application: **Hello World!**'
	}
	)
st.sidebar.title("Main Menu")

def chatbot(user_input):
    response = ""
    if "hola" in user_input:
        response = "Hola! ¿Cómo puedo ayudarte?"
    elif "asistente" in user_input or "llamas" in user_input:
        response = "Me llamo Josua."
    elif "hacer" in user_input:
        response = "Estoy aquí para ayudarte con cualquier pregunta que tengas."
    elif "información" in user_input:
        query = user_input.replace("información", "").strip()
        results = search_google(query)
        if not results:
            response = "No he encontrado resultados."
        else:
            response = "Aquí tienes lo que he encontrado en Google:"
            for result in results:
                response += "\n- [{}]({})".format(result["title"], result["link"])
    else:
        response = "Lo siento, parece que hay un problema con tu mensaje. Por favor, escríbelo de nuevo."
    return response

def search_google(query):
    results = []
    driver = webdriver.Firefox()
    driver.get(f"https://www.google.com/search?q={query}")
    links = driver.find_elements_by_css_selector("div.r a")
    for link in links:
        title = link.find_element_by_css_selector("h3").text
        url = link.get_attribute("href")
        results.append({"title": title, "link": url})
    driver.quit()
    return results

if __name__ == '__main__':
    st.title("Chatbot")
    user_input = st.text_input("Introduce tu mensaje:", value="soy tu asistente, en que puedo ayudarte").lower()
    if st.button('Enviar'):
        response = chatbot(user_input)
        st.write(response)
        
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
