from config import fbAppName,fbAppID,fbAppSecret,apiV,accessToken,makeAPICall
import urllib.request
import json
import pprint
pp = pprint.PrettyPrinter(indent=2, compact=True)

# query_string = "https://graph.facebook.com/" + apiV + "/me/photos?" + "access_token=" + accessToken
# response = urllib.request.urlopen(query_string)

result = makeAPICall("me","photos")

if result["response_code"] == 200:

	firstPhoto = result['response']['data'][0]
	print("id :" , firstPhoto['id'])
	print("name :" , firstPhoto['name'])
	print("created_time :" , firstPhoto['created_time'])

	# query_string = "https://graph.facebook.com/" + apiV + "/"+firstPhoto['id']+"?fields=name,link,created_time,height,width,can_tag,from,images" + "&access_token=" + accessToken
	photo_result = makeAPICall(firstPhoto['id'], "", "name,link,created_time,height,width,can_tag,from,images")

	if photo_result['response_code'] == 200:

		print("name :" , photo_result['response']['name'])
		print("link :" , photo_result['response']['link'])
		print("created_time :" , photo_result['response']['created_time'])
		print("height :" , photo_result['response']['height'])
		print("width :" , photo_result['response']['width'])
		print("can_tag :" , photo_result['response']['can_tag'])
		print("from :" , photo_result['response']['from'])
		print("images :" , photo_result['response']['images'])
