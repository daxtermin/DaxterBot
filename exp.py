import json

json_data1 = '''{
    "error": "False",
    "category": "Pun",
    "type": "twopart",
    "setup": "A Roman walks into a bar and raises 2 fingers and says to the bartender...",
    "delivery": "Five beers, please.",
    "flags": {
        "nsfw": "False",
        "religious": "False",
        "political": "False",
        "racist": "False",
        "sexist": "False",
        "explicit": "False"
    },
    "safe": "True",
    "id": 286,
    "lang": "en"
}'''
parsed = json.loads(json_data1)
print(parsed['setup']+"\n"+parsed['delivery'])

json_data2 = '''
{
  "error": "False",
  "category": "Programming",
  "type": "single",
  "joke": "Java and C were telling jokes. It was C's turn, so he writes something on the wall, points to it and says 'Do you get the reference?' But Java didn't.",
  "flags": {
    "nsfw": "False",
    "religious": "False",
    "political": "False",
    "racist": "False",
    "sexist": "False",
    "explicit": "False"
  },
  "id": 4,
  "safe": "Turn",
  "lang": "en"
}'''
parsed = json.loads(json_data2)
print(parsed['joke'])
