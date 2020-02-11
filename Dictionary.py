import json
from difflib import get_close_matches

data=json.load(open("data.json"))



def translate(w):
    w=w.lower()
    if w in data:
          return data[w]
    elif w.upper() in data:
          return data[w.upper()]
    elif w.title() in data:
          return data[w.title()]
    elif len(get_close_matches(w,data.keys()))>0:
         yn= input("Did you mean %s instead? Press Y if yes or N: " %get_close_matches(w,data.keys())[0])
         if yn == 'Y':
             return data[get_close_matches(w,data.keys())[0]]
         elif yn == "N":
             return "The word is not exist!! Please check it again."
         else:
          return "We didn't understand your query"
    else:

        return "The word is not exist!! Please check it again."
          



word=input("Enter the word: ")

output=(translate(word))
if type(output) == list:
     for item in output:
         print(item)
else:
     print(output)
