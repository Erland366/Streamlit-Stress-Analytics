import streamlit as st
import os
import pandas as pd
import io
import time
from PIL import Image
from multipage import save, MultiPage, start_app, clear_cache

def logs(prev_vars):
    if prev_vars != None:
        start_index = prev_vars
    else:
        start_index = 1 
    logs = load_data("./res/logs.csv")
    st.header("Logs Our Training")
    st.text("How we did our training and parameters")
    st.dataframe(logs.tail(10))
    save([start_index], "placeholder1", ["App2", "App3"])

@st.cache
def load_data(url, header='infer', **kwargs):
    return pd.read_csv(url, header=header, **kwargs)