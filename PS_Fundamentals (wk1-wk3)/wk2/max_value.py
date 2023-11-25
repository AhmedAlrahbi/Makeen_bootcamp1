#ICA_21112023, first number to be > 100
result = []
while True:
    x = input("""
'Q' to quit
'max' to calc max value
Enter a number: """)
    if(x!="Q" and x!="max"):
        result.append(x)
        print(result)
    elif (x=="max"):
        for i in result:
            if int(i) > 100:
                print(result.index(i), "position")
                print(i, end = " \n")
                break
    else:
        exit(result)

