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
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
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
   components.html('<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Sunsets don&#39;t get much better than this one over <a href="https://twitter.com/GrandTetonNPS?ref_src=twsrc%5Etfw">@GrandTetonNPS</a>. <a href="https://twitter.com/hashtag/nature?src=hash&amp;ref_src=twsrc%5Etfw">#nature</a> <a href="https://twitter.com/hashtag/sunset?src=hash&amp;ref_src=twsrc%5Etfw">#sunset</a> <a href="http://t.co/YuKy2rcjyU">pic.twitter.com/YuKy2rcjyU</a></p>&mdash; US Department of the Interior (@Interior) <a href="https://twitter.com/Interior/status/463440424141459456?ref_src=twsrc%5Etfw">May 5, 2014</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>',height=420,width=350)
# LINK TO THE CSS FILE
with open('.streamlit/style.css')as f:
 st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
