import tweepy
import pandas as pd
from collections import Counter

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Set up Tweepy authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Input for Twitter usernames
users_input = input("Whose Twitter information do you want? (Separate usernames with commas): ")
users = [user.strip() for user in users_input.split(',')]

def get_followings(username):
    try:
        user = api.get_user(screen_name=username)
        return [friend.screen_name for friend in tweepy.Cursor(api.friends, screen_name=username).items()]
    except tweepy.TweepError as e:
        print(f"Error getting followings for {username}: {e}")
        return []

followings = {}
following_list = []

for person in users:
    print('#####\nStarting: ' + person + '\n#####')
    try:
        followings[person] = get_followings(person)
        following_list = following_list + followings[person]
    except KeyError:
        print('IndexError')

counter_result = Counter(following_list).most_common(10)
print("Top 10 followed users:", counter_result)

follow_relations = {}

for following_user in followings.keys():
    follow_relation_list = []
    for followed_user in followings.keys():
        if followed_user in followings[following_user]:
            follow_relation_list.append(True)
        else:
            follow_relation_list.append(False)
    follow_relations[following_user] = follow_relation_list

following_df = pd.DataFrame.from_dict(follow_relations, 
                                      orient='index', columns=followings.keys())

print(following_df)
