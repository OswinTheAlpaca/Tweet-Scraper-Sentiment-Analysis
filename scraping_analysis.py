# -*- coding: utf-8 -*-

import tweet_scraping_engOnly
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import numpy as np
import pandas as pd


class SentimentData(object):
    
    def __init__(self, tweet_df):
        self.tweet_df = tweet_df()
    
    def __str__(self):
        sd = SentimentData(self)
        print(sd)
        
    def sentiment_percent(self, tweet_df ):
        
        df = pd.DataFrame(tweet_scraping_engOnly.csv_writer)
        
        ### analyze overall percentage of positive tweets
        def pos(self):
            df.value_counts(normalize='Positive')
        
        ### analyze overall percentage of neutral tweets
        def neut(self):
            df.value_counts(normalize='Neutral')
        
        ### analyze overall percentage of negative tweets
        def neg(self):
            df.value_counts(normalize='Negative')

    

# data visualization of scraping and sentiment analysis results. 
# types of visualization inspired by tutorial from Youtube Computer Science channel (https://www.youtube.com/watch?v=ujId4ipkBio)
class SentimentViz(object):
    
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame
    
    def __str__(self):
        sv = SentimentViz(self)
        print(sv)
        
    ## generate the report in pdf format (use name of the csv file) [MOVE TO MAIN!!!!]
    def gen_report(self): 
        pass
    
    ## sentiment results in bar chart
    ## code inspired by Saral Gyaan's tutorial (https://www.youtube.com/watch?v=AR2bLFXycf4)
    def bar_chart(self):
        
        ### initialize x-axis values
        x = ['Positive', 'Neutral', 'Negative']
        
        ### initialize y-axis values according to sentiment analysis results calculated by SentimentData class methods
        y = [SentimentData.sentiment_percent.pos(), SentimentData.sentiment_percent.neut(), SentimentData.sentiment_percent.neg()]
        
        ### define pyplot style sheet used for chart
        plt.style.use('ggplot')
        
        ### define layout parameters for the chart
        plt.bar(x, y, width=1.6, bottom=None, align='center', data=None)
        
        ### define label for x-axis
        plt.xlabel('Tweets Sentiment')
        
        ### define label for y-axis
        plt.ylabel('Share Percentage')
        
        ### define title for the chart
        plt.title('Sentiment Analysis Results')
        
        ### make chart appear in pop-up window
        plt.show()
        
    ## sentiment results in pie chart
    def pie_chart(self):
        sentimentPie = np.array([SentimentData.sentiment_percent.pos(), SentimentData.sentiment_percent.neut(), SentimentData.sentiment_percent.neg()])
        pieFields = ['Positive', 'Neutral', 'Negative']
        plt.pie(sentimentPie, labels=pieFields)
        
    ## polarity and subjectivity in plot chart 
    def scatterplot_chart(self):
        
        ### initialize x-axis data to reflect tweet subjectivity taken out of csv file 
        x = SentimentData.tweet_subjectivity()
        
        ### initialize y-axis data to reflect tweet polarity taken out of csv file
        y = SentimentData.tweet_polarity()
        
        ### initialize dictionnary for color parameter -- color changes depending on sentiment result
        sentimentColor = dict({'Positive': 'green', 
                               'Negative': 'red', 
                               'Neutral': 'bleue'})
        
        ### define scatter plot parameters [INCOMPLETE]
        plt.scatter(x, y, c=sentimentColor)
        
        plt.show()
        
    ## write word cloud from tweet_text collumn of csv file
    ## with the help of Parul Rajput's wordcloud tutorial (https://www.analyticsvidhya.com/blog/2021/08/creating-customized-word-cloud-in-python/)
    def word_cloud(self):
        
        ### initialize stopword set -- common link words words (prepositions, etc.) will be ignored
        stopwords = set(STOPWORDS)
        
        ### initialze word cloud mask image variable -- the word cloud will take the shape of that image (twitter bird)
        mask = np.array(Image.open("twitter_image.png"))
        
        ### set the parameters for the word cloud
        wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=1000, mask=mask)
        
        ### create wordloud in twitter
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        
        ### store to file
        plt.savefig("twitter_image.png", format="png")
        
        ### make wordcloud appear in popup window
        plt.show()
    

