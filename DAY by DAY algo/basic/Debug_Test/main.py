#user defined function

def calcAddition(left, right):
    sum = left +  right
    return sum

def getLarger(varLeft, varRgiht):
    if (varLeft >= varRgiht) :
        varReturn = varLeft
    else :
        varReturn = varRgiht
    return varReturn

var1 = 3
var2 = 4

var3 = calcAddition(var1, var2)
print("Var3 : ", var3)


var4 = getLarger(var1, var2)
print("Var4 : ", var4)

