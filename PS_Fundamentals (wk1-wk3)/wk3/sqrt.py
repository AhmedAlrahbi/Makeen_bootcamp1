#ICA
   
   # using lists
# def sqrt_find(x):
#     listSqrt =[]
#
#     for i in range (x):
#         exp = i**2
#         if (exp <=x):
#             listSqrt.append(exp)
#     print(listSqrt)
#     hi = len(listSqrt) - 1
#     print(hi)
#
# sqrt_find(x)
def sqrt_find(x):
    li = 0
    hi = x
    while (li <= hi):
        mid = int((li + hi) / 2)
        if (mid * mid == x):
            print(mid)
            break
        elif(mid * mid < x):
            li = mid + 1
        else:
            hi = mid - 1
    else:
        print ("Answer is Float")
opt = input("""Enter any value to start:
 ('stop' to Quit): """)

while (opt != "stop"):
    try:
      inputX = int(input('Enter a number: '))
      assert inputX >= 0
      sqrt_find(inputX)
    except AssertionError :
      print("Number is negative, try again.")
    except ValueError:
        print("You entered a string")
