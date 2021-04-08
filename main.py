import tweepy
import csv
import pandas as pd
import re
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# using Regular Expression (re) to strip out the emojis
RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)


def strip_emoji(text):
    return RE_EMOJI.sub(r'', text)


# Authenticate to Twitter
auth = tweepy.OAuthHandler(
    "k1MxRDsdaOJxkAvk4hi1Udxro",
    "TKmTdCg50CS4TXLticIxMc5PVSkm9TsCdSqnCszPOjHuDR4c94")
    
auth.set_access_token("321365430-SEEjSZOGgLMsY9hPBdvEZEraQOzMrF5INAh6IzXH",
                      "2B7Yc4fLk9rx2vEmKzrR1V0bXHQq49eUX361ESYebqmL3")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Gather Input
search_keyword = input("search keyword? ")
search_limit = int(input("search limit amount? "))
print("searching: '" + search_keyword + " (limit: " + str(search_limit) + ") '\n")

csvFile = open(search_keyword+'.csv', 'a+', newline='', encoding="utf-8")

csvWriter = csv.writer(csvFile)


created = []
id_twitter = []
username = []
text = []

for tweet in tweepy.Cursor(api.search, q=search_keyword, count=300, lang='id', result_type="latest").items(search_limit):
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
