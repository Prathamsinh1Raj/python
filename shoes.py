import json
#read the shoes data from the json file
with open ('ab.json') as file:
    shoes_data=json.load(file)
    #print shoes data
    print(shoes_data)