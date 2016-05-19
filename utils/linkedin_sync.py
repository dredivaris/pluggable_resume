"""linkedin_sync.

Usage: linkedin_sync.py  [ADMIN_USERNAME ADMIN_PASSWORD LINKEDIN_USERNAME LINKEDIN_PASSWORD USER_TO_SCRAPE]

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
import jsonpickle
import json
import requests

from docopt import docopt
from linkedin_selenium_scraper.profile_scraper import LinkedinProfile


import requests
import logging
# These two lines enable debugging at httplib level (requests->urllib3->http.client)
#  You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
#  The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1
# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True



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
        print (auth_token)
    except KeyError:
        print("Error: invalid admin username or password provided")
        exit()

    profile = LinkedinProfile(linkedin_user_account_to_scrape, email, password)
    pickled_profile = jsonpickle.encode(profile)
    payload = json.dumps({
        'resume_id': 1,
        'data': pickled_profile
    })
    headers = {'content-type': 'application/json',
               'authentication-token': auth_token}
    r = requests.post(REMOTE_URL + '/resume/api/v1.0/', data=payload)
    print(r.status_code)
    print(r.content)
