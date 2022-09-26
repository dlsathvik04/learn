import requests
import json

#An API that does not exist 
#.................................................................................................
response = requests.get('http://api.open-notify.org/doesnotexist')
print(response.status_code)


#getting a json response from an api that does not require any authentication and processing it  
#.................................................................................................
response = requests.get('http://api.open-notify.org/iss-now.json')
print(response.status_code)
print((response.json())["iss_position"])

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
jprint(response.json())


#getting a json response from an api that does not require any authentication but need parameters
#.................................................................................................
response = requests.get('http://api.open-notify.org/iss-now.json')
print(response.status_code)
print((response.json())["iss_position"])

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
jprint(response.json())


#getting a response from an api that requires authentication and processing it  
#.................................................................................................