#!/usr/bin/env python3

import tweepy
from listener import WeenieListener
import secret


def main():
    auth = tweepy.OAuthHandler(secret.CONSUMER_TOKEN, secret.CONSUMER_SECRET)
    auth.set_access_token(secret.ACCESS_TOKEN, secret.ACCESS_SECRET)
    api = tweepy.API(auth)
    listener = WeenieListener()
    stream = tweepy.Stream(auth=api.auth, listener=listener())
    stream.filter(track=['@_weenie_bot'])


if __name__ == "__main__":
    main()
