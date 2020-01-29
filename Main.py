'''
Main runs the other classes, takes input, and will calculate
'''


import re

#ELSE COUNT(*) * 292 END
from Calculator import Calculator
from Tokenizer import Tokenizer



print("Enter/Paste the content from the webpage(select all with ctrl or cmd + a and copy paste in terminal). \n Ctrl-D or Ctrl-Z ( windows ) to run program it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

inputArray = contents
tokenizer = Tokenizer(inputArray)
calculator = Calculator(tokenizer)
calculator.calculate()

