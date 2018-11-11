import praw
from config import Config
import pickle

# Get config vars
f = file('config.cfg')
config = Config(f)

# Authenticate with Reddit
reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     username=config.username,
                     password=config.password,
                     user_agent=config.user_agent)

query = 'Daily Discussion, December'
december_discussions = list(reddit.subreddit('Bitcoin').search(query, sort='new', time_filter='year', limit=None))
query = 'Daily Discussion, January'
january_discussions = list(reddit.subreddit('Bitcoin').search(query, sort='old', time_filter='year', limit=None))
print(january_discussions)
query = 'Daily Discussion, February'
february_discussions = list(reddit.subreddit('Bitcoin').search(query, sort='old', time_filter='year', limit=None))

bitcoin_discussions = december_discussions + january_discussions + february_discussions

for i in bitcoin_discussions:
    print(i.title)

# Save Data
with open('bitcoin_discussions.pickle','w') as f:
    pickle.dump(bitcoin_discussions,f)
