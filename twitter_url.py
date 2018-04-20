import urllib.request, urllib.parse, urllib.error
import oauth
import Hidden

def augment(url, parameters):
"""
This function augments the twitter url adding the authontication data necessary for the scrapping.
"""
	secrets = Hidden.oauth()
	consumer = oauth.OAuthConsumer(secrets['consumer_key'], secrets['consumer_secret'])
	token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])

	oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, token=token, http_method='GET', http_url=url, parameters=parameters)
	oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)

	return oauth_request.to_url()
