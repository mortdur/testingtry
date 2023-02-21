import snscrape.modules.twitter as twitter
import streamlit as st

# Crear una instancia de TwitterScraper
scraper = twitter.TwitterScraper()

# Obtener los últimos tweets del usuario especificado
tweets = scraper.get_user_timeline('username', count=10)

# Mostrar los tweets en Streamlit
for tweet in tweets:
    st.write(tweet.text)