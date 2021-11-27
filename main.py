import streamlit as st
from multipage import save, MultiPage, start_app, clear_cache
import pandas as pd
# from src.page.hranalytics import hranalytics
# from src.page.hranalyticsgraph import hranalyticsgraph
# from src.page.model import model
from PIL import Image
import os

def main():
    st.set_page_config(page_title="Stress Analytics", page_icon="📊", layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
        }
    )
    start_app()

    logs = pd.read_csv("./res/logs.csv")
    st.dataframe(logs.tail(10))
if __name__ == "__main__":
    main()