***REMOVED***linkedin_sync.

Usage: linkedin_sync.py  [ADMIN_USERNAME ADMIN_PASSWORD LINKEDIN_USERNAME LINKEDIN_PASSWORD USER_TO_SCRAPE]

Options:
  -h --help     Show this screen.
  --version     Show version.

***REMOVED***
import jsonpickle
import json
import requests

from docopt import docopt
from linkedin_selenium_scraper.profile_scraper import LinkedinProfile

REMOTE_URL = 'http://localhost:5000'

if __name__ == '__main__':
    args = docopt(__doc__, version='linkedin_sync 0.1')
    # print(args)
    username = args['ADMIN_USERNAME']
    admin_password = args['ADMIN_PASSWORD']

    email = args['LINKEDIN_USERNAME']
    password = args['LINKEDIN_PASSWORD']
    linkedin_user_account_to_scrape = 'https://www.linkedin.com/in/{}'.format(args['USER_TO_SCRAPE'])

    # first get auth token
    r = requests.post(REMOTE_URL + '/login/',
                      data=json.dumps({'email': username, 'password': admin_password}),
                      headers={'content-type': 'application/json'})
    try:
        auth_token = r.json()['response']['user']['authentication_token']
    except KeyError:
        print("Error: invalid admin username or password provided")
        exit()

    profile = LinkedinProfile(linkedin_user_account_to_scrape, email, password)
    pickled_profile = jsonpickle.encode(profile)
    payload = json.dumps({
        'resume_id': 0,
        'data': pickled_profile
***REMOVED***)
    headers = {'Content-Type': 'application/json',
               'Authentication-Token': auth_token}
    r = requests.post(REMOTE_URL + '/resume/api/v1.0/', data=payload, headers=headers)
    print(r.status_code)
    print(r.content)
