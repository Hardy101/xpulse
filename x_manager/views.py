import tweepy
from django.shortcuts import render

# Create your views here.
def fetch_posted_tweets(request):
    # Twitter API Keys
    api_key = "7je4NADE0Xj2CU6zFl6kHSzwA"
    api_secret = "PptWv5K9l2XSlnBBf1ZdRrGlaRHJlamNzZMbZzUjJ8lp6nVWoy"
    access_token = "1725255780767592449-ZABwZmJH9HCMIfWGMBM4piYHlhUOZS"
    access_token_secret = "hm4NKjLuyNg66dRppIacBsqUeNh6ZdK7zwy3nwHmAhZmr"

    # Authenticate
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Fetch recent tweets (adjust count as needed)
    tweets = api.user_timeline(count=50)  # Adjust 'count' for more/less tweets

    # Structure data for the template
    tweet_data = [
        {
            "text": tweet.text,
            "created_at": tweet.created_at,
            "retweets": tweet.retweet_count,
            "likes": tweet.favorite_count,
        }
        for tweet in tweets
    ]

    return render(request, 'posts.html', {"tweets": tweet_data})

def view_followers(request):
    import requests
    url = "https://api.x.com/2/users/{id}/followers"
    headers = {"Authorization": "Bearer <token>"}
    response = requests.request("GET", url, headers=headers)
    print(response.text)