import json

data = '''
[
    {
      "id" : "001",
      "x" : "2",
      "name" : "Hasibul"
    },
    {
      "id" : "007",
      "x" : "3",
      "name" : "Hasinur"
    }
]'''

info = json.loads(data)
print('User Count;',len(info))

for item in info:
    print('Name:',item["name"])
    print('Attriute:',item["x"])
    print('ID:',item["id"])
