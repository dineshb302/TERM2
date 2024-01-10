#!/usr/bin/env python
import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title= "Stock Sentiment Analysis Honour5", layout="wide")
## Load the dataset

def load_data():
    file_data = pd.read_csv("stock_predict_data.csv",encoding = "ISO-8859-1")
    return file_data

def get_prediction(stock):
#   Stock_predict.write("Fetching the prediction for ", Stock)
    stock_predict_data = load_data()
    pred_result = stock_predict_data['result']
    result=[]
    for p in pred_result:
        if p == 1:
            result.append("Up")
        else:
            result.append("Down")
    stock_predict_data['Result'] = result
    pred_data = stock_predict_data[stock_predict_data['symbol']==stock]
    pred_data_df = pred_data.get(['symbol', 'description', 'date', 'source.name'])
    pred_data_df.columns = ['Stock Name','News Headline','Date','Source']

## Container for Stock prediction  
    Stock_predict.subheader("Prediction for Stock:")
    write = "The Stock will go " + pred_data['Result']
    Stock_predict.write(write)
    Stock_news.subheader('Prediction is based on the following News headlines:')
    Stock_news.dataframe(pred_data_df)

    
## Sidebar with Team info
st.sidebar.title("Honour5 members:")
st.sidebar.write("Dinesh Bhatotia, 12310035")
st.sidebar.write("Pushan Kumar Banerjee, 12310015")
st.sidebar.write("Sigireddy Sithal, 12310002")
st.sidebar.write("Sudhakar Jagdale, 12310054")
st.sidebar.write("Vanama Venkata Sri Harsha Sai, 12310038")

## Header Section - Intro
Header = st.container()
Header.subheader("Stock Sentiment Analysis Honour5")
Header.write("Hi,")
Header.write("Honour5 presents stock prediction based on the sentiment of news headlines")

## Container for Stock input
Stock_input = st.container()
stock_predict_data = load_data()
stocks_list = stock_predict_data['symbol'].unique()

Stock = Stock_input.selectbox("Please choose a stock: ",
                              stocks_list, index=None,
                              placeholder="Select a stock...")
#Stock_input.write("Selected stock is ", Stock)
Stock_predict = st.empty()
Stock_news = st.empty()
# Button to get prediction from file
if Stock_input.button("Get Prediction"):
    get_prediction(Stock)

