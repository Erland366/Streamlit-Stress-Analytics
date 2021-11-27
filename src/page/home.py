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
    st.text("2. Muhammad Furqony Sabillilhaq")
    st.image(Image.open("res/screencapture_kaggle.png"))

    save([start_index], "placeholder1", ["App2", "App3"])