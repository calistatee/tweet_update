import tweepy

# log in via codes provided by Twitter
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

# this is for authentication by using OAuthHandler and set_access_token method
# from tweepy with a bunch of codes hidden to us
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# main variables where we'll do all the twitter magic
api = tweepy.API(auth)

# if authentication was successful, should be able to see the name
# of my account printed out
print(api.me().name)

# my application settings are set for "Read and Write"
# this line should tweet out my message to my account's timeline
# can’t update duplicate status

api.update_status(status = "hello world")