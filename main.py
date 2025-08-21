import streamlit as st
from pytz import country_names

from app import send_sms,financial_data_of_company,controller,message_creator
import pickle
import pandas as pd

Stocks = pd.read_pickle("Stocks.pkl")

st.title("StockPulse: Stock Data Alerts via WhatsApp")

# Input for a single company name
country = st.selectbox("Select Country", Stocks['Country'].unique())
exchange = st.selectbox("Select Exchange", Stocks[Stocks['Country']==country]['Exchange'].unique())
stock_name = st.selectbox("Stock Name", Stocks[Stocks['Exchange']==exchange]['Name'])
ticker = Stocks[Stocks['Name']==stock_name]['Ticker'].iloc[0]

# Input for phone number
phone_number = st.text_input("Enter your phone number:")

# When the user submits, validate and display the results
if st.button("Submit"):
    controller(phone_number, ticker)
    st.text("Message Sent")



