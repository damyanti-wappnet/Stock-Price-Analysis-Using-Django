# install yfinance package to get real time stock data
import yfinance as yf
from django.shortcuts import render

#import express library from plotly module for data visualization
import plotly.express as px

#import pandas library for Data Manupalation
import pandas as pd

# import plotly.graph_objects to create plotly objects that can be used to render charts
import plotly.graph_objects as go

def index(request):
    #Will load Apple Stock data on first website visit 
    stock_data = yf.download('AAPL', start="2020-01-01", end="2022-12-31")

    #variable created to pass in context for dropdown select value
    selected_data = ""

    if request.method == "POST":
        if request.POST["search"]:
            #variable created to display selected data that can be used to render the charts
            stock_data = yf.download(request.POST["drop_xc"].split('-')[0], start="2020-01-01", end="2022-12-31")
            selected_data = f'of {request.POST["drop_xc"].split("-")[1]}' 
            print(request.POST["drop_xc"])
    
    
    
    fig = px.line(stock_data, x = stock_data.index, y = 'Close', title = 'Close price Analysis with Time Period ')
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"), 
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
    fig1 = px.bar(stock_data, x = stock_data.index, y = 'Close', title = f'Close price Analysis with Time Period {selected_data}')
    fig1.update_xaxes(rangeslider_visible=True)
    fig1.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"), 
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

    fig2 = go.Figure(data=[go.Candlestick(x=stock_data.index,open=stock_data['Open'],high=stock_data['High'],low=stock_data['Low'],close=stock_data['Close'])])
    fig2.update_xaxes(rangeslider_visible=True)
    fig2.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
    fig2.update_layout(
    title = 'Close price Analysis with Time Period ',
    yaxis_title = 'Close Price',
    xaxis_title = 'Date'
)

    # Render the graph in the template
    context = {
        'line_graph': fig.to_html(full_html=False),
        'bar_graph': fig1.to_html(full_html=False),
        'candlestick_graph': fig2.to_html(full_html=False),
        'selected': selected_data
    }
    return render(request, 'index.html', context)