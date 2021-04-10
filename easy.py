import tweepy
import csv
import pandas as pd

API_KEY = "k1MxRDsdaOJxkAvk4hi1Udxro"
API_KEY_SECRET = "TKmTdCg50CS4TXLticIxMc5PVSkm9TsCdSqnCszPOjHuDR4c94"
ACCESS_TOKEN = "321365430-SEEjSZOGgLMsY9hPBdvEZEraQOzMrF5INAh6IzXH"
ACCESS_TOKEN_SECRET = "2B7Yc4fLk9rx2vEmKzrR1V0bXHQq49eUX361ESYebqmL3"

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
search_keyword = "bitcoin"
search_limit = 100
print("searching: '" + search_keyword +
      " (limit: " + str(search_limit) + ")'")

csvFile = open(search_keyword+'.csv', 'a+', newline='', encoding="utf-8")

csvWriter = csv.writer(csvFile)

created = []
id_twitter = []
username = []
text = []

for tweet in tweepy.Cursor(api.search, q=search_keyword, count=300, lang='id', result_type="latest",  fromDate="2020-01-01", tweet_mode="extended").items(search_limit):
    print(tweet.created_at,  tweet.id, tweet.user.name, tweet.text)
    created.append(tweet.created_at)
    id_twitter.append(tweet.id)
    username.append(tweet.user.name)
    text.append(tweet.text)
    tweets = [tweet.created_at, tweet.id,
              tweet.user.name, tweet.text]
    csvWriter.writerow(tweets)

dictTweets = {"timestamp": created, "id_twitter": id_twitter,
              "username": username, "text": text}

dataFrame = pd.DataFrame(dictTweets, columns=[
                         "timestamp", "id_twitter", "username", "text"])

dataFrame

openFile = open(search_keyword + ".csv", "r")
print(openFile.read())
