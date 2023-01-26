from dotenv import load_dotenv
import tweepy
import time
import tmdbBot
import os
load_dotenv()

# Set the various access codes
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")
USER_ID = ""  # TEST IF YOUR USER ID GETS DATA HERE

def getUserTweets():
    client = tweepy.Client(bearer_token)
    tweets = client.get_users_tweets(id=USER_ID, tweet_fields=[
                                     'context_annotations', 'created_at', 'geo'])
    for tweet in tweets.data:
        print(tweet)


def generateMovieTweetDaily():
    client = tweepy.Client(consumer_key=consumer_key,
                           consumer_secret=consumer_secret,
                           access_token=access_token,
                           access_token_secret=access_token_secret)

    tmdbResults = tmdbBot.getMoviesReleasingToday()
    for result in tmdbResults:
        # print(result)
        # Create poster path
        resultPoster = result['poster_path']
        posterPath = f'{tmdbBot.POSTER_PATH}{resultPoster}'
        overview = result['overview']
        release_date = result['release_date']

        title = result['title']
        resultID = result['id']
        movieDetails = tmdbBot.getMovieDetails(resultID)
        imdbPath = f'{tmdbBot.IMDB_URL}{movieDetails["imdb_id"]}'
        popularity = "{0:.0f}%".format(movieDetails["popularity"])
        runtime = time.strftime(
             "%M hr %S min", time.gmtime(movieDetails["runtime"])) if movieDetails["runtime"] > 0 else "NA"
        budget = f'USD {movieDetails["budget"]:,}' if movieDetails["budget"] > 0 else "NA"

        # Genres
        genres = []
        for genre in movieDetails["genres"]:
            genres.append(genre["name"])
        genreText = ', '.join(genres)

        # Generate Contents
        tweetContent = f'{tmdbBot.convertTextToBold(title)} ({release_date})  \nGenre: {genreText} \n- "{movieDetails["tagline"]}" \n {imdbPath}'
        print(tweetContent)
        replyContent = f'Overview: \n {overview}' if (len(
            result['overview']) < 141) else (f'Popularity Score: {popularity} \nRuntime: {runtime} \nBudget: {budget} \nPoster Link: {posterPath}')
        print(replyContent)

        # Create first tweet
        parent_tweet = client.create_tweet(text=tweetContent)
        print(parent_tweet)
        parent_data = parent_tweet[0]
        print(parent_data['id'])

        # Create reply tweet for a thread
        details_tweet = client.create_tweet(
            text=replyContent, in_reply_to_tweet_id=parent_data['id'])
        print(details_tweet)

generateMovieTweetDaily()
