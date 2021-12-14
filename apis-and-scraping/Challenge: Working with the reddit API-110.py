## 2. Authenticating with the API ##

import json

# Create a dictionary of headers containing our Authorization header.
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}


params={"t":"day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params =params)


python_top=response.json()
print(response.json())

## 3. Getting the Most Upvoted Post ##



python_top_articles=python_top["data"]['children']

# most_upvoted=max(python_top_articles, lambda x : x['data']['ups'])
# most_upvoted=max(x['data']['ups'] for x in python_top_articles)
max=0
for i in python_top_articles:
    if max<i['data']['ups']:
        max=i['data']['ups']
        l=i
most_upvoted=l['data']['id']    

## 4. Getting Post Comments ##

import json

# Create a dictionary of headers containing our Authorization header.
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}



response = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers=headers)


comments=response.json()


## 5. Getting the Most Upvoted Comment ##

comments_list=comments[1]['data']['children']
s=json.dumps(comments)
maxa=0
for i in comments_list:
    print(i['data']['ups'])
    if maxa< i['data']['ups']:

        maxa=i['data']['ups']
        maxi=i['data']['id']
most_upvoted_comment=maxi

## 6. Upvoting a Comment ##

import json

# Create a dictionary of headers containing our Authorization header.
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
payload = {"dir": 1, "id": "d16y4ry"}
# requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers=headers)
params={"id":"t1_d16y4ry","dir":"1"};
response = requests.post("https://oauth.reddit.com/api/vote", headers=headers,json=payload)

status=response.status_code