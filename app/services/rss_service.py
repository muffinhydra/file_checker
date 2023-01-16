
import feedparser

def get_feed():
    news_feed = feedparser.parse("http://feeds.feedburner.com/TheHackersNews")
    feed_list = []
    for entry in news_feed.entries:
        feed_list.append({
            "title": entry["title"],
            "summary": entry["summary"],
            "link": entry["link"],
            "picture": entry["links"][1]["href"],
            "date" : entry["published"],
            "author" : entry["author"]
        })
    return feed_list


if __name__ == "__main__":
    print(get_feed()[0])
    pass
    