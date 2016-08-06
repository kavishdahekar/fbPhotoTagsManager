import urllib.request
import json
import os,sys

fbAppName	=	"kndPhotoManager"
fbAppID		=	"238648626528810"
fbAppSecret	=	"fac7ea1588ae117abe769e7db181ddf6"
apiV		=	"v2.7"	# Graph API version

# Access Token
# Permissions : email, user_photos
if os.path.isfile("long.accessToken"):
	tokenFile = "long.accessToken"
elif os.path.isfile("short.accessToken"):
	tokenFile = "short.accessToken"
else:
	print("No access token file found!")
	sys.exit()

with open(tokenFile,'r') as f:
	accessToken = f.read()

def makeAPICall(node,edge = "",fields = "", query_string_param = ""):
	if query_string_param != "":
		query_string = query_string_param
	else:
		query_string = "https://graph.facebook.com/" + apiV + "/"+node + "/" + edge + "/" +"?fields=" + fields + "&access_token=" + accessToken
	
	result = urllib.request.urlopen(query_string)

	if result.getcode() == 200:
		readData = result.read().decode('utf8')
		try:
			retData = json.loads(readData)
		except ValueError as e:
			# invalid json
			return {"response_code" : result.getcode(), "data_type" : "string", "query_string" : query_string, "response" : readData}
		else:
			# valid json
			return {"response_code" : result.getcode(), "data_type" : "json", "query_string" : query_string, "response" : retData}

	else:
		return {"error_code" : result.getcode(), "query_string" : query_string, "response" : result}