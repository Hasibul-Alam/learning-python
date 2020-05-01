import json

data = '''
{
    "name" : "Hasibul",
    "phone" : {
      "type" : "intl",
      "number" : "+880 1732 184996"
    },
    "email" : {
      "hide" : "Yes"
    }
}'''

info = json.loads(data)
print("Name:", info["name"])
print("Hide:", info["email"]["hide"])
