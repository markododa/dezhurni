#!/usr/bin/env python2
# -*- coding: utf-8
import datetime
from functions import eventfunc
from people import people
import config

def dateread(file):
    year, month, day = map(int, open(file, 'r').readline().split())
    return datetime.date(year=year, month=month, day=day)

def datewrite(file, datum):
    file = open(file, 'w')
    file.write(datum.strftime('%Y %-m %-d'))
    file.close()
if dateread('caldate') - datetime.datetime.now().date() < datetime.timedelta(days=17):
    startdate = dateread('caldate')
else:
    exit()

def weekly (name, email, week_start):
	for offset in (config.days):
		eventfunc(week_start+datetime.timedelta(days=offset), week_start+datetime.timedelta(days=offset+1), name, email)


def postit (startdate):
    week_end=startdate+datetime.timedelta(days=-1)
    for person in people:
        name, email = person
        week_start = week_end + datetime.timedelta(days=1)
        week_end = week_end + datetime.timedelta(days=7)
        weekly(name, email, week_start)
        print name, email, week_start, week_end
        nextdate = week_end + datetime.timedelta(days=1)
        datewrite('caldate', nextdate)

postit(startdate)
