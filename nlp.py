import tweepy
from textblob import TextBlob

consumer_key='h8EtOsMnbgrfSCvC0OLRR43ev'
consumer_secret='KIBEiv82WhwmxLj2ol8EmIu2zlY30GHrJFRJM3BmlcpkYeyhYE'

access_token='146830814-yXTFynWk5h5WpUwiCR0qQthDJzn1WV5PeQXML0Mc'
access_token_secret='dpRFnZ6XDQlKoblCLW16teZDOaHMtqustEzufBONlYZnn'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets = api.search('trump') #replace with what you wart to search

for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)


#polarity measures how postitive or negative the text is
#and subjectivity measures how much of an opinion it is versus how factual it is


#1. Sentiment Analysis - Understanding and Extracting Feelings from data
#2. An API acts as a gateway that lets you access an apps functionality from your code
#3. TextBlob is awesome for NLP tasks
#use AlchemyLanguage by Watson Laboratory for better analysis.
#user can access questions like  how to monitor social media to , and how can I use business intelligence to create dashboards and charts
