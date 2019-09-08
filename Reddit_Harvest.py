import praw
import inspect
#i = 1
reddit = praw.Reddit(
                     user_agent='Maybeatestytestmaybeatroll')
for submission in reddit.subreddit('TIFU').top(time_filter='all', limit=10000):
    #filename = "Dataset/TIFUPostTop{}.txt".format(i)
    filename = "TIFU.txt"
    filepath = open(filename,"a+",encoding="utf-8")
    if not submission.selftext:
        continue
    filepath.write(submission.selftext + "/n")
    filepath.close()
    #i += 1
# 'selftext' is the attribute of the post 

