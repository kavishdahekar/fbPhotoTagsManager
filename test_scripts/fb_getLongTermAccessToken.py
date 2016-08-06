from config import fbAppName,fbAppID,fbAppSecret,apiV,accessToken,makeAPICall

# "https://graph.facebook.com/oauth/access_token?client_id={APP_ID}&client_secret={APP_SECRET}&grant_type=fb_exchange_token&fb_exchange_token={EXISTING_ACCESS_TOKEN}"
query_string = "https://graph.facebook.com/oauth/access_token?client_id="+fbAppID+"&client_secret="+fbAppSecret+"&grant_type=fb_exchange_token&fb_exchange_token="+accessToken

# print(query_string)

result = makeAPICall("","","",query_string)
if result['response_code'] == 200:
	accessToken = result['response'].split("&")[0].split("=")[1]

	with open('long.accessToken','w') as f:
		f.write(accessToken)