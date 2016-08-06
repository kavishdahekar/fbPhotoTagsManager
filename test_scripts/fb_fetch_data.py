from config import fbAppName,fbAppID,fbAppSecret,apiV,accessToken
import urllib.request
import json

# query_string = "https://graph.facebook.com/" + apiV + "/me/photos?" + "access_token=" + accessToken
query_string = "https://graph.facebook.com/" + apiV + "/me?" + "access_token=" + accessToken

response = urllib.request.urlopen(query_string)

print("Response :",response.getcode())
if response.getcode() == 200:
	response = json.loads(response.read().decode('utf8'))

	print(response['name'])
	print(response['id'])