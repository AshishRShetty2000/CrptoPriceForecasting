Project Overview
This project contains two main components:

Frontend: A Flask-based web interface for data visualization.
Backend: A Python backend that integrates with Reddit's API using PRAW to fetch and analyze sentiment data.

Project Structure
plaintext
Copy code
root/
|-- templates/         # HTML templates for the Flask app
|-- static/            # Static files (CSS, JavaScript)
|-- app.py             # Main Flask application file
|-- requirements.txt   # Python dependencies

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
