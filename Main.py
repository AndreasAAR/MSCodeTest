'''
Auth: Andreas Ährlund-Richter
Using algorithm theorized to solve code-test at Multisoft
proposed at Codeproject.com by Richard Deeming
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
fixedNum = 245 #Its the number in the SQL statement for ELSE
rowCount =  2947105/fixedNum
rowCount = rowCount
print("rowcount " + str(rowCount))

#Now we have to figure out the actual calculation of the for loop.

#our end variable
sum = 0
#The iterations in the loop
iters = 835-1
iterLimit = 597-1
if iters > iterLimit :
    iters = iterLimit
print("iterations " + str(iters))



for i in range(iters+1):
    print(i)
    if i < fixedNum:
        sum += rowCount*i
    if i >= fixedNum:
        sum += rowCount*fixedNum


print(sum)