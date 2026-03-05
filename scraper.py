import praw


CLIENT_ID = 'qBrnSZel40RxSGLjgUDgjg',
CLIENT_SECRET ='4wvbeFYiPOVW-tTJ5bKzpxU7HJvULw',
USER_AGENT = "silent_pain_app"




reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

def fetch_complaints(query, limit=100):

    complaints = []

    search_queries = [
        f"{query} I hate",
        f"{query} I wish",
        f"{query} frustrating",
        f"{query} problem"
    ]

    for q in search_queries:

        for submission in reddit.subreddit("all").search(q, limit=limit):

            complaints.append(submission.title)

            if submission.selftext:
                complaints.append(submission.selftext)

    return complaints