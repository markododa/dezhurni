#!/usr/bin/env python2
# -*- coding: utf-8
from  people import people

ord_no=1
out = """{| class="wikitable" border="1" cellpadding="3" cellspacing="1"
|-
! Ред бр.
! Дежурен
! Забелешка
"""

for person in people:
	name, email = person
	out += '|-\n'
    	out += '| '+str(ord_no)+'\n'
    	out += '| '+name+'\n'
    	out += "| \n"
    	ord_no += 1
out += "|-\n|-|}"
print out
