import tweepy
import csv
import pandas as pd
import re

RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

def strip_emoji(text):
    return RE_EMOJI.sub(r'', text)

print(strip_emoji('@achilorstuv WKWKWKKWWK KOK BISA SPAGHETTI ADA KRIUKNYA SARAH üò≠🤔'))

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

MAX_TWEETS = 10
search_keyword = input("search keyword? ")
print("searching: '" + search_keyword + "'\n")

# tweets = tweepy.Cursor(api.search,
#                        q=search_keyword,
#                        lang="en",
#                        since="2021-04-04").items(1)

# for tweet in tweets:
#     print('$' + tweet.text + '\n\n')


csvFile = open(search_keyword+'.csv', 'a+', newline='', encoding="utf-8")

csvWriter = csv.writer(csvFile)
search_limit = 10

created = []
id_twitter = []
username = []
text = []

for tweet in tweepy.Cursor(api.search, q=search_keyword, count=100, lang='id', result_type="latest").items(search_limit):
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
