#!/usr/bin/env python2
# -*- coding: utf-8
import datetime
from calclient import addevent
from people import people
import config

state = 'caldate'

def dateread(file):
    year, month, day = map(int, open(file, 'r').readline().split())
    return datetime.date(year=year, month=month, day=day)

def datewrite(file, date):
    if date:
        file = open(file, 'w')
        file.write(date.strftime('%Y %-m %-d'))
        file.close()
    else:
        print 'Date is to far in the future or past'

def checkdate(date):
    if abs(date - datetime.datetime.now().date()) < datetime.timedelta(days=14):
        return True
    else:
        return False

def addweek (name, email, week_start):
	for offset in (config.days):
		addevent(week_start+datetime.timedelta(days=offset), week_start+datetime.timedelta(days=offset+1), name, email, config.summary, config.location, config.description, config.calendarId)


def addshift (date, people,dryrun=False):
    if checkdate(date):
        week_end=date+datetime.timedelta(days=-1)
        for person in people:
            name, email = person
            week_start = week_end + datetime.timedelta(days=1)
            week_end = week_end + datetime.timedelta(days=7)
            if dryrun == False:
                addweek(name, email, week_start)
            print name, email, week_start, week_end
        return week_end + datetime.timedelta(days=1)
    else:
        return False

datewrite(state, addshift(dateread(state), people))
