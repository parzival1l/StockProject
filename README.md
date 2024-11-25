# Stock Market Analytics Dashboard

## Overview
This application is a real-time stock market analytics dashboard that combines Flask, FastAPI, and yfinance to provide interactive stock data visualization and news updates. Users can analyze stock prices with customizable time periods, detailed market insights, and relevant news articles.

## Features
- **Real-time Stock Data**: Fetch current and historical stock data using yfinance
- **Interactive Visualization**:
  - Line chart with markers for price points
  - Candlestick chart (toggleable)
  - Range slider for time period navigation
  - High/Low markers with visual indicators
  - Hover tooltips with detailed price information
  - Open/Close price annotations

- **Time Period Filters**:
  - Last Day (1-minute intervals)
  - 1 Week
  - 1 Month
  - 3 Months

- **Key Statistics**:
  - Minimum and Maximum values
  - Price change percentage
  - Last Open/Close prices
  - Day High/Low indicators

- **News Integration**:
  - Latest news articles related to the selected stock
  - Sentiment analysis for each article
  - Direct links to full news articles
  - News source and publication time
  - Top 5 most relevant articles displayed

## Technology Stack
- **Backend**:
  - Flask: Web application framework
  - FastAPI: Modern API framework with automatic Swagger documentation
  - yfinance: Yahoo Finance API wrapper
  - pandas: Data manipulation and analysis
  - Alpha Vantage API: Real-time news and sentiment analysis

- **Frontend**:
  - Plotly.js: Interactive charts
  - jQuery: AJAX requests
  - HTML5/CSS3: Responsive design

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Alpha Vantage API key (free tier available)

### Setup
1. Clone the repository
2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your Alpha Vantage API key:
   - Create a `.env` file in the root directory
   - Add your API key: `ALPHA_VANTAGE_API_KEY=your_api_key_here`

## Usage

1. Start the application:
```bash
python -m uvicorn app.main:api_app --reload
```

2. Access the dashboard:
- Open your web browser and navigate to `http://localhost:8000`
- The FastAPI documentation is available at `http://localhost:8000/docs`

3. Using the Dashboard:
- Enter a valid stock symbol (e.g., AAPL, GOOGL, MSFT) in the search box
- Select your preferred time period from the dropdown menu
- View the interactive price chart and statistics
- Scroll down to see related news articles and sentiment analysis

## Interpreting the Data

### Price Chart
- Green markers indicate price increases
- Red markers indicate price decreases
- The range slider shows the full time period available
- Dotted lines indicate the day's high and low prices

### Statistics Panel
- "Change %" shows the percentage change over the selected period
- "Day Range" displays the current day's price range
- "Period High/Low" shows the extreme values for the selected time frame

### News Section
- Each news card shows:
  - Article title and summary
  - Source and publication time
  - Sentiment indicator (positive/negative/neutral)
  - Click on the title to read the full article
- Color-coded sentiment indicators:
  - Green: Positive sentiment
  - Red: Negative sentiment
  - Gray: Neutral sentiment

## Troubleshooting

- Ensure all dependencies are correctly installed
- Check that port 8000 is not in use by other applications
- Verify your internet connection for real-time data updates
- Confirm your Alpha Vantage API key is correctly set in the .env file
- Some stock symbols might not be available through Yahoo Finance
- Alpha Vantage API has rate limits on the free tier

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- [yfinance](https://github.com/ranaroussi/yfinance) for stock market data
- [Alpha Vantage](https://www.alphavantage.co/) for news and sentiment analysis
- [Plotly](https://plotly.com/javascript/) for interactive visualization
- [FastAPI](https://fastapi.tiangolo.com/) and [Flask](https://flask.palletsprojects.com/) frameworks