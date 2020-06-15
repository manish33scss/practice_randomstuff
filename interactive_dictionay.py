"""
Created on Mon Jun 15 18:45:24 2020

@author: manish kumar
"""


import json
from difflib import SequenceMatcher as sm
from  difflib import get_close_matches as matches
 

with open (r"D:\Tutorials\New folder\08 Application 1 Building an Interactive Dictionary\data.json") as f:
    data = json.load(f)


input_word = input(" Enter a Word.. ")

print(input_word)

def meaning(word):
    word=word.lower()
    if word in data:
        
        output = data[word]
        return output
    elif len(matches(word,data.keys())) > 0:
        
       
        yn = input("did you mean %s instead ?? _______ enter Y if yes, or no N if not    " % matches(word, data.keys()) [0] )
        print(yn)
        if yn == "y" :
            
            return data[matches(word, data.keys())[0]]
        elif yn == 'n':
            print("no match found")
            
        else: return "We dont understand the entry !!!"
    else: 
        return "word doesn't exist++double check it.."
  
output=   meaning(input_word)

if type(output) == list:
    for i in output:
        print(i)
        
