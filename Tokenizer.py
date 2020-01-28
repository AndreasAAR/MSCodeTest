import re

class Tokenizer:

    def __init__(self, inputArray):
        self.fixedNum = self.fixedGet(inputArray)
        self.testI = self.testIget(inputArray)
        #self.testRes
        #self.iters
        #self.iterLimit


    def fixedGet(self,inputArray):
         testPattern = "(ELSE COUNT\(\*\) \* )\d* END"
         return  self.getToken(testPattern,inputArray)

    def testIget(self,inputArray):
         testPattern = "\< \d*\; i\+\+\)"
         return  self.getToken(testPattern,inputArray)


    def getToken(self, pattern, inputArray):
        token =""
        for i in inputArray:
            test = re.search(pattern, i)
            if not isinstance(test, type(None)):
                digits = "[0-9]+"
                token = re.search(digits, test.group()).group()
                break
        return token

    def getFixed(self):
        return self.fixedNum

    def getTestI(self):
        return self.testI