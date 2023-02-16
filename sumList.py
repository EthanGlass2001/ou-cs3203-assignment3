
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


def sumList(numList):
    sumOfList = 0
    for i in numList:
        sumOfList += i
    return sumOfList


def reverseList(numList):
    return numList[::-1]



if __name__ == '__main__':
    print("Enter a String of numbers that you want to add together and multiply by a comma (,):")

    userInput = input()
    numList = userInput.split(',')
    numList = [int(i) for i in numList]
    print(sumList(numList))
    print(productList(numList))
    # print(f"The reverse of {numList} is {reverseList(numList)}")

