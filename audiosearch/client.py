"""
Audiosear.ch Client
Copyright 2015 Pop Up Archive
"""

import requests
from base64 import b64encode
import pprint

class Client(object):

    version = '1.0.0'

    def __init__(self, oauth_key, oauth_secret, oauth_host='https://www.audiosear.ch'):
        if oauth_key is None:
            raise "OAuth key required"
        if oauth_secret is None:
            raise "OAuth secret required"
        
        self.key = oauth_key
        self.secret = oauth_secret
        self.host = oauth_host

        # get oauth token
        params = {'grant_type':'client_credentials'}
        unencoded_sig = "{}:{}".format(self.key, self.secret)
        signature = b64encode(unencoded_sig)
        headers = {'Authorization': "Basic {}".format(signature),
                   'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.host+'/oauth/token', params=params, headers=headers)
        result = response.json()
        #pprint.pprint(result)
        self.access_token = result.get('access_token', None)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def get(self, path, params={}):
        headers = {'Authorization': "Bearer " + self.access_token}
        resp = requests.get(self.host+'/api'+path, params=params, headers=headers)
        return resp.json()

    def search(self, params, type='episodes'):
        #pprint.pprint(params)
        return self.get('/search/'+type, params)

    def get_show(self, show_id):
        return self.get('/shows/'+str(show_id))

    def get_episode(self, ep_id):
        return self.get('/episodes/'+str(ep_id))

