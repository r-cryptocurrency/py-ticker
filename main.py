import imggen
import praw
from userpw import *

tickerimg = imggen.imggen()

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,
                     username=username, password=password,
                     user_agent=user_agent)

print(reddit.user.me())
sub = reddit.subreddit('ccticker')
print(sub.title)
ss = sub.stylesheet()
sub.stylesheet.upload("ticker", "img/temp/ticker.png")
sub.stylesheet.update(stylesheettext)
