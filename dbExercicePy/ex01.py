# Convert the following dictionary into JSON format
import json
data = {"key1" : "value1", "key2" : "value2","key3":"value"}
jsonData=json.dumps(data,indent=2,separators=(",","="))
print(jsonData)