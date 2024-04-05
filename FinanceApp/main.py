import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

symbol = st.sidebar.text_input('Hisse Senedi', value='AVD')

st.title(symbol+ ' Hisse Senedi Grafigi')

start_date = st.sidebar.date_input('Starting Date', value=datetime(2020,1,1))
end_date = st.sidebar.date_input('Ending Date', value=datetime.now())

df = yf.download(symbol, start = start_date, end = end_date)

st.subheader('Hisse Senedi Fiyatlari')
st.line_chart(df['Close'])

st.subheader('Hisse Tablosu')
st.write(df)