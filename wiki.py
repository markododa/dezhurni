#!/usr/bin/python
from simplemediawiki import MediaWiki
from tabela import tabela
from people import people
import sys
text = '==== Листа на дежурства ====\n\nОва е автоматски генерерирана листа на дежурни со две ротации, доколку не сте во можност да бидете дежурни некоја недела или ден запишете во забелешка и пишете на мејлинг листа. Доколку сте дежурен во вашиот google calendar е вметнат нов календар насловен „Хаклаб: Дежурства“ со настан за деновите кога сте дежурни. Поставете ги известувањата за да бидете навреме известени.\n\n'
text+=tabela(people)
wiki = MediaWiki('https://wiki.spodeli.org/api.php')
user, password = open('credentials', 'r').read().split()
wiki.login(user,password)
token = wiki.call({'action': 'query', 'meta': 'tokens'})['query']['tokens']['csrftoken']
wiki.call({'action': 'edit', 'title': 'Хаклаб/Дежурства', 'section':'5', 'text':text, 'token':token})
