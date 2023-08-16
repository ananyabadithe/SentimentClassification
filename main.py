# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

import tweepy

from data.raw_data.tweets_collection import user_tweets

consumer_key = "u8vd4U48YXaxhH0kCuchz4zHf"
consumer_secret = "6nIwV04jjjC9HuZbb8K68pdgv8gPdTs9mcGeXPjIK769HLFHcs"
access_token = "1690123664211992577-myuS0VAQYXNNVXjuoh9XW5Botq5YOp"
access_token_secret = "Ad0vS0IxdKNyv5pPFFaF9c2L2gbLUjrpVlBZj2GstPpY5"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

user_post = api.
for tweet in user_tweets:
    print(tweet.text)
