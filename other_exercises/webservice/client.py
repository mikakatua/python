import requests

r = requests.get('https://api.github.com/user', auth=('ricardoahumada', 'izaskun7'))
r.status_code
r.headers['content-type']
r.encoding
r.text
data = r.json()
print(data)
print(data['login'])
