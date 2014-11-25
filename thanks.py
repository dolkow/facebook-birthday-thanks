#!/usr/bin/env python2
#coding=utf8

import os
import urllib
import urlparse
import urllib2
import json
from time import mktime, gmtime

def get(token, since, until):
	params = dict()
	params['access_token'] = token
	params['since'] = since
	params['before'] = until
	params['limit'] = 1000
	params = urllib.urlencode(params)

	url_format = 'https://graph.facebook.com/v2.2/me/feed?%s'
	url = url_format % params

	conn = urllib2.urlopen(url)
	try:
		data = conn.read()
	finally:
		conn.close()
	return json.loads(data)

def main():
	names = []
	uids  = []

	# token can be acquired here: https://developers.facebook.com/tools/explorer
	# you'll need the "read_stream" and "publish_actions" permissions.
	token = 'fill this in'

	# Unix timestamp range
	# this is two days ago until now -- can be customized
	end   = int(mktime(gmtime()))
	start = end - 2*24*60*60

	data = get(token, start, end)['data']
	for gratz in data:
		names.append(gratz['from']['name'])
		uids.append(gratz['from']['id'])
		print gratz['from']['id'], gratz['from']['name']

	out = 'Thanks for the birthday wishes, %s and %s!' % (', '.join(names[:-1]), names[-1])
	print out

if __name__ == '__main__':
	main()
