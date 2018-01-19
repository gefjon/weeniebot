import tweepy
import re
from responder import RespondingThread


class WeenieListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        tweepy.StreamListener.__init__(self)

    def on_status(self, status):
        print('new status {}'.format(status.text))
        res = RespondingThread(status)
        res.start()

    def on_error(self, status_code):
        if status_code == 420:
            return False
