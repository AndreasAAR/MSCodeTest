import webbrowser

'''
Auth: Andreas Ährlund-Richter
Using algorithm theorized to solve code-test at Multisoft
proposed at Codeproject.com by Richard Deeming

Calculator will calculate with tokens given by tokenizer and output answer
'''

#Calc number of rows in the database "Vacation" COUNT(*), its "C" in the formula in " The Tests and Background "

#We use the example call
# EXEC dbo.ObscureProcedure @i = 406
#That gives
'''
ObscureCount
------------
2947105
(1 row(s) affected)
'''
#We know that anything not @i < 245   will be 245 times the @i parameter.
#ELSE COUNT(*) * 245

class Calculator:

    def __init__(self, tokenizer):
        self.fixedNum = tokenizer.getFixed()
        self.iteratorVal = tokenizer.getIterator()
        self.testInput = tokenizer.getTestInput()
        self.iterLimit = tokenizer.getIterlimit()
        self.testResult = tokenizer.getTestResult()

    def calculate(self):
        print(self.testResult)
        print(self.fixedNum)

        rowCount =  int(self.testResult)/int(self.fixedNum)

        #Now we have to figure out the actual calculation of the for loop.
        #our end variable
        sum = 0
        #The iterations in the loop
        iters = int(self.iteratorVal)-1
        iterLimit = int(self.iterLimit)-1
        if iters > iterLimit :
            iters = iterLimit
        print("iterations " + str(iters))

        fixedNum = int(self.fixedNum)

        for i in range(iters+1):
            #print(i)
            if i < fixedNum:
                sum += rowCount*i
            if i >= fixedNum:
                sum += rowCount*fixedNum

        htmlTestVariabel = "TESTTEXT"
        html_str = """<html>
          <head></head>
          <body>
            <p>Tack för att du använde kodtestlösaren.<br>
               Lägg in det här på testsidan:<br>
               <br><br><h1>{code}</h1><br>
               <img src="http://domain.com/footer.jpg">
            </p>
          </body>
        </html>
        """.format(code=int(sum))

        htmlPath = "answer.html"

        Html_file = open(htmlPath, "w")
        Html_file.write(html_str)
        Html_file.close()
        webbrowser.open('file://'+ "/Users/AAR/Dropbox/Andreas/PLUGG_JOBB/VT2020/Jobbsök/Test/MSCodeTest/answer.html")

        print("Answer: ")
        print(sum)