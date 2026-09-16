import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Password Strength Analyzer", layout="wide")
st.title("Password Strength Analyzer")
st.caption("Responsive browser demo: all analysis runs client-side in your browser.")

# Read analyze.html shipped in the repo root
html_path = Path(__file__).resolve().parent / "analyze.html"
if not html_path.exists():
    st.error(f"Unable to load interface: {html_path.name} was not found next to app.py.")
    st.stop()

html = html_path.read_text(encoding="utf-8")

# Render the page inside Streamlit with a roomy viewport so content isn't clipped on larger/smaller displays.
components.html(html, height=1500, scrolling=True)
