import streamlit as st
import pandas as pd
import yfinance as yf


st.title("Stock Market App")
# streamlit run .\stock_market.py 
st.write("This is working.")

ticker_symbol = st.text_input("Enter stock ticker symbol", "AAPL")
ticker_data =yf.Ticker(ticker_symbol)

# hist = ticker_data.history(start="2022-05-31",end="2022-07-20")

starting_date = st.date_input("Enter the starting date", value=pd.to_datetime("2021-01-01"))
ending_date = st.date_input("Enter the ending date", value=pd.to_datetime("today"))


hist = ticker_data.history(start=starting_date, end=ending_date)

st.write(hist)
#st.dataframe(hist) for handling large dataset

col1, col2 = st.columns(2)

with col1:
    st.write("This is working Volume")
    st.line_chart(hist.Volume)

with col2:
    st.write("This is working Close")
    st.line_chart(hist.Close)