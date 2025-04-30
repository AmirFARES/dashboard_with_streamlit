import streamlit as st

# Set page configuration
st.set_page_config(page_title="Looker Studio Embed", layout="centered")

# Title of the app
st.title("Looker Studio Dashboard")

# Embed Looker Studio report using raw HTML
looker_embed_html = """
<iframe width="1400" height="1000" 
src="https://lookerstudio.google.com/embed/reporting/e1d9de8a-5c36-4581-8c8b-1060893902f9/page/h0zdE" 
frameborder="0" style="border:0" allowfullscreen 
sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
</iframe>
"""

st.markdown(looker_embed_html, unsafe_allow_html=True)
