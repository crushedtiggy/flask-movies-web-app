import requests

url = "https://imdb8.p.rapidapi.com/title/auto-complete"

querystring = {"q":"game of thr"}

headers = {
    'x-rapidapi-key': "c403d25882mshd4c054b7b7572ebp115fa9jsn69f49911e2c5",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)