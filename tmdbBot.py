# References
# https://realpython.com/api-integration-in-python/
# https://2.python-requests.org/en/latest/api/
import requests
from datetime import datetime

def getMoviesReleasingToday():
    API_KEY="e2d839f38159f4c867f24fe905f323af"
    POSTER_PATH="https://image.tmdb.org/t/p/w500/"
    formatted_date = datetime.now().strftime("%Y-%m-%d")
    future_date = formatted_date + datetime.timedelta(days=1)
    resp = requests.get(f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&air_date.gte=&region=US&release_date.gte={future_date}&release_date.lte={future_date}&show_me=0&sort_by=primary_release_date.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=0&with_original_language=en&with_release_type=3&with_runtime.gte=0&with_runtime.lte=400')
    print(resp)
    print(resp.status_code)
    print(resp.status_message)
    if resp.status_code != 200:
        # Throws an exception out
        raise requests.RequestException(
            'GET /discover/movie/ {}'.format(resp.status_message))
    print(resp.json())

    response = resp.json()
    results = response['results']
    # ternary operator
    output = quote+'\n-- '+author if (author != '') else quote
    print('output : '+output)
    return output
