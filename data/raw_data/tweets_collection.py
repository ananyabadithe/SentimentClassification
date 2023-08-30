# import tweepy
#
# consumer_key = "u8vd4U48YXaxhH0kCuchz4zHf"
# consumer_secret = "6nIwV04jjjC9HuZbb8K68pdgv8gPdTs9mcGeXPjIK769HLFHcs"
# access_token = "1690123664211992577-myuS0VAQYXNNVXjuoh9XW5Botq5YOp"
# access_token_secret = "Ad0vS0IxdKNyv5pPFFaF9c2L2gbLUjrpVlBZj2GstPpY5"
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
#
# api = tweepy.API(auth)
#
# user_tweets = api.user_timeline(screen_name='twitterusername', count=10)
# for tweet in user_tweets:
#     print(tweet.text)
