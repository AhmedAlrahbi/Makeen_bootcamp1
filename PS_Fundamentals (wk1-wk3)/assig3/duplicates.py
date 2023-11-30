#assign3, Q3
def eliminate_duplicates(lst):

    res = []
    for ele in lst:
        if ele not in res:
            res.append(ele)
    return res

my_list = []
for j in range(10):
    element = int(input("Enter an element: "))
    my_list.append(element)

result = eliminate_duplicates(my_list)
print("The List as follows:", end=" ")
for number in result:
    print(number, end=" ")
