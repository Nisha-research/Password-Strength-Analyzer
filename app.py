import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Password Strength Analyzer", layout="centered")
st.title("Password Strength Analyzer")

# Read analyze.html shipped in the repo root
html_path = Path(__file__).parent / "analyze.html"
html = html_path.read_text(encoding="utf-8")

# Render the page inside Streamlit (adjust height as needed)
components.html(html, height=900, scrolling=True)
