Audiosear.ch Python Client
=========================================

Python client SDK for https://www.audiosear.ch/

See docs at https://www.audiosear.ch/developer/

OAuth credentials are available from https://www.audiosear.ch/oauth/applications

Example:

```python
from audiosearch import Client

# create a client
client = Client( oauth_id, oauth_secret )

# fetch a show with id 1234
show = client.get('/shows/1234')
# or more idiomatically
show = client.get_show(1234)

# fetch an episode
episode = client.get('/episodes/5678')
# or idiomatically
episode = client.get_episode(5678)

# get related content for an episode or show
related = client.get_related(15, {'type': 'shows', 'size': 5, 'from': 5}) # id is required, type: 'episodes' is default

# search episodes
res = client.search({ 'q':'test' }, 'episodes')

# get the next page of results
res = client.search({ 'q':'test', 'page':2 }, 'episodes')

# episode search restricted to a single field
res = client.search({'q':'title:Example Podcast Episode')

# search episodes with a filter
res = client.search({'q':'test','filters':"['show_id':74]"}, 'episodes')

# search episodes with multiple filters
res = client.search({"q":"test", "filters[show_id]":74, "filters[transcripts.transcript]":"experiment"}, 'episodes')

for episode in res['results']:
  print "[%s] %s (%s)" % ( episode['id'], episode['title'], episode['show_title'] )

# tastemakers
recs = client.get_tastemakers({'n': 5}) # type: 'episodes' is the default, may also specify 'type': 'shows'

# trending
trends = client.get_trending()

# person
person = client.get_person(1578)

```

## Development

To run the unit tests, create a **.env** file in the checkout
with the following environment variables set to meaningful values:

```
AS_ID=somestring
AS_SECRET=sekritstring
AS_HOST=http://audiosear.ch.dev
```

Then run the tests:

```bash
make test
```
