# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:32:46 2018

@author: zhang
"""
import tweepy
import time
from settings import TWITTER
from collections import namedtuple
from chatterbot import ChatBot

auth = tweepy.OAuthHandler("UVl2MyzWaCjGxuQ8MH0gJNmKr", "URWYHO5hq6SWpYe7Y3l1pt6wyznAt6OPGkCytmuNO5H6e28v9D")
auth.set_access_token("983813133075656704-ljsIqyAKO3t6KF42WeLj8YEDpG3c2U3", "vxucZLRKp9hTzZvLTV8LW7w407bdCdxWzgqKagnnboWEd")

api = tweepy.API(auth)

#public_tweets = api.statuses_lookup([983814669663170560])


#for tweet in public_tweets:
 #   print(tweet.text)
print("1")
# Train based on the english corpus
'''chatbot.train("chatterbot.corpus.english")

# Train based on english greetings corpus
chatbot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
chatbot.train("chatterbot.corpus.english.conversations")
'''
'''
chatbot = ChatBot(
    "TwitterBot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="./twitter-database.db",
    twitter_consumer_key=TWITTER["CONSUMER_KEY"],
    twitter_consumer_secret=TWITTER["CONSUMER_SECRET"],
    twitter_access_token_key=TWITTER["ACCESS_TOKEN"],
    twitter_access_token_secret=TWITTER["ACCESS_TOKEN_SECRET"],
    trainer="chatterbot.trainers.TwitterTrainer"
)'''

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    filters=["chatterbot.filters.RepetitiveResponseFilter"]
)




#print(public_tweets[0])

# Train based on the english corpus
#chatbot.train("chatterbot.corpus.english")

# Get a response to an input statement
print("Here rrr")
trendIndex = int(input("What is the trendIndex "))
trends = api.trends_place(2358820)
data = trends[0]
getTrends = data["trends"]
names = [trend["name"] for trend in getTrends]
print(names)


message = ""
print("go into loop")
notDuplicated = True
tweet = api.user_timeline(id = '983814669663170560', count = 1)[0]
lastTweet = ""
while 1:
    
    
#tweet = api.user_timeline(id = '983813133075656704', count = 1)[0]
    if notDuplicated :
        print("It's not duplicated")
        tweet = api.user_timeline(id = '983814669663170560', count = 1)[0]
        print("The last tweet is ",tweet.text)
        print("Your response is ", chatbot.get_response(tweet.text))
        message = chatbot.get_response(tweet.text)
        lastTweet = tweet.text
        
    else :
        
        message = names[trendIndex] +" good or bad?"
        trendIndex = trendIndex +1
        print("The trend is ", message)
        notDuplicated = True
    try:
        print("Your tweet is ", (message))
        api.update_status((message))
    except tweepy.TweepError:
            print("Duplicated")
            notDuplicated = False     
    time.sleep(40)
    
    print("one loop end")

#x = json.loads(api.trends_available(), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
#print(api.trends_available())

#print(api.trends_closest())
    #followers = api.followers()
#nameList = []
#print(followers)
#print(len(followers))
#print (api.get_status("983814669663170560"))

'''
for i in range (0,len(followers)):
    if followers[i]==""
'''













