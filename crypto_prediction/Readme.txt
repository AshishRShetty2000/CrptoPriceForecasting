# Crypto Price and Reddit Sentiment Analysis

This project is a web application that visualizes the impact of Reddit sentiment on cryptocurrency prices. Using Python's Flask framework and the PRAW library, it fetches Reddit posts, analyzes sentiment using TextBlob, and displays the sentiment and price data on a dual-axis line chart with Chart.js.

Features
- Fetches data from the r/cryptocurrency subreddit.
- Analyzes sentiment of post titles.
- Displays Reddit sentiment and crypto prices on an interactive line chart.
- Allows users to see how sentiment correlates with crypto price trends over time.

Requirements:

- Python 3.6 or later
- [Flask](https://flask.palletsprojects.com/)
- [PRAW](https://praw.readthedocs.io/) - Python Reddit API Wrapper
- [TextBlob](https://textblob.readthedocs.io/) - For sentiment analysis
- [Chart.js](https://www.chartjs.org/) - For rendering charts in the frontend

For Reddit Api I have already added the secret key, client_id

Setup Instructions
1. Clone the Repository
git clone https://github.com/AshishRShetty2000/CrptoPriceForecasting.git

cd .\CrptoPriceForecasting\crypto_prediction\

2. Set Up a Virtual Environment (Recommended)

python -m venv venv

3. Activate the environment
On Windows

.\venv\Scripts\activate

4.Install npm node modules:

npm install

5. Install the Required Python Packages

Make sure you have all required libraries installed. You can install them using requirements.txt.

pip install -r requirements.txt

pip install Flask praw textblob pandas

6. Run the Flask Application

Start the Flask server using the command below:

python app.py

The application will be run.
