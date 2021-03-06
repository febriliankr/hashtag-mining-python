import tweepy
import csv
import pandas as pd
import re
from decouple import config

# using Regular Expression (re) to strip out the emojis
RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)


def strip_emoji(text):
    return RE_EMOJI.sub(r'', text)


API_KEY = config('API_KEY')
API_KEY_SECRET = config('API_KEY_SECRET')
ACCESS_TOKEN = config('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET')

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    print('\033[93m' + "[∙] Authenticating..." + '\033[0m')
    api.verify_credentials()
    print('\033[92m' + "[✔️] Authentication success!" + '\033[0m')
except:
    print("Error during authentication")

# Gather Input
search_keyword = 'FSM UKSW'  # input("Search keyword [type any string]: ")
search_limit = 25  # int(input("Search limit amount [type any number]: "))
print("searching: '" + search_keyword +
      " (limit: " + str(search_limit) + ")'")

csvFile = open(search_keyword+'.csv', 'a+', newline='', encoding="utf-8")

csvWriter = csv.writer(csvFile)

created = []
id_twitter = []
username = []
text = []

for tweet in tweepy.Cursor(api.search, q=search_keyword, count=300, lang='id', fromDate="2020-01-01", tweet_mode="extended").items(search_limit):
    print(tweet.created_at,  tweet.id, tweet.user.name, tweet.text)
    created.append(tweet.created_at)
    id_twitter.append(tweet.id)
    username.append(tweet.user.name)
    text.append(strip_emoji(tweet.text))
    tweets = [tweet.created_at, tweet.id,
              tweet.user.name, strip_emoji(tweet.text)]
    csvWriter.writerow(tweets)

dictTweets = {"timestamp": created, "id_twitter": id_twitter,
              "username": username, "text": text}

dataFrame = pd.DataFrame(dictTweets, columns=[
                         "timestamp", "id_twitter", "username", "text"])

dataFrame

openFile = open(search_keyword + ".csv", "r")
print(openFile.read())
