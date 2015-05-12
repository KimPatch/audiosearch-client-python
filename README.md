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

# search
res = client.search({ 'q':'test' }, 'episodes')
for episode in res['results']:
  printf("[%s] %s (%s)\n", episode['id'], episode['title'], episode['show_title'])
end

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
