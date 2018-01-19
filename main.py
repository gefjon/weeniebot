#!/usr/bin/env python3

import tweepy
from listener import WeenieListener
import os


def main():
    auth = tweepy.OAuthHandler(os.environ['CONSUMER_TOKEN'], os.environ['CONSUMER_SECRET'])
    auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])
    api = tweepy.API(auth)
    listener = WeenieListener(api)
    stream = tweepy.Stream(auth=api.auth, listener=listener)
    try:
        stream.filter(track=['@_weenie_bot'])
    except KeyboardInterrupt:
        quit()


if __name__ == "__main__":
    main()
