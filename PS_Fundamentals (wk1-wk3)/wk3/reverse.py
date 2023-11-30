#ICA, 26112023, Reversing end multiplication result
lst =[]
result = []
#Fun1
entry = int(input("Enter length of the list : "))
def readFloats():
    for i in range(0, entry):
        ele = float(input(f"enter the {i+1} number: "))
        lst.append(ele)
    return lst
def multi10(lst):
    for j in range(0, entry):
        eleRes = lst[j] * 10
        result.append(eleRes)
    return result
def printReversed(result):
    revResult = result
    revResult.reverse()
    print(revResult)
def main():
    readFloats()
    multi10(lst)
    printReversed(result)
main()
