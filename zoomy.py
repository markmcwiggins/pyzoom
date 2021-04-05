#!/usr/bin/env python3

from pyzoom import ZoomClient
from datetime import datetime as dt

def schedule_meeting(when, meetingname, duration = 60, password = 'not-secure'):
    #starttime = dt(2021, 4, 3, 16, 30, 0).isoformat()
    starttime = when.isoformat()
    
    meeting = client.meetings.create_meeting(meetingname, start_time=starttime, duration_min = duration, password = password)
    return meeting




# use ZOOM_API_KEY and ZOOM_API_SECRET environment values
# so as not to expose them in the code

my_zoom_id = 'mark@pythonsoftwarewa.com'

client = ZoomClient.from_environment()

mymeeting = schedule_meeting(dt(2021, 4, 5, 16, 30, 0), 'Interview', 45, 'securepass')

print(mymeeting.start_url)

# get the list of scheduled meetings

response = client.raw.get('/users/%s/meetings' % my_zoom_id)

# the response is raw text, so we need to convert it to Python to be able to use it easily

k = eval(response.text)

# like this:

for m in k['meetings']:
    print(m['topic'], m['join_url'], m['start_time'])


