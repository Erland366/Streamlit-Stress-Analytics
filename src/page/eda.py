import streamlit as st
import os
import pandas as pd
import io
import time
from PIL import Image
from multipage import save, MultiPage, start_app, clear_cache
import joblib

def eda(prev_vars):
    if prev_vars != None:
        start_index = prev_vars
    else:
        start_index = 1 

    st.title("Exploratory Data Analysis")
    st.text("We're gonna do some EDA to our data")
    data = load_data("./res/data.csv", delimiter=r"\t")
    with st.spinner("Wait for data to load"):
        with st.container():
            st.header("Take a look at top 10 data")
            st.dataframe(data.head(10))
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                with st.expander("See data info"):
                    data_info = pd.concat([pd.DataFrame(data.dtypes), data.count()], axis=1).set_axis(
                        ['dtypes', 'count'], axis="columns")
                    st.dataframe(data_info.astype('str'),
                                    width=1000, height=250)
            with col2:
                with st.expander("See data describe"):
                    st.dataframe(data.describe(), height=250)
        with st.container():
            with st.expander("See Value Counts Per Category"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    data_vc_str = joblib.load("./res/value_counts_str.pkl")
                    st.dataframe(data_vc_str, width=450)
                with col2:
                    data_vc_anx = joblib.load("./res/value_counts_anx.pkl")
                    st.dataframe(data_vc_anx, width=450)
                with col3:
                    data_vc_dep = joblib.load("./res/value_counts_dep.pkl")
                    st.dataframe(data_vc_dep, width=450)
    save([start_index], "placeholder1", ["App2", "App3"])

@st.cache
def load_data(url, header='infer', **kwargs):
    return pd.read_csv(url, header=header, **kwargs)