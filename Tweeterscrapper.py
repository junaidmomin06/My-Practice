# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 09:54:36 2021

@author: user
"""

from twitterscraper import query_tweets
import pandas as pd
import datetime as dt

begin_date = dt.date(2020,4,15)
end_date = dt.date(2020,4,18)

limit = 100
lang = 'english'

#user = realDonaldTrump

tweets = query_tweets("#covid-19", begindate = begin_date, enddate = end_date, limit = limit, lang = lang)
df = pd.DataFrame(t.__dict__ for t in tweets)

