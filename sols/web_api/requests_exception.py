import requests

url="https://httpstat.us/200?sleep=5000"

try:
    r = requests.get(url, timeout=3)
    r.raise_for_status()
# Capture HTTP error codes >+ 400
except requests.exceptions.HTTPError as errh:
    raise SystemExit(errh)
# Capture generic errors
except requests.exceptions.RequestException as err:
    raise SystemExit(err)

print("Request successful")
print(r.status_code, r.request.url)