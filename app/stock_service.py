import yfinance as yf
import pandas as pd
from typing import Dict, Any
from datetime import datetime, timedelta
import pytz
import os
import requests

# Add this at the top of the file
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY', 'YOUR_API_KEY_HERE')

def test_yfinance():
    """
    Test function to verify yfinance is working correctly
    """
    try:
        # Test with Apple stock (AAPL) for a simple period
        stock = yf.Ticker("AAPL")
        # Get just 5 days of historical data
        hist = stock.history(period="5d")
        return not hist.empty
    except Exception as e:
        print(f"YFinance test failed: {str(e)}")
        return False

def get_stock_news(symbol: str) -> list:
    """
    Fetch news articles related to the stock symbol
    """
    try:
        url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
        response = requests.get(url)
        data = response.json()

        if "feed" not in data:
            return []

        # Get the top 5 news articles
        news_articles = []
        for article in data["feed"][:5]:
            news_articles.append({
                "title": article.get("title", ""),
                "summary": article.get("summary", ""),
                "url": article.get("url", ""),
                "source": article.get("source", ""),
                "time_published": article.get("time_published", ""),
                "sentiment": article.get("overall_sentiment_label", "neutral")
            })

        return news_articles
    except Exception as e:
        print(f"Error fetching news: {str(e)}")
        return []

def get_stock_data(symbol: str, period: str) -> Dict[str, Any]:
    """
    Fetch historical stock data using yfinance
    """
    try:
        end_date = datetime.now()

        if period == "1d":
            # For 1 day, get data with 1-minute intervals for the last trading day
            start_date = end_date - timedelta(days=1)
            stock = yf.Ticker(symbol)
            hist = stock.history(start=start_date, end=end_date, interval='1m')
        else:
            # For other periods, use daily data
            if period == "1wk":
                start_date = end_date - timedelta(days=7)
            elif period == "1mo":
                start_date = end_date - timedelta(days=30)
            elif period == "3mo":
                start_date = end_date - timedelta(days=90)
            else:
                start_date = end_date - timedelta(days=30)

            stock = yf.Ticker(symbol)
            hist = stock.history(start=start_date, end=end_date)

        # Handle empty data
        if hist.empty:
            return {"error": f"No historical data found for symbol {symbol}"}

        # Format datetime index properly
        if period == "1d":
            # For intraday data, keep time information
            hist.index = hist.index.tz_convert('America/New_York')
            date_strings = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in hist.index]
        else:
            # For daily data, use date only
            hist.index = hist.index.date
            date_strings = [str(date) for date in hist.index]

        response_data = {
            "dates": date_strings,
            "open": [float(val) for val in hist['Open'].tolist()],
            "close": [float(val) for val in hist['Close'].tolist()],
            "high": [float(val) for val in hist['High'].tolist()],
            "low": [float(val) for val in hist['Low'].tolist()],
            "volume": [int(val) for val in hist['Volume'].tolist()],
            "symbol": symbol,
            "period": period
        }

        if not hist.empty:
            response_data.update({
                "last_open": float(hist['Open'].iloc[-1]),
                "last_close": float(hist['Close'].iloc[-1]),
                "day_high": float(hist['High'].max()),
                "day_low": float(hist['Low'].min())
            })

        # Add news data to the response
        response_data["news"] = get_stock_news(symbol)

        return response_data

    except Exception as e:
        return {"error": f"Error fetching data: {str(e)}"}

# Test the functionality
if __name__ == "__main__":
    # Run test
    print("Testing YFinance package...")
    if test_yfinance():
        print("YFinance test passed!")
        # Try getting some actual data
        result = get_stock_data("AAPL", "1wk")
        if "error" not in result:
            print("Successfully retrieved AAPL data!")
            print(f"Number of data points: {len(result['dates'])}")
            print(f"Latest close price: {result['last_close']}")
        else:
            print(f"Error: {result['error']}")
    else:
        print("YFinance test failed!")