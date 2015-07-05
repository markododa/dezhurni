#!/usr/bin/env python
# -*- coding: utf-8
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'mk_MK.utf8')
from people import people

def tabela(people):
    def dateread(file):
        year, month, day = map(int, open(file, 'r').readline().split())
        return datetime.date(year=year, month=month, day=day)
    
    def datewrite(file, datum):
        file = open(file, 'w')
        file.write(datum.strftime('%Y %-m %-d'))
        file.close()

    if datetime.datetime.now().date() > dateread('nextdate'):
        startdate = dateread('nextdate')
        datewrite('startdate', dateread('nextdate'))
    else:
        startdate = dateread('startdate')
        
    week_end = startdate+datetime.timedelta(days=-1)
    ord_no=1
    out = """{| class="wikitable" border="1" cellpadding="3" cellspacing="1"\n|-\n! Ред бр.\n! Дежурен\n! Датум\n! Забелешка\n"""
    
    for x in (range(3)):
        for person in people:
            name, email = person
            week_start = week_end + datetime.timedelta(days=1)
            week_end = week_end + datetime.timedelta(days=7)
            out += '|-\n'
            out += '| '+str(ord_no)+'\n'
            out += '| '+name+'\n'
            out += '| '+week_start.strftime('%-d %b')+' до '+week_end.strftime('%-d %b %Y')+'\n'
            out += "| \n"
            ord_no += 1
            if x == 0:
                nextdate = week_end + datetime.timedelta(days=1)
                datewrite('nextdate', nextdate)
    out += "|}"
    return out

print(tabela(people))
