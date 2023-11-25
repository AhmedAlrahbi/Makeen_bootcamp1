#ICA 20112023, Incremnted numbers and their sums
sum_ = 0
newsum = 0
x = int(input("Enter the number to increment the sum: "))
rep = int(input("How many times u want it to repeat : "))
for i in range(2, rep + 1):
    sum_ += sum_
    sum_ = (f'{x}' * i)
    newsum += int(f'{x}' * i)
    print(sum_[:-1], end = "+")
print (sum_, end =" = ")
print(newsum)