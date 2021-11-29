import streamlit as st
import os
import pandas as pd
import io
import time
from PIL import Image
from multipage import save, MultiPage, start_app, clear_cache

def home(prev_vars=0):
    if prev_vars != None:
        start_index = prev_vars
    else:
        start_index = 1 

    st.title("Pengantar Sains Data Kelompok 8")
    st.header("Nama Anggota Kelompok")
    st.text("1. Erland Hilman Fuadi (195150200111045)")
    st.text("2. Muhammad Furqony Sabillilhaq (195150200111085)")
    with st.expander("Introduction"):
        st.markdown("The Taylor Manifest Anxiety Scale was first developed in 1953 to identify individuals who would be good subjects for studies of stress and other related psychological phenomenon. Since then it has been used as a measure of anxiety as general personality trait. Anxiety is a complex psychological construct that includes a multiple of different facets related to extensive worrying that may impair normal functioning. The test has been widely studied and used in research however there are some concerns that it does not measure a single trait but instead measures a basket of loosely related ones and so the score is not that meaningful")
    with st.expander("Procedure"):
        st.markdown("The test consists of fifty statements about you. You must rate each one as true or false. It should take most people four to ten minutes to complete.")
    
    with st.expander(label="Kaggle Picture"):
        st.image(Image.open("res/screencapture_kaggle.png"))
    
    save([start_index], "placeholder1", ["App2", "App3"])