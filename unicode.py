import unicodedata
import sys
import json
#import os
allItems = []
def UnicodeLookup(char):
    for i in range(0x110000):
        character = chr(i)
        name = unicodedata.name(character, "")
        if ''+char.upper() in f"{name}":
            item = {"Icon": "char", "Title": f"{character}", "Subtitle": f"{name}"}
            allItems.append(item)
    json_string = json.dumps(allItems)
    #jsonDumpPath = os.getcwd()[:-14]+"\JSON data\chars.json"
    #with open(jsonDumpPath, 'w') as file:
     #   file.write(json_string)
    print(json_string)

UnicodeLookup(sys.argv[1])
