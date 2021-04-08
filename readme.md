# Streaming Tweets with Search Keyword

searches through a string, strips the emoji, and convert it to csv

## Authenticating

```
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
```

`consumer_key` adalah `API Key`, dan `consumer_secret` adalah `API key secret`

```
auth.set_access_token(key, secret)
```

`key` adalah `Access token` dan `secret` adalah `Access token secret` yang didapat di portal twitter API

## Stripping Down The Emoji

![original tweet](./assets/images/example-1-original-tweet.png)

The original tweet

![csv entry](./assets/images/example-1-csv.png)

Stripped out from its emoji in csv
