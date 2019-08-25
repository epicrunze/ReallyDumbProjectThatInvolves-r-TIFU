import praw
import inspect

x = []

reddit = praw.Reddit(client_id='PurljHA0fr4yYQ',
                     client_secret='URh00WvOlXQz5O_06VhkBhIXtus',
                     user_agent='Maybeatestytestmaybeatroll')

for submission in reddit.subreddit('TIFU').top(time_filter='all', limit=10):
    x.append(submission.selftext)
print(x[6])