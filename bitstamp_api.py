#!//usr/bin/python
import os
import time
import sys
import hashlib
import base64
import hmac
import urllib
import json
import time

def ticker():
  f = urllib.urlopen("https://www.bitstamp.net/api/ticker/")
  res = f.read()
  to_json = json.loads(res)
  return to_json

# Function authenticates to bitstamp and retrieves account balance
# in a json hash
def account_balance(secret, key, cid):
  API_SECRET = bytes(secret).encode('utf-8')
  API_KEY = bytes(key).encode('utf-8')
  client_id = bytes(cid).encode('utf-8')
  # Strip unix epoch timestamp of milliseconds
  ts_unix = bytes(time.time())[0:10].encode('utf-8')
  # Message string will contain timstamp + client_id API_KEY
  message = bytes(ts_unix + client_id + API_KEY).encode('utf-8')

  # Our signature needs to contain the API_SECRET, message. It is then encoded in sha256 using hmac module
  # The encoded string is then converted into a 64 Character HASH in all uppercase
  sig = hmac.new(API_SECRET, msg=message, digestmod=hashlib.sha256).hexdigest().upper()

  # We now need to prepare our key, signature and nonce values to be POSTED to the url in a params hash
  params = urllib.urlencode({'key' : API_KEY, 'signature': sig, 'nonce' : ts_unix})
  # we open the url and post the values
  f = urllib.urlopen("https://www.bitstamp.net/api/balance/", params)
  res = f.read()
  # The result is converted to json and returned
  to_json = json.loads(res)
  time.sleep(1)
  return to_json


def user_transactions(secret, key, cid, offset = 0, limit = 100, sort = 'desc'):
  API_SECRET = bytes(secret).encode('utf-8')
  API_KEY = bytes(key).encode('utf-8')
  client_id = bytes(cid).encode('utf-8')

  ts_unix = bytes(time.time())[0:10].encode('utf-8')
  message = bytes(ts_unix + client_id + API_KEY).encode('utf-8')
  sig = hmac.new(API_SECRET, msg=message, digestmod=hashlib.sha256).hexdigest().upper()
  params = urllib.urlencode({'key' : API_KEY, 'signature': sig, 'nonce' : ts_unix, 'offset' : offset, 'limit' : limit,  'sort' : sort})
  f = urllib.urlopen("https://www.bitstamp.net/api/user_transactions/", params)
  res = f.read()
  to_json = json.loads(res)
  time.sleep(1)
  return to_json

