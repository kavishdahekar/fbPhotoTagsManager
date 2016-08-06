from config import fbAppName,fbAppID,fbAppSecret,apiV,accessToken,makeAPICall

result = makeAPICall("me")
print(result['response_code'])
print(result['response']['name'])
print(result['response']['id'])
print(result['query_string'])