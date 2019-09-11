
#import VADER 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

 # function to print sentiments of feedback 
def sentiment_scores(article): 
  
    # Create a SentimentIntensityAnalyzer object. 
    analyzer = SentimentIntensityAnalyzer() 
  
    # polarity_scores method of SentimentIntensityAnalyzer 
    # oject gives a sentiment dictionary. 
    # which contains pos, neg, neu, and compound scores. 
    sentiment_dict = analyzer.polarity_scores(article) 
    return sentiment_dict