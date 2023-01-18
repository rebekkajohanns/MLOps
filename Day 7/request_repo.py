import requests
#response=requests.get("https://api.github.com/repos/SkafteNicki/dtu_mlops")


#response = requests.get(
#   'https://api.github.com/search/repositories',
#   params={'q': 'requests+language:python'},
#)

response = requests.get('https://imgs.xkcd.com/comics/making_progress.png')
print(response.status_code)

if response.status_code == 200:
   print('Success!')
elif response.status_code == 404:
   print('Not Found.')
print('content')
print(response.content)
print('json')
print(response.json)

with open(r'img.png','wb') as f:
   f.write(response.content)