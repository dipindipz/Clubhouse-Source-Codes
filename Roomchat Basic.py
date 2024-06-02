import requests

api = "https://www.clubhouseapi.com/api/"

url = api + "send_channel_message"

# Fill in the channel ID and message
channel_id = "your_channel_id"
message = "Your message here"

# Fill in your user token
usertoken = "your_user_token"

data = {
    "channel": channel_id,
    "message": message
}

headers = {"Authorization": "Token " + usertoken}

response = requests.post(url, headers=headers, json=data)
print(response.text)
