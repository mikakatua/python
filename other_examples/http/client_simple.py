import http.client

conn = http.client.HTTPConnection("localhost", 8081)
conn.request("GET", "/")

r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
print(data1)
