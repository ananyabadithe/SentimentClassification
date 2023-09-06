import feedparser
from textblob import TextBlob

# Parse the BBC World News RSS Feed
rss_url = "http://feeds.bbci.co.uk/news/world/rss.xml"
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    print("Title:", entry.title)
    print("Link:", entry.link)
    print("Description:", entry.description)

    analysis = TextBlob(entry.title)
    sentiment = "Neutral"
    if analysis.sentiment.polarity > 0:
        sentiment = "Positive"
    elif analysis.sentiment.polarity < 0:
        sentiment = "Negative"

    print("Sentiment:", sentiment)
    print("----------")