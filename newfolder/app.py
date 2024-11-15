from flask import Flask, jsonify, render_template
import praw
from textblob import TextBlob
import pandas as pd
import datetime

app = Flask(__name__)

# Reddit API credentials
reddit = praw.Reddit(
    client_id="I3UifirACiBH1ZbDtDRj_Q",
    client_secret="HQ3tMcfhyB6d296JO7ex0F-DY-y7lg",
    user_agent="crypto forecasting for the project",
    redirect_uri="http://localhost:8080"
)

def fetch_reddit_sentiment():
    # Use subreddit of interest
    subreddit = reddit.subreddit("cryptocurrency")
    # Fetch recent posts
    posts = subreddit.hot(limit=150)  # Adjust limit as needed
    sentiment_data = []
    
    for post in posts:
        analysis = TextBlob(post.title)  # Analyze the sentiment of the post title
        sentiment_score = analysis.sentiment.polarity
        sentiment_data.append({
            "title": post.title,
            "score": sentiment_score,
            "created": datetime.datetime.fromtimestamp(post.created_utc)
        })
    
    # Convert to DataFrame and sort by date
    df = pd.DataFrame(sentiment_data)
    df = df.sort_values(by="created")  # Sort by date
    return df

# Flask route to get data for charting
@app.route('/data', methods=['GET'])
def get_data():
    sentiment_df = fetch_reddit_sentiment()
    
    # Create price data using the sentiment scores and align with dates
    price_data = {
        "dates": list(sentiment_df['created'].astype(str)),  # Convert timestamps to strings for JSON
        "prices": [500 + score * 100 for score in sentiment_df['score']]  # Sample transformation for price
    }
    
    # Log the data for verification (optional)
    print("Sentiment DataFrame:", sentiment_df)
    print("price_data:", price_data)
    
    # Send both sentiment and price data as JSON
    return jsonify({
        "sentiment": sentiment_df.to_dict(orient="list"),
        "prices": price_data
    })

# Render the homepage
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
