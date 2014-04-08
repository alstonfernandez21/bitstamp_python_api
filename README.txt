How to use the API
# Import the bitstamp_api
import bitstamp_api

secret = "YOUR_SECRET"
key    = "KEY_HERE"
cid    = "YOUR CID"


# Get account balance
bal = bitstamp_api.account_balance(secret, key, cid)
print bal
print bal["fee"]

# Get user transactions
user_trans = bitstamp_api.user_transactions(secret, key, cid)
print user_trans
~
