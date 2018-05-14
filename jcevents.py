import requests

url = "https://events.jumpcloud.com/events"

payload = "startDate=2018-02-08T00:00:00Z&endDate=2018-02-08T23:00:00Z"
headers = {
    'x-api-key': "7bbdb89ce3419ddf28444e98673d237a733abd9b",
    'content-type': "application/json",
    }

response = requests.request("GET", url, params=payload, headers=headers)

print(response.text)


curl -G -H "x-api-key: 7bbdb89ce3419ddf28444e98673d237a733abd9b" -H "Content-Type:application/json" --data-urlencode "startDate=2018-02-20T00:00:00Z" --data-urlencode "endDate=2018-02-21T00:00:00Z" https://events.jumpcloud.com/events | python -m json.tool
