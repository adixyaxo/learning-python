import requests

r = requests.get('https://aditya-dagar.vercel.app') # gets html txt or json data from urls

print(r.text)

# we can also make post request which is a little complicated where we also send the data look it at the requests docs or documentation page