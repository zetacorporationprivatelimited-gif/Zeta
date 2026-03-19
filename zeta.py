import streamlit as st
import streamlit.components.v1 as components

# This command forces the Streamlit page to use the full width of your browser
st.set_page_config(layout="wide")

# This CSS hides the padding at the top so your site starts right at the top
st.markdown("""
    <style>
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    </style>
    """, unsafe_allow_html=True)
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()
    # height=2500 ensures the full page is captured without a second scrollbar
    # width=None with use_container_width=True makes it fill the screen
    components.html(html_code, height=2500, scrolling=True)