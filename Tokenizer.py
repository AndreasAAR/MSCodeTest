''''
Tokenizer takes multi-line input (ctrl+a of entire site with problem,
extracts whats needed for solving the code problem
'''

import re

class Tokenizer:

    def __init__(self, inputArray):
        self.fixedNum = self.setter(inputArray, "(ELSE COUNT\(\*\) \* )\d* END")
        self.iteratorVal = self.setter(inputArray, "\< \d*\; i\+\+\)")
        self.testInput = self.setter(inputArray, "EXEC dbo.ObscureProcedure @i = \d+")
        self.iterLimit = self.setter(inputArray, "WHERE @i < \d*")
        self.testResult= self.setter(inputArray, "^\d+$")
        #self.iters


    def setter(self,inputArray,pattern):
        return self.getToken(pattern, inputArray)

    def getToken(self, pattern, inputArray):
        token = 0
        digits = "[0-9]+"
        for i in inputArray:
            test = re.search(pattern, i)
            if not isinstance(test, type(None)):
                if not isinstance(re.search(digits, test.group()) , type(None)):
                    token = re.search(digits, test.group()).group()
                break
        if token == 0:
            print("WARNING: there is likely an error!")
        return token

    def getFixed(self):
        return self.fixedNum

    def getIterator(self):
        return self.iteratorVal

    def getTestInput(self):
        return self.testInput

    def getIterlimit(self):
        return self.iterLimit

    def getTestResult(self):
        return self.testResult