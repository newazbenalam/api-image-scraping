import http.client
import json
import os

import requests

baseUrl = "9gag.com"
route_initial = "/v1/feed-posts/type/home"

folder_path = "downloaded_images"

import os

def images_from_api(jsonData, folder_path):
    # Create folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Iterate over each post in the JSON data
    for post in jsonData['data']['posts']:
        # Extract image URL from each post
        image_url = post['images']['image700']['url']
        # Download the image
        download_image(image_url, folder_path)
    
    

def download_image(url, folder_path):
    filename = os.path.join(folder_path, url.split("/")[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(url).content)
        
# Driver Code
def start(pages, route):
  conn = http.client.HTTPSConnection(baseUrl)

  payload = ""

  headers = {
      'cookie': "____ri=7644; ____lo=BD",
      'User-Agent': "insomnia/2023.5.8",
      'content-type': "application/json",
      }

  # conn.request("GET", route, payload, headers)

  # res = conn.getresponse()
  # data = res.read()
  # jsonData = json.loads(data.decode("utf-8"))

  # print(data.decode("utf-8"))
  # image_urls = [post['images']['image700']['url'] for post in jsonData['data']['posts']]
  # print(image_urls[0])
    
  for page in range(pages):
    # if page > 1:
    conn.request("GET", route, payload, headers)
    res = conn.getresponse()
    data = res.read()
    jsonData = json.loads(data.decode("utf-8"))
    
    route = f"{route_initial}?{jsonData['data']['nextCursor']}"
      
    print(res.status)
    print(route)
    images_from_api(jsonData, folder_path)

start(5, route_initial) # define how many pages you want to scrap





