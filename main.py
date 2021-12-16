import streamlit as st
import pandas as pd
from functions import *
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



st.set_page_config(page_title='NLP with oil and renewable energy articles',
                   layout="wide")

st.sidebar.image('images/oilprice-logo.png', width=300)
st.sidebar.image('images/Spiced_Logo_2.png', width=300)
st.sidebar.header('NLP with oil and renewable energy articles')
st.sidebar.markdown('**Spiced Data Science bootcamp final project**. _Browse the menu below for options:_')


menu = st.sidebar.selectbox(
    "",
    ("Introduction", "Data", "Sentiment Analysis", "Modelling", "Network analysis"),
)

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.markdown('---')
st.sidebar.write('Francisco Ebeling | December 2021 ebelingbarros@gmail.com https://www.github.com/ebelingbarros/')

if menu == 'Introduction':
    set_home()
elif menu == 'Data':
    data()
elif menu == 'Sentiment Analysis':
    sentiment_analysis()
elif menu == 'Modelling':
    modelling()
elif menu == 'Network analysis':
    network()
