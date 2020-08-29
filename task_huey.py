import os
import requests
from huey import crontab
from huey.contrib.djhuey import periodic_task

SITE_URL = os.environ.get('SITE_URL')


@periodic_task(crontab(hour='2'))
def every_day_two_am():
    url = '{}/movie/external_api'.format(SITE_URL)
    requests.get(url)

