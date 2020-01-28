'''
Main runs the other classes, takes input, and will calculate
'''


import re

#ELSE COUNT(*) * 292 END
from Tokenizer import Tokenizer

testString = "for (int i = 0; i < 891; i++) {"
testPattern = "\< \d*\; i\+\+\)"
test = re.search(testPattern , testString)
print(test)

digits ="[0-9]+"
digits = re.search(digits,test.group()).group()


print(digits)

print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

inputArray = contents
tokenizer = Tokenizer(inputArray)
print(tokenizer.getIterator())
print(tokenizer.getFixed())
print(tokenizer.getTestIterator())