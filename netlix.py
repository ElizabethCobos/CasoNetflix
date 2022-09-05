import streamlit as st
import pandas as pd
import codecs

st.title ("Netflix App")


@st.cache
def load_data(nrows):
    doc=codecs.open("movies.csv","rU","latin1")
    data = pd.read_csv (doc, nrows=nrows)
    lowercase = lambda x:str(x).lower()
    return data

data_load_state = st.text("Loading data...")
data = load_data(500)
data_load_state.text("Done! (using st.cache)")

st.dataframe(data)