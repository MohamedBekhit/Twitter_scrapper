import urllib.request, urllib.parse, urllib.error
import twitter_url
import json
import ssl


TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#while True:
print('')
acct = input('Enter Twitter Account:')
#if (len(acct) < 1): break
url = twitter_url.augment(TWITTER_URL,
                    {'screen_name': acct, 'count': '2'})
print('\nRetrieving', url)
print("--------------------------------------")
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()
js = json.loads(data)
for element in range(len(js)):
	print(js[element]['text'])
	print('\n')
