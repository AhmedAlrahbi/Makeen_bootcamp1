#assign3, Q2
def index_of_smallest_element(my_list):
    print(my_list)
    smallest_index = 0
    for i in range(1, len(my_list)):
        if my_list[i] < my_list[smallest_index]:
            smallest_index = i
    return smallest_index
my_list = []
for j in range(10):
    element = int(input("Enter the elements of the list: "))
    my_list.append(element)

result = index_of_smallest_element(my_list)
print(f"The index of the smallest element is: {result}")
