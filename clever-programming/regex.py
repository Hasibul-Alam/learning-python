import re

text = '''Random string. halambd7@gmail.com,
        some random text.
        hasibul.alam.01@utrgv.edu'''

pattern =  re.compile('[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+')

result = pattern.findall(text)
print(result)
