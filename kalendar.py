#!/usr/bin/env python2
# -*- coding: utf-8
from datetime import timedelta as td
from functions import eventfunc
from people import people
import config

def weekly (name, email, week_start):
	for offset in (config.days):
		eventfunc(week_start+td(days=offset), week_start+td(days=offset+1), name, email)


def postit ():
	date = config.date
	week_end = date+td(days=-1)
	days_offset = 7
	for person in people:
		name, email = person
		week_start = week_end+td(days=1)
		week_end = date + td(days=days_offset-1)
		weekly(name, email, week_start)
		print name, email, week_start, week_end
		days_offset+=7

postit()
