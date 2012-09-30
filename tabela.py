#!/usr/bin/env python2
# -*- coding: utf-8
from datetime import timedelta as td, datetime as dt
from  people import people

date = dt.date(dt(year=2012, month=9, day=03))
days_offset=7
week_end = date+td(days=-1)
ord_no=1
out = """{| class="wikitable" border="1" cellpadding="3" cellspacing="1"
|-
! Ред бр.
! Дежурен
! Датум [од-до]
! Забелешка
"""

for x in (range(2)):
	for person in people:
		name, email = person
    		week_start = week_end + td(days=1)
    		week_end = date + td(days=days_offset-1)

    		out += '|-\n'
    		out += '| '+str(ord_no)+'\n'
    		out += '| '+name+'\n'
    		out += '| '+str(week_start)+' - '+str(week_end)+'\n'
    		out += "| \n"

    		ord_no += 1
    		days_offset += 7
		if x==0:
			nesho = week_end+td(days=1)
out += "|}"
print out
print nesho
