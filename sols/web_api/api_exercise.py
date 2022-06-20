# Using the REST API https://timeapi.io/swagger/index.html
# print the day of the week of today and tomorrow. For example:
# >>> Today is Monday
# >>> Tomorrow will be Tuesday
# Use the UTC time zone in the requests

import requests

tz = "UTC"
api_server = "https://timeapi.io"

# Get current day of the week
api_endpoint = "/api/Time/current/zone"
request_headers = {
  "Accept": "application/json"
}
query_params = {
  "timeZone": tz
}
response = requests.get(api_server+api_endpoint, params=query_params, headers=request_headers)
response_json = response.json()

print("Today is %s" % response_json["dayOfWeek"])

# Get the date of tomorrow
api_endpoint = "/api/Calculation/current/increment"
request_headers = {
  "Accept": "application/json",
  "Content-type": "application/json"
}
post_data = {
  "timeZone": tz,
  "timeSpan": "1:00:00:00"
}
response = requests.post(api_server+api_endpoint, json=post_data, headers=request_headers)
response_json = response.json()
tomorrow_date = "%d-%02d-%02d" % (
  response_json["calculationResult"]["year"],
  response_json["calculationResult"]["month"],
  response_json["calculationResult"]["day"]
)

# Get tomorrow's day of the week
api_endpoint = "/api/Conversion/DayOfTheWeek/" + tomorrow_date
request_headers = {
  "Accept": "application/json"
}
response = requests.get(api_server+api_endpoint, headers=request_headers)
response_json = response.json()
print("Tomorrow will be %s" % response_json["dayOfWeek"])

