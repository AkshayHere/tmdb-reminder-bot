# References
# https://realpython.com/api-integration-in-python/
# https://2.python-requests.org/en/latest/api/
import requests

def getRandomQuote():
    # Random Quote Generator
    # https://github.com/lukePeavey/quotable
    resp = requests.get('http://api.quotable.io/random')
    print(resp)
    print(resp.status_code)
    if resp.status_code != 200:
        # Throws an exception out
        raise requests.RequestException(
            'GET /random/ {}'.format(resp.status_code))
    print(resp.json())

    response = resp.json()
    author = response['author']
    quote = response['content']
    # ternary operator
    output = quote+'\n-- '+author if (author != '') else quote
    print('output : '+output)
    return output
