# Dependencies
import numpy as np
import tweepy
import time
import json
# Twitter API Keys
consumer_key = 'NifRehCGUHRSUFBk0vv0Vjing'
consumer_secret = 'DnviBCITMk7LgBQYCqoHafODESCC6rBOcJp9ZdpCLwhWgfKFUz'
access_token = '979169820619849728-tSWnLhGzAoWLHnlTNezh3LV94TIeWBy'
access_token_secret = 'kHoW9NPeMBTE0KY8P3aA1BcIXzU6oYL6qLPK9EI5Uzr7t'
# Target Term
target_term = "@frankhasuer"
# Opening message
print("We're going live!")
# Create Thank You Function
def ThankYou():

    # Twitter Credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Search for all tweets
    public_tweets = api.search(target_term, count=5, result_type="recent")

    # Loop through all tweets
    for tweet in public_tweets['statuses']:

        # Get ID and Author of most recent tweet directed to me
        tweet_id = twee['id']
        tweet_author = tweet['user']['screen_name']
        
        # Print the tweet_id
        print(tweet_id)
        

        # Use Try-Except to avoid the duplicate error
        try:
            api.update_status('Thank you @%s! Come again!' % tweet_author, in_reply_to_status_id=tweet_id)
            
            # Print success message
            print('Success')

            # Print message if duplicate
        except Exception:
            print('Already responded to this one')

        # Print message to signify complete cycle
        print('We are done for now. I will  chack again in 60 seconds')

while (True):
    ThankYou()
    time.sleep(60)