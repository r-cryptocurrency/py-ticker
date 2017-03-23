import reddit
import cmc

prawer = reddit.prawer()
prawer.r.login(reddit.username, reddit.password)

sub = prawer.r.get_subreddit('xdn')
ss = sub.get_stylesheet()

ticker_text = cmc.getcmc()

ss_text = """
#header {
background-repeat: repeat;
-webkit-animation: banner 300s infinite linear;
animation: banner 300s infinite linear;
 }

@-webkit-keyframes banner {
from { background-position: 0 0px; }
to { background-position: -5402px 500px; }
}
@keyframes banner {
from { background-position: 0 0px; }
to { background-position: -5402px 0px; }
}
"""

sub.set_stylesheet(ss_text)
print(sub.title)
