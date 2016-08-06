from config import fbAppName,fbAppID,fbAppSecret,apiV,accessToken
import urllib.request
import json
import pprint
pp = pprint.PrettyPrinter(indent=2, compact=True)

# query_string = "https://graph.facebook.com/" + apiV + "/me/photos?" + "access_token=" + accessToken
query_string = "https://graph.facebook.com/" + apiV + "/me/photos?" + "access_token=" + accessToken

response = urllib.request.urlopen(query_string)

print("Response :",response.getcode())
if response.getcode() == 200:
	response = json.loads(response.read().decode('utf8'))

	# pp.pprint(response)
	firstPhoto = response['data'][0]
	print(firstPhoto['id'])
	print(firstPhoto['name'])
	print(firstPhoto['created_time'])

	query_string = "https://graph.facebook.com/" + apiV + "/"+firstPhoto['id']+"?fields=name,link,created_time,height,width,can_tag,from,images" + "&access_token=" + accessToken
	print(query_string)
	# "https://graph.facebook.com/v2.7/1023227637761944?fields=link&access_token=EAADZADLacQioBAKRjZAZCKgRA19i3wWwQh0AM11sTulfKuuHGOnEqAFl0up52rmLiVDZCN0kOM1mCyEPN3xvZCWn6kWWa90uVM5eO4hegmvLxzm4ZCU7ju0DG9DhAfUYAnpPK8V0ZC4UA2nxIo73asexmr0sZBHpe8gOi3WXgDIIAgZDZD"
	photo_response = urllib.request.urlopen(query_string)
	print("Response :",photo_response.getcode())
	if photo_response.getcode() == 200:
		photo_response = json.loads(photo_response.read().decode('utf8'))

		print(photo_response['name'])
		print(photo_response['link'])
		print(photo_response['created_time'])
		print(photo_response['height'])
		print(photo_response['width'])
		print(photo_response['can_tag'])
		print(photo_response['from'])
		print(photo_response['images'])
