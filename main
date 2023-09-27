import tweepy
from auth_file import AuthCredentials
import csv
import re
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import numpy as np
import pandas as pd

# Fetch authentication information from auth_file module
auth = tweepy.OAuthHandler(AuthCredentials.consumer_key, AuthCredentials.consumer_key_secret)
auth.set_access_token(AuthCredentials.access_token, AuthCredentials.access_token_secret)
api = tweepy.API(auth)

# Initialize keyword for tweet search
def enter_keyword():
    # Initialize prompt that asks the user to input a keyword for search and store the entered value
    keyword = input('Please enter your keyword: ')
    return keyword

class PrintTweets:
    def __init__(self, keyword):
        self.keyword = keyword

    # Perform tweet search and print output to a CSV file
    def print_search(self):
        # Initialize variable for public tweets mentioning the keyword fetched from the Tweepy API
        public_tweets = api.search(q=f"{self.keyword} -filter:retweets", lang='en')

        # Ask the user to input the name of the output file to be created
        filename = input('Please enter a name for the output file: ')

        # Create/open a CSV file to store scraped tweets
        with open(f'{filename}.csv', 'a+', encoding='utf-8', newline='') as scrape_output:
            # Initialize field names for the CSV file
            fieldnames = ['Tweet Text', 'Subjectivity', 'Polarity', 'Sentiment Analysis']
            csv_writer = csv.DictWriter(scrape_output, fieldnames=fieldnames)

            # Write field names in the CSV file if it's empty
            if scrape_output.tell() == 0:
                csv_writer.writeheader()

            for tweet in public_tweets:
                # Extract tweet text
                tweet_text = tweet.text

                # Clean the tweet text
                cleaned_tweet = CleanTweets(tweet_text).clean()

                # Analyze tweet sentiment
                sentiment = AnalyzeTweet(cleaned_tweet).analyze_sentiment()

                # Write data to the CSV file
                csv_writer.writerow({
                    'Tweet Text': cleaned_tweet,
                    'Subjectivity': sentiment['Subjectivity'],
                    'Polarity': sentiment['Polarity'],
                    'Sentiment Analysis': sentiment['Sentiment Analysis']
                })

class CleanTweets:
    def __init__(self, tweet):
        self.tweet = tweet

    # Clean the tweet text
    def clean(self):
        # Remove hashtags, mentions, and URLs from tweet text
        clean_tweet = re.sub("#[A-Za-z0-9]+", "", self.tweet)
        clean_tweet = re.sub("@[A-Za-z0-9]+", "", clean_tweet)
        clean_tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", clean_tweet)
        return clean_tweet

class AnalyzeTweet:
    def __init__(self, tweet):
        self.tweet = tweet

    # Analyze tweet sentiment
    def analyze_sentiment(self):
        analysis = TextBlob(self.tweet)
        sentiment = {
            'Subjectivity': analysis.sentiment.subjectivity,
            'Polarity': analysis.sentiment.polarity,
            'Sentiment Analysis': 'Positive' if analysis.sentiment.polarity > 0 else
                                  ('Neutral' if analysis.sentiment.polarity == 0 else 'Negative')
        }
        return sentiment

    def generate_word_cloud(self, filename):
        # Generate a word cloud from the cleaned tweet text
        stopwords = set(STOPWORDS)
        wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=1000, mask=None)
        wordcloud.generate(self.tweet)

        # Save the word cloud as an image
        wordcloud.to_file(filename)

        # Display the word cloud
        plt.figure(figsize=(8, 8), facecolor=None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)

        # Show the word cloud image
        plt.show()

if __name__ == "__main__":
    keyword = enter_keyword()
    tweets = api.search(q=f"{keyword} -filter:retweets", lang='en')
    
    for tweet in tweets:
        tweet_text = tweet.text
        cleaned_tweet = CleanTweets(tweet_text).clean()
        sentiment = AnalyzeTweet(cleaned_tweet).analyze_sentiment()
        
        print("Tweet Text:", cleaned_tweet)
        print("Sentiment Analysis Result:", sentiment)
        print()
