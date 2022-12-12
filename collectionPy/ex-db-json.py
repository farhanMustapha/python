import json
data="""{
    "key1":"value1",
    "key2":"value2",
    "key3":"value3"
}"""

jsonData=json.loads(data)
print(jsonData['key2'])