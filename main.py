import feedparser, time

URL = "https://bitnaleeeee.github.io/feed.xml"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
## Enjoys solving problems and controlling flow with JavaScript

## Recent Post 

"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
