#Here u will find answers for problem 2&3 of the assignment 1 20/11/2023
#2. Tuition problem
def tuition():
    tuition = 10000
    inctTuition = 5/100
    year = 1
    addition = 0
    sum_ = 0

    for i in range(1, 15): # num of years
        addition = tuition * inctTuition # give us the increased amount
        tuition += addition # increased amount plus whole tuition

        print(f"Your tuition for year {i}: {tuition}")
        if 11 <= i <= 14: #calc after tenth year total of outputs
            sum_ += tuition

    print("Your total tuition After the 10th year:", sum_)

"""<------------------------------------------------------------------------------------------------>"""

#3. Nested loop arrow
#what we will enter here is log2(128)+1 which will give us '8' jumps till we reach 128
def nestedLoop():
    n = int(input("Enter expo: press 8:"))
    for i in range(1, n + 1): #this will be our rows
        for k in range(1, n - i + 1): #spaces decrease as number increase for good arrow shape
            print("  ", end="    ")
        for j in range(0, i): # this will print first half of the arrow (increasing power)
            print(2 ** j, end="    ")
        for k in range(i - 2, -1, -1): # this will print second half of the arrow (decreasing power)
            print(2 ** k, end="    ")
        print() # new line for each row
choice = 0
def main():
    try:
        choice = int(input("Enter (2 or 3) to view Questions 2&3: "))
        while choice != 0:
            if choice == 2:
                tuition()
            elif choice == 3:
                nestedLoop()
            else:
                print("Wrong choice")
            choice = int(input("Enter (2 or 3) to view Questions 2&3 (or 0 to exit): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
main()



