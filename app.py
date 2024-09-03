from flask import Flask, render_template, request,session ,redirect
from flask_mysqldb import MySQL
import tweepy
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app=Flask(__name__)
app.secret_key = "zdcxfxfvxcvcvcv25562521cvbcgb2152521cggcg215252"


@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/tweetAnalysis/<word>")
def tweetAnalysis(word):
    topic=word
    consumer_key = 'EvbddLEJv7nTQllXQVaEnmJKI'
    consumer_secret = 'BdBIPyyxU7CQ28KE1yrVbhOAZItQZcPHwR2hpVkO72W9bhQcR5'
    access_token = '1004710959053598721-qzKVNZidlPklP2UFtinItEP9DWRGjx'
    access_token_secret = 'G6aIF6ubRZhTZLDlSDsPVGrHBv8xpTNnSO3QgLe3e2Ir0'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    tweets = api.search(topic, count=200)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

    sid = SentimentIntensityAnalyzer()


    listy = [] 
    tweetsList=[]
    pcount,ncount,necount=0,0,0
    for index, row in data.iterrows():
        ss = sid.polarity_scores(row["Tweets"])
        twee={"text":tweets[index].text,"date":tweets[index].created_at,
        "pos_score":ss['pos']*100,"neg_score":ss['neg']*100,
        "neu_score":ss['neu']*100,"id":tweets[index].id}
        tweetsList.append(twee)
        pcount+=ss['pos']
        ncount+=ss['neg']
        necount+=ss['neu']
        listy.append(ss)

    
   
        

    return render_template("tweet.html",s=topic,p=pcount,n=ncount,ne=necount,tweets=tweetsList)


if __name__ == "__main__":
    app.debug=True
    app.run()