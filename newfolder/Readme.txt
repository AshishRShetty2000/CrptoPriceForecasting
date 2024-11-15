# Crypto Price and Reddit Sentiment Analysis

This project is a web application that visualizes the impact of Reddit sentiment on cryptocurrency prices. Using Python's Flask framework and the PRAW library, it fetches Reddit posts, analyzes sentiment using TextBlob, and displays the sentiment and price data on a dual-axis line chart with Chart.js.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Notes](#notes)

## Features
- Fetches data from the r/cryptocurrency subreddit.
- Analyzes sentiment of post titles.
- Displays Reddit sentiment and crypto prices on an interactive line chart.
- Allows users to see how sentiment correlates with crypto price trends over time.

## Requirements
- Python 3.6 or later
- [Flask](https://flask.palletsprojects.com/)
- [PRAW](https://praw.readthedocs.io/) - Python Reddit API Wrapper
- [TextBlob](https://textblob.readthedocs.io/) - For sentiment analysis
- [Chart.js](https://www.chartjs.org/) - For rendering charts in the frontend
Setup Instructions
1. Clone the Repository
```bash
git clone https://github.com/yourusername/crypto-forecasting.git
cd crypto-forecasting

2. Set Up a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install the Required Python Packages
Make sure you have all required libraries installed. You can install them using requirements.txt.
pip install -r requirements.txt
If you don't have a requirements.txt, install packages manually:
pip install Flask praw textblob pandas
5. Run the Flask Application
Start the Flask server using the command below:
python app.py
The application should be running at http://127.0.0.1:5000.

