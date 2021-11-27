import streamlit as st
from multipage import save, MultiPage, start_app, clear_cache
import pandas as pd
from src.page.logs import logs
from src.page.eda import eda
# from src.page.hranalyticsgraph import hranalyticsgraph
# from src.page.model import model

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
    app = MultiPage()
    app.navbar_name = "Navigation"
    app.next_page_button = "Next Page"
    app.previous_page_button = "Previous Page"
    app.add_app("Log Training", logs)
    app.add_app("Exploratory Data Analysis", eda)
    app.run()

if __name__ == "__main__":
    main()