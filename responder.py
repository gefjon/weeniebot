import threading
import tweepy
import re
import os


class RespondingThread(threading.Thread):
    def __init__(self, tweet):
        self.tweet = tweet
        threading.Thread.__init__(self)

    def tweet_reply(self, text):
        auth = tweepy.OAuthHandler(os.environ['CONSUMER_TOKEN'], os.environ['CONSUMER_SECRET'])
        auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])
        api = tweepy.API(auth)
        api.update_status(text, self.tweet.id)

    def single_person(self, weenie):
        if weenie == '@{}'.format(self.tweet.user.screen_name):
            return '{} you are a weenie'.format(weenie)
        else:
            return '{} is are a weenie'.format(weenie)

    def no_names(self):
        return '@{} you are a weenie'.format(self.tweet.user.screen_name)

    def many_people(self, weenies):
        response = ''
        for weenie in weenies:
            response += '{} '.format(weenie)
        return response + ' are all a bunch of weenies'

    def run(self):
        regex = re.compile('(?<=^|(?<=[^a-zA-Z0-9-_\.]))(@[A-Za-z0-9_]+)')

        to_weenie = []
        usernames = regex.findall(self.tweet.text)
        for user in usernames:
            if user != '@_weenie_bot':
                to_weenie.append(user)
        if len(to_weenie) == 0:
            self.tweet_reply(self.no_names())
        elif len(to_weenie) == 1:
            self.tweet_reply(self.single_person(to_weenie[0]))
        else:
            self.tweet_reply(self.many_people(to_weenie))
