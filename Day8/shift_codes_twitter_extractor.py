import csv
import datetime
import tweepy

__author__ = 'maydee'


def authenticate():
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    global api
    api = tweepy.API(auth)


def get_user_timeline(num_tweets):
    """ Get the last num_tweets tweets from the user_id account."""

    all_tweets = api.user_timeline(user_id=user_id, count=num_tweets)
    result_tweets = []
    result_dates = []
    for tweet in all_tweets:
        if ("BL2" in tweet.text) or ("BL:TPS" in tweet.text):
            result_tweets.append(tweet)
        if "[Active through" in tweet.text:
            result_dates.append(tweet.text[tweet.text.index(']')-5:tweet.text.index(']')])
    return result_tweets, result_dates


def get_id_from_screenname(screen_name):
    """Get the ID from the screen_name of the user."""
    return api.get_user(screen_name=screen_name).id


def up_to_date_tweets(tweets_and_dates):
    """Delete the codes which are out of date."""

    result = []
    for tweet, tweet_date in tweets_and_dates:
        if datetime.date(datetime.date.today().year, int(tweet_date[:2]), int(tweet_date[-2:])) > datetime.date.today():
            result.append((tweet, tweet_date))
    return result


def codes_into_csv(filename, codes):
    if ".csv" not in filename:
        filename += ".csv"
    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel', delimiter=',', doublequote = True,
                                lineterminator = '\r\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["GAME", "CODE", "EXPIRE DATE"])
        for code, code_date in codes:
            spamwriter.writerow([code.text.split("\n")[0], code.text.split("\n")[1],
                                 datetime.date(datetime.date.today().year, int(code_date[:2]), int(code_date[-2:]))])
            print([code.text.split("\n")[0], code.text.split("\n")[1],
                   datetime.date(datetime.date.today().year, int(code_date[:2]), int(code_date[-2:]))])


amount_of_tweets = 100
api = None
csv_filename = "codes_borderlands.csv"

authenticate()
user_id = get_id_from_screenname("Borderlands")
tweets, dates = get_user_timeline(amount_of_tweets)
recent_active_codes = up_to_date_tweets(zip(tweets, dates))

for item, date in recent_active_codes:
    print("{}\n time: {}\n".format(item.text, date))

codes_into_csv(csv_filename, recent_active_codes)