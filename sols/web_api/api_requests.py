from pprint import pprint
import requests
from pprint import pprint, pformat

api_endpoint = "https://timeapi.io/api/Time/current/zone"
query_params = {"timeZone": "Europe/Amsterdam"}
request_headers = {"Accept": "application/json"}

response = requests.get(api_endpoint, params=query_params, headers=request_headers)
print("{:*^80}".format(" REQUEST "))
print("URL: ", response.request.url)
print("HTTP headers: ")
for key, value in response.request.headers.items():
  print(f"  {key}: {value}")
print("Method: ", response.request.method)
print("\n")

print("{:*^80}".format(" RESPONSE "))
print("HTTP status: ", response.status_code)
print("HTTP headers: ")
for key, value in response.headers.items():
  print(f"  {key}: {value}")
print("\n")

print("HTML encoding: ", response.encoding)
print("HTML content: ", response.text)
print("\n")

print("JSON response:\n %s" % pformat(response.json()))
print("\n")

response_dict = response.json()
print("Current Time: %s" % response_dict["time"])
print("\n")
