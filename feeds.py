feeds.py

import feedparser

def get_feed(url, max_items=3):
    feed = feedparser.parse(url)
    return [f"• [{e.title}]({e.link})" for e in feed.entries[:max_items]]

def get_news():
    sources = {
        "Krebs on Security": "https://krebsonsecurity.com/feed/",
        "The Hacker News": "https://feeds.feedburner.com/TheHackersNews",
        "CyberScoop": "https://www.cyberscoop.com/feed/",
        "Dark Reading": "https://www.darkreading.com/rss.xml"
    }

    final = "🛡️ **Top Cybersecurity Headlines**\n"
    for name, url in sources.items():
        try:
            items = get_feed(url)
            final += f"\n__**{name}**__\n" + "\n".join(items) + "\n"
        except Exception:
            final += f"\n{name} - ⚠️ Error fetching news\n"
    return final
