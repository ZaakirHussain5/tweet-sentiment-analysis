# Tweet Sentiment Analysis

## Overview

This project is a Flask web application that performs sentiment analysis on tweets related to a specific topic. The application uses the Tweepy library to interact with the Twitter API and the VADER (Valence Aware Dictionary and sEntiment Reasoner) tool from the NLTK library to analyze the sentiment of the tweets.

## Features

- Search for tweets containing a specific keyword or topic.
- Analyze the sentiment of the tweets, including positive, negative, and neutral scores.
- Display the results in a user-friendly web interface.

## Requirements

- Python 3.x
- Flask
- Flask-MySQLdb
- Tweepy
- Pandas
- NLTK

You can install the required Python packages using pip:

```bash
pip install Flask Flask-MySQLdb tweepy pandas nltk
```

## Setup

1. **Create a Twitter Developer Account:** To use the Twitter API, you'll need to have developer access. Obtain your `consumer_key`, `consumer_secret`, `access_token`, and `access_token_secret` from the Twitter Developer portal.

2. **Configure the Application:** Update the `tweetAnalysis` function in `app.py` with your Twitter API credentials:

   ```python
   consumer_key = 'YOUR_CONSUMER_KEY'
   consumer_secret = 'YOUR_CONSUMER_SECRET'
   access_token = 'YOUR_ACCESS_TOKEN'
   access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
   ```

3. **Run the Application:** Start the Flask development server by running:

   ```bash
   python app.py
   ```

4. **Access the Application:** Open your web browser and navigate to `http://127.0.0.1:5000/` to use the application.

## Usage

1. **Home Page:** Navigate to the home page to start using the application.

2. **Search for Tweets:** Enter a keyword or topic on the search page to find tweets related to it.

3. **View Analysis:** The application will display the sentiment analysis results, including positive, negative, and neutral scores, along with individual tweet details.

## File Structure

- `app.py`: The main Flask application script.
- `templates/`
  - `home_page.html`: The home page template.
  - `search.html`: The search page template.
  - `tweet.html`: The tweet analysis results template.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
