from logic import TruthTable

ans1 = str(input("Please enter a proposition using the variables p and q: "))
ans2 = str(input("please enter a different proposition using p and q: "))

myTable = TruthTable(["p", "q"], [ans1, ans2])
myTable.display()

myTableList = myTable.table
t=1
for i in range(0,len(myTableList)):
    if(myTableList[i][1][0] == myTableList[i][1][1]):
        t=t*1
    else:
        t=t*0
        break 
if(t==1):
    print("The propositions are equivalent")
else:
     print("The propositions are not equivalent")
    
