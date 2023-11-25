#ICA_21112023, dice roll statistics program
sides = []
n=""
while True:
    n = input("""type 'stop' to stop
Enter the throw result : """)
    if(n!="stop"):
        sides.append(int(n))
    elif(n=="stop"):
        break

y = int(input("How many sides your dice have? "))
counter = [0]*y
def countInputs(sides):
    for num in sides:
        counter[num-1]+=1
    return counter
def printCounters(counter):
    for i in range (len(counter)):
        print(i+1, end = f": {counter[i]}\n")
        


def main():
    x = countInputs(sides)
    printCounters(x)
    
main()