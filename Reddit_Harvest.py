import praw
import inspect
#i = 1
reddit = praw.Reddit(client_id='PurljHA0fr4yYQ',
                     client_secret='URh00WvOlXQz5O_06VhkBhIXtus',
                     user_agent='Maybeatestytestmaybeatroll')
for submission in reddit.subreddit('TIFU').top(time_filter='all', limit=100):
    #filename = "Dataset/TIFUPostTop{}.txt".format(i)
    filename = "TIFUFull.txt"
    filepath = open(filename,"a+",encoding="utf-8")
    if not submission.selftext:
        continue
    filepath.write(submission.selftext + "/n")
    filepath.close()
    #i += 1
# 'selftext' is the attribute of the post 

