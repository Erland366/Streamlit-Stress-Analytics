import streamlit as st
from multipage import save, MultiPage, start_app, clear_cache
from src.page.hranalytics import hranalytics
from src.page.hranalyticsgraph import hranalyticsgraph
from src.page.model import model
from PIL import Image
import os


#Nyobain push kedua
print("Hello world")
def main():
    st.set_page_config(page_title="HR Analytics", page_icon="📊", layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
        }
    )

    start_app()
if __name__ == "__main__":
    main()