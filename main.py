import imggen
import praw
from datetime import datetime
from userpw import *

try:
    tickerimg = imggen.imggen()
    with open('pyticker.log', 'a') as f:
        f.write("{} - successfully created ticker image\n".format(str(datetime.now())))
except:
    with open('pyticker.log', 'a') as f:
        f.write("{} - failed to created ticker image\n".format(str(datetime.now())))


try:
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,
                         username=username, password=password,
                         user_agent=user_agent)
    
    print(reddit.user.me())
    sub = reddit.subreddit('cryptocurrency')
    # print(sub.title)
    ss = sub.stylesheet()
    sstext = ss.stylesheet
    sub.stylesheet.upload("ticker", "img/temp/ticker.png")
    sub.stylesheet.update(sstext)
    with open('pyticker.log', 'a') as f:
        f.write("{} - successfully updated reddit\n".format(str(datetime.now())))
except:
    with open('pyticker.log', 'a') as f:
        f.write("{} - failed to update reddit\n".format(str(datetime.now())))
