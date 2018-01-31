import tweepy

# log in via codes provided by Twitter
consumer_key = 'enter your consumer key'
consumer_secret = 'enter your consumer secret key'

access_token = 'enter your access token'
access_token_secret = 'enter your access token secret'

# this is for authentication by using OAuthHandler and set_access_token method
# from tweepy with a bunch of codes hidden to us
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# main variables where we'll do all the twitter magic
api = tweepy.API(auth)

# if authentication was successful, should be able to see
# your twitter account name printed out
print(api.me().name)

# make sure your application settings are set for "Read and Write"
# this line should tweet out your message to your account timeline
# no duplicated status allowed

api.update_status(status = "thank you for reading my code!")
