# Stock Market Analytics Dashboard

## Overview
This application is a real-time stock market analytics dashboard that combines Flask, FastAPI, and yfinance to provide interactive stock data visualization. Users can analyze stock prices with customizable time periods and detailed market insights.

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

## Technology Stack
- **Backend**:
  - Flask: Web application framework
  - FastAPI: Modern API framework with automatic Swagger documentation
  - yfinance: Yahoo Finance API wrapper
  - pandas: Data manipulation and analysis

- **Frontend**:
  - Plotly.js: Interactive charts
  - jQuery: AJAX requests
  - HTML5/CSS3: Responsive design

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup
1. Clone the repository:
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
- Toggle between line and candlestick views using the chart type selector
- Use the range slider below the chart to zoom into specific time periods
- Hover over data points to view detailed price information

## Interpreting the Data

- **Price Chart**:
  - Green markers indicate price increases
  - Red markers indicate price decreases
  - The range slider shows the full time period available
  - Dotted lines indicate the day's high and low prices

- **Statistics Panel**:
  - "Change %" shows the percentage change over the selected period
  - "Day Range" displays the current day's price range
  - "Period High/Low" shows the extreme values for the selected time frame

## Troubleshooting

- Ensure all dependencies are correctly installed
- Check that ports 8000 are not in use by other applications
- Verify your internet connection for real-time data updates
- Some stock symbols might not be available through Yahoo Finance

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.