import feedparser
import pandas as pd
RSS_URL = "http://dvd.netflix.com/Top100RSS"
feed = feedparser.parse(RSS_URL)
print(type(feed))
print(feed.keys())
print(type(feed.bozo))
print(type(feed['bozo']))
print(feed.version) # empty string, shouldn't be
print(feed.bozo)  # should be zero but is 1
if (feed.bozo == 0):
    print('Well-formed')
else:
    print('potential trouble ahead')
print(feed.feed.keys())
print(len(feed.entries)) #should be 100, is zero
df = pd.DataFrame(feed.entries)
