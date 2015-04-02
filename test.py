#!/usr/bin/env python2
# -*- coding: utf-8
from datetime import datetime as dt
from datetime import timedelta as td
from functions import eventfunc
import config
startDate = dt.date(dt(year=2014, month=06, day=18))
endDate = startDate + td(days=1)
eventfunc(startDate, endDate, "Test", 'andrejtrajchevski@gmail.com')
