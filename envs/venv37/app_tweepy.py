import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("UzvIlVhhDeQC3aqTYKEbakmey", "vo37kFpweSg7A7qnlBngBzvesr6TjUWdLaOpDczcXsLgy0Sbqi")
auth.set_access_token("1445216835729645571-addOSoHeodBYWSSVXhfkeXCJwetPC1","SYWyzhAltn1tt0vGSZwjpcnP3sZsilQBnZ1UCKGSTMye")
api = tweepy.API(auth)
# test authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#all_keys = open('twitterkeys', 'r').read().splitlines()
#api_key = all_keys[UzvIlVhhDeQC3aqTYKEbakmey]
#api_key_secret = all_keys[vo37kFpweSg7A7qnlBngBzvesr6TjUWdLaOpDczcXsLgy0Sbqi]
#access_token = all_keys[1445216835729645571-addOSoHeodBYWSSVXhfkeXCJwetPC1]
#access_token_secret = [SYWyzhAltn1tt0vGSZwjpcnP3sZsilQBnZ1UCKGSTMye]

#authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
#authenticator.set_access_token(access_token, access_token_secret)

#api = tweepy.API(authenticator, wait_on_rate_limit=True)
#api.create_friendship('SeamusRMurphy')

api = tweepy.API(auth, wait_on_rate_limit=True)
api.create_friendship('SeamusRMurphy')
