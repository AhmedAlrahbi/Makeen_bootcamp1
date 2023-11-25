#ICA, 20112023 grading system
def gradeSys(keyAns):
    fixAns = keyAns
    index = 0
    grade = 0
    sumGrade = 0
    numStu = int(input("Enter number of student : "))
    num = 1
    for j in range (1, numStu +1):
        stuAns = input(f"Enter the  5 mc answers (a,b,c) for student {num}: ")
        valid = len(stuAns) == 6
        for i in range (0,len(stuAns)):
            valid = (stuAns[i] == fixAns[i])
            if valid:
                grade += 1
        print(f"The grade for student {num} is : ", grade)

        num+=1
        sumGrade+=grade
        grade = 0
    avg = sumGrade/numStu
    print("Students average: ", avg)
def main():
    gradeSys(input("Enter the answer key : "))
main()