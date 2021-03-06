#Dude json is just dictionaries and lists, keys and values wow mind blown

#my json doesnt work it gives me errors in my python download folders

#write json in python, key : value


import json
input = ''' [
{ "name" : "Filip",
"phone" : "777-777-7777",
"x" : "8"
} , 
{ "name" : "Jimmy"
"phone" : "555-555-5555",
"x" : "16"
}
]'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('name', item['name'])
    

#I got an error - pretty sure i have the incorrect JSON on my computer


#returns dictionary
#everything in python is dictionary or list

#list of two dictionaries
#json doesnt have attributes

#easy to make and easy to read

#Walmart is service-oriented architecture

#API - we set the rules, link with their API - geocoding

#script for Google maps API pull on Web Services: APIs