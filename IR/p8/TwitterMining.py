#AIM: Write a program for mining Twitter to identify tweets for a specific period and identify trends and named entities. 

import tweepy
consumer_key = "Z742Rjo1x4xywd0wynsqF0gfs"
consumer_secret = "PjM2E0dJrTIAgHSBB5FnDwzRnoi1Bld5rwaraUELRh3UQ53nRN"
access_token = "1100604691216396289-B0WYU29XPlnmG6C8qcfQNpfHdDkVT8"
access_token_secret = "ool9gDFLDf9ar7fawt2efSV1aIZNn3d8gK5EcnShNSccX"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)


# The Twitter user who we want to get tweets from
name = "SauravAstage"
# Number of tweets to pull
tweetCount = 20

# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print (tweet.text)
