import praw
import os

def newest_exists_in_log(log):
    if(os.path.exists(log)):
        with open(log) as file:
            for submission in reddit.subreddit(sub).new(limit=1):
                if str(submission.id) in file.read():
                    #os.remove(log)
                    logged_posts.append(submission.id)
                    return True
                else:
                    return False

newest_exists_in_log('logged.csv')

file = open('logged.csv', 'a+')
try:
    print('Newest Posts: [Ctrl + C to quit]')
    while(True):
        for submission in reddit.subreddit(sub).new(limit=1):
            #if (newest_exists_in_log('logged.csv') == False and submission.id not in logged_posts):
            if("[S]" in submission.title and submission.id not in logged_posts):
                print(submission.id + " " + submission.title)
                file.write(submission.id + ", ")
                logged_posts.append(submission.id)

except KeyboardInterrupt:
    print(' RPU terminated.')
    file.close()
    pass


def main():
    # reddit script login 
    reddit = praw.Reddit(client_id="eLrU3U_JSn0QjA",
                        client_secret="vUkldgPBoyQzAoMvZJ6mkUMywYM",
                        user_agent="rpmupdater")

    print("What subreddit would you like to updates from ")
    sub = input()
    logged_posts = []

if __name__ == "__main__":
    main()