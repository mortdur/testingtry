import requests
from requests.api import request
import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
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
title_container = st.container()
col1, col2 = st.columns([3, 20])
image = Image.open('img/logo.png')
with title_container:
   with col1:
    st.image(image, width=130)
   with col2:
     st.markdown('<h1 style="color: #28cffe;">SaveYourLife</h1>',unsafe_allow_html=True)
#st.image('img/logo.png')
#st.title("SaveYourLife Tumor Brain Predict!")
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
   components.html('<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Sunsets don&#39;t get much better than this one over <a href="https://twitter.com/GrandTetonNPS?ref_src=twsrc%5Etfw">@GrandTetonNPS</a>. <a href="https://twitter.com/hashtag/nature?src=hash&amp;ref_src=twsrc%5Etfw">#nature</a> <a href="https://twitter.com/hashtag/sunset?src=hash&amp;ref_src=twsrc%5Etfw">#sunset</a> <a href="http://t.co/YuKy2rcjyU">pic.twitter.com/YuKy2rcjyU</a></p>&mdash; US Department of the Interior (@Interior) <a href="https://twitter.com/Interior/status/463440424141459456?ref_src=twsrc%5Etfw">May 5, 2014</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>',height=420,width=350)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
