def sumList(numList):
    sumOfList = 0
    for i in numList:
        sumOfList += i
    return sumOfList

def productList(numList):
    if len(numList) == 0:
        return 0
    elif len(numList) == 1:
        return numList[0]
    else:
        productOfList = 1
        for i in numList:
            productOfList *= i
        return productOfList

testList = [ 1, 2 ,3 ,4 ,5]

print(productList(testList))

