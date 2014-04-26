#!/usr/bin/env python2
# -*- coding: utf-8
#promena vtora mesto bla
import gflags
import httplib2
import config

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run
from datetime import timedelta, datetime as dt

FLAGS = gflags.FLAGS

#Auth section
# Set up a Flow object to be used if we need to authenticate. This
# sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
# the information it needs to authenticate. Note that it is called
# the Web Server Flow, but it can also handle the flow for native
# applications
# The client_id and client_secret are copied from the API Access tab on
# the Google APIs Console
FLOW = OAuth2WebServerFlow(
    client_id=config.client_id,
    client_secret=config.client_secret,
    scope=config.scope,
    user_agent=config.user_agent)

# To disable the local server feature, uncomment the following line:
# FLAGS.auth_local_webserver = False

# If the Credentials don't exist or are invalid, run through the native client
# flow. The Storage object will ensure that if successful the good
# Credentials will get written back to a file.
storage = Storage('calendar.dat')
credentials = storage.get()
if credentials is None or credentials.invalid == True:
  credentials = run(FLOW, storage)

# Create an httplib2.Http object to handle our HTTP requests and authorize it
# with our good Credentials.
http = httplib2.Http()
http = credentials.authorize(http)

# Build a service object for interacting with the API. Visit
# the Google APIs Console
# to get a developerKey for your own application.
service = build(serviceName='calendar', version='v3', http=http,
       developerKey=config.developerKey)


#Event adding part
def eventfunc (startDate, endDate, name, email):
	event = {
		'summary': config.summary + name,
		'location': config.location,
		'description' : config.description,
		'start': {'date': startDate.strftime('%Y-%m-%d')},
		'end': {'date': endDate.strftime('%Y-%m-%d')},
		'attendees': [{'email': email}],
		"reminders": {"useDefault": "useDefault"}
		}
	created_event = service.events().insert(calendarId=config.calendarId, body=event).execute()
	print created_event['id']
