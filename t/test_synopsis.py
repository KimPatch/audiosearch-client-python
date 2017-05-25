import os
import json

import unittest
from unittest import TestCase

import sys
sys.path.append("../audiosearch")
sys.path.append(".")

from audiosearch import Client

import pprint

import dotenv
dotenv.load_dotenv('.env')

class TestSynopsis(TestCase):

    def setUp(self):
        self.client = Client(os.environ.get('AS_ID'), os.environ.get('AS_SECRET'), os.environ.get('AS_HOST'))

    def test_constructor(self):
        self.assertTrue(self.client)

    def test_search(self):
        resp = self.client.search({'q':'test'})
        #pprint.pprint(resp)
        self.assertTrue(resp)
        self.assertEqual(resp['query'], 'test')
        self.assertEqual(resp['page'], 1)
        self.assertEqual(len( resp['results'] ), 10)
        for hit in resp['results']:
            self.assertTrue(hit['title'])

    def test_episodes(self):
        episode_i = self.client.get_episode(5678)
        episode = self.client.get('/episodes/5678')
        self.assertEqual(episode_i['title'], episode['title'])
        trending = self.client.get_trending()
        trending_i = self.client.get('/trending/')
        self.assertEqual(trending[0]['trend'], trending_i[0]['trend'])
        tm = self.client.get_tastemakers(1)
        tm_i = self.client.get('/tastemakers/episodes/1')
        if len(tm) > 0:
            self.assertEqual(tm[0]['episode']['title'], tm_i[0]['episode']['title'])
        rel = self.client.get_related(15)
        rel_i = self.client.get('/episodes/15/related/')
        self.assertEqual(rel[0]['title'], rel_i[0]['title'])

    def test_shows(self):
        show = self.client.get('/shows/1234')
        show_i = self.client.get_show(1234)
        self.assertEqual(show['title'], show_i['title'])
        # fetch with absolute url
        show_abs = self.client.get(show_i['urls']['self'])
        self.assertEqual(show_abs['id'], show_i['id'])


if __name__ == '__main__':
    unittest.main()
