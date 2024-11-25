from fastapi import FastAPI, Query
from flask import Flask, render_template
from fastapi.middleware.wsgi import WSGIMiddleware
from .stock_service import get_stock_data
import uvicorn
import socket
import sys

def find_free_port(start_port=8000):
    """Find a free port starting from the given port number."""
    port = start_port
    while port < start_port + 100:  # Try 100 ports
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            port += 1
    raise RuntimeError('No free ports found')

# Initialize FastAPI and Flask apps
api_app = FastAPI(
    title="Stock Market Analytics",
    description="An API for fetching and analyzing stock market data",
    version="1.0.0"
)

flask_app = Flask(__name__)

# Flask routes
@flask_app.route('/')
def home():
    return render_template('index.html')

# FastAPI endpoints
@api_app.get("/api/stock-data/")
async def get_stock_info(
    symbol: str = Query(..., description="Stock symbol (e.g., AAPL)"),
    period: str = Query("1mo", description="Time period (1mo, 3mo, 1wk)")
):
    """
    Get stock data for a given symbol and time period.
    """
    return get_stock_data(symbol, period)

# Mount Flask app under FastAPI
api_app.mount("/", WSGIMiddleware(flask_app))

if __name__ == "__main__":
    try:
        # Find a free port
        port = find_free_port()
        print(f"Starting server on port {port}")
        uvicorn.run(api_app, host="0.0.0.0", port=port)
    except Exception as e:
        print(f"Error starting server: {e}", file=sys.stderr)
        sys.exit(1)