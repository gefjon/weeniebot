import tweepy
import re

regex = '\b@[A-Za-z0-9_]+\b'
regex = re.compile(regex)


class WeenieListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        tweepy.StreamListener.__init__(self)

    def on_status(self, status):
        to_weenie = []
        with regex.findall(status.text) as usernames:
            for user in usernames:
                if user != '@_weenie_bot':
                    to_weenie.append(user)
        response = ''
        if len(to_weenie) == 0:
            return
        elif len(to_weenie) == 1:
            response = '{} is a weenie'.format(to_weenie[0])
        else:
            response = '{} are all weenies'.format(' '.join(weenie for weenie in to_weenie))
        self.api.update_status(response, status.id)
        print('responded to the tweet "{}" with "{}"'.format(status.text, response))

    def on_error(self, status_code):
        if status_code == 420:
            return False
