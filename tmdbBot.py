from dotenv import load_dotenv
import requests
import os
from datetime import datetime, timedelta
load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_API_URL = "https://api.themoviedb.org/3/"
POSTER_PATH = "https://image.tmdb.org/t/p/w500"
TMDB_URL = "https://www.themoviedb.org/movie/"
IMDB_URL = "https://m.imdb.com/title/"
ADD_DAYS = 2 # No of days added to current day to pull data

def convertTextToBold(input_text):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    bold_chars = "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
    output = ""
    for character in input_text:
        if character in chars:
            output += bold_chars[chars.index(character)]
        else:
            output += character 
    return output

def getMoviesReleasingToday():
    current_date = datetime.today()
    # print(f'current_date: {current_date}')
    future_date = current_date + timedelta(days=ADD_DAYS)
    # print(f'future_date: {future_date}')
    formatted_date = future_date.strftime("%Y-%m-%d")
    # print(f'formatted_date: {formatted_date}')
    resp = requests.get(
        f'{TMDB_API_URL}discover/movie?api_key={TMDB_API_KEY}&language=en-US&air_date.gte=&region=US&release_date.gte={formatted_date}&release_date.lte={formatted_date}&show_me=0&sort_by=primary_release_date.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=0&with_original_language=en&with_release_type=3&with_runtime.gte=0&with_runtime.lte=400')
    # print(resp)
    if resp.status_code != 200:
        # Throws an exception out
        status_code, status_message = resp.json()
        raise requests.RequestException(
            'GET /discover/movie/ {}'.format(f'{status_code} > {status_message}'))
    responseData = resp.json()
    return responseData['results']

def getMovieDetails(movieID):
    resp = requests.get(
        f'{TMDB_API_URL}movie/{movieID}?api_key={TMDB_API_KEY}&language=en-US')
    print(resp)
    if resp.status_code != 200:
        # Throws an exception out
        status_code, status_message = resp.json()
        raise requests.RequestException(
            'GET /movie/ {}'.format(f'{status_code} > {status_message}'))
    responseData = resp.json()
    print(responseData)
    return responseData
