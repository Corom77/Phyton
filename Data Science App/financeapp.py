import yfinance as yf
import streamlit as st
st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Cac40!
""")
tickerSymbol = '^FCHI'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
