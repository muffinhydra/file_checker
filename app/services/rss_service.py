import feedparser

def get_feed():
    """
    Retrieve RSS feed from the specified url and parse the entries into a list of dictionaries.

    The function uses the feedparser library to parse the RSS feed from the specified url. It then creates a list of dictionaries, each representing an entry in the RSS feed. The dictionaries contain the title, summary, link, picture, date and author of the entry.

    Returns:
    list: A list of dictionaries, each representing an entry in the RSS feed"""
    
    news_feed = feedparser.parse("http://feeds.feedburner.com/TheHackersNews")
    feed_list = []
    for entry in news_feed.entries:
        feed_list.append(
            {
                "title": entry["title"],
                "summary": entry["summary"],
                "link": entry["link"],
                "picture": entry["links"][1]["href"],
                "date": entry["published"],
                "author": entry["author"],
            }
        )
    return feed_list


if __name__ == "__main__":
    print(get_feed()[0])
    pass
