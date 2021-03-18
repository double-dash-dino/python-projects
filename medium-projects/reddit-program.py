# This is a program that will send me an email every X days (every day by default) 
# with the top reddit posts of the day.

import getpass
import praw


client_id=getpass.getpass('Please enter your client id')
client_secret=getpass.getpass('Please enter your client secret')
user_agent=getpass.getpass('Please enter your user agent')
username=getpass.getpass('Please enter your username')
password=getpass.getpass('Please enter your password')

reddit = praw.Reddit(
client_id=client_id, 
client_secret=client_secret, 
user_agent=user_agent, 
username=username, 
password=password)

subreddit_of_interest = input('What subreddit would you like to hear about?')

subred = reddit.subreddit(subreddit_of_interest)

top10 = subred.top("week", limit=10)

print(f'***************\nHere is a list of the top 10 posts for this week in r/{subreddit_of_interest}:')

for post in top10:
    print(post.title)
    print(post.url)
    print('*********')