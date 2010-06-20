import feedparser

def title(feed):
    if entry.has_key("title"):
        return entry["title"]
    else:
        return "[Untitled]"

def content(feed):
    if entry.has_key("content"):
        out = ""
        for content in entry.content:
            out += content.value
        return out
    elif entry.has_key("desciption"):
        return entry.description
    return "[Empty]"

feed = feedparser.parse("http://www.facebook.com/feeds/notifications.php?id=1442653315&viewer=1442653315&key=471db49804&format=rss20")
out = "<html><body><center>"
for entry in feed['entries']:
    out += "<b>%s</b><br/>%s<hr/><br/>" % (title(feed), content(feed))
out += "</center></body></html>"
open("feed.html", "w").write(out.encode('ascii', 'ignore'))
