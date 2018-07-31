import imggen
import cmc
import praw
import re
from datetime import datetime
from userpw import *

try:
    cmcdata = cmc.getcmc()
    cmctext = ''
    for i in cmcdata:
        print(i["id"])
        cmctext += "{0}. **{1} ({2}) - ${3:.2f}B - ${4:.2f}**\n".format(i["rank"], i["name"], i["symbol"], float(i["market_cap_usd"])/1e9, float(i["price_usd"]))
    cmctext = cmctext[:-1]
    print(cmctext)
    with open('pyticker.log', 'a') as f:
        f.write("{} - successfully got ticker data\n".format(str(datetime.now())))
except:
    with open('pyticker.log', 'a') as f:
        f.write("{} - failed to get ticker data\n".format(str(datetime.now())))

try:
    tickerimg = imggen.imggen(cmcdata)
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
    # sub = reddit.subreddit('cryptocurrencyadmin')
    # print(sub.title)
    ss = sub.stylesheet()
    sstext = ss.stylesheet
    settings = praw.models.reddit.subreddit.SubredditModeration(sub).settings()
    sidebar_contents = settings['description']
    sidebar_contents = re.sub(r'(1\. \*\*Bitcoin.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+\n.+)', cmctext, sidebar_contents)
    # sub.stylesheet.upload("ticker", "img/temp/ticker.png")
    sub.stylesheet.upload("crypto-top10", "img/temp/ticker.png")
    sub.stylesheet.update(sstext)
    praw.models.reddit.subreddit.SubredditModeration(sub).update(description=sidebar_contents)
    with open('pyticker.log', 'a') as f:
        f.write("{} - successfully updated reddit\n".format(str(datetime.now())))
except:
    with open('pyticker.log', 'a') as f:
        f.write("{} - failed to update reddit\n".format(str(datetime.now())))
