import praw
from userpw import *

class prawer:
    def __init__(self):
        self.r = praw.Reddit(client_id=client_id, client_secret=client_secret,
                             username=username, password=password,
                             user_agent=user_agent)

