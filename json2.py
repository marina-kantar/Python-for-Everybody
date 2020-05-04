import json

input ='''
[
    {
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    } ,
    {
        "id" : "007",
        "x" : "7",
        "name" : "Mark" 
    }
]'''

info = json.loads(input)
print('User count: ', len(info))

for item in info :
    print("Id: ", item["id"])
    print("x: ", item["x"])
    print("Name: ", item["name"])