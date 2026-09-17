import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Password Analyzer",
    page_icon="logo.svg", # This tells Streamlit to use your SVG file
    layout="wide"
)
st.set_page_config(page_title="Password Strength Analyzer", layout="wide")
st.title("Password Strength Analyzer")
st.caption("Responsive browser demo: all analysis runs client-side in your browser.")

# Read analyze.html shipped in the repo root
html_path = Path(__file__).resolve().parent / "analyze.html"
if not html_path.exists():
    st.error(f"Unable to load interface: {html_path.name} was not found next to app.py.")
    st.stop()

html = html_path.read_text(encoding="utf-8")

# height is just an initial fallback before analyze.html's own resize script runs
# (see the "Streamlit iframe auto-height" block at the bottom of analyze.html's <script>).
# scrolling=False so the page grows/shrinks with real content instead of showing a
# fixed-height box with its own internal scrollbar - that nested-scrollbar look is what
# was causing the cramped mobile view.
components.html(html, height=1000, scrolling=False)
