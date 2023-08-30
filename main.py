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

bearer_token = "YOUR_BEARER_TOKEN"

client = tweepy.Client(bearer_token)

query = "sunny"
max_results = 2

try:
    user_posts = client.search_recent_tweets(query=query, max_results=max_results)
    for post in user_posts:
        print(post.text)
except tweepy.errors.Forbidden as e:
    print("Error: Forbidden -", e)
except tweepy.TweepError as e:
    print("Error:", e)





