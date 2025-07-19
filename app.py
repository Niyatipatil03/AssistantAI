import streamlit as st
from ui import home, faq_chat, forms_guide, video_help

st.set_page_config(page_title="Clerk Assistant AI", layout="wide")

# Sidebar navigation
st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio("Go to", ("Home", "Chat Assistant", "Form Guide", "Video Help"))

# Page loader
if menu == "Home":
    home.render()
elif menu == "Chat Assistant":
    faq_chat.render()
elif menu == "Form Guide":
    forms_guide.render()
elif menu == "Video Help":
    video_help.render()
