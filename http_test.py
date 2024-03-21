import http.client
import json

baseUrl = "9gag.com"
route = "/v1/feed-posts/type/home"
conn = http.client.HTTPSConnection(baseUrl)

payload = ""

headers = {
    'cookie': "____ri=7644; ____lo=BD",
    'User-Agent': "insomnia/2023.5.8",
    'content-type': "application/json",
    }

conn.request("GET", route, payload, headers)

res = conn.getresponse()
data = res.read()
jsonData = json.loads(data.decode("utf-8"))

# print(data.decode("utf-8"))
print(jsonData)
print(res.status)