#POTD_15112023, Merged sorted lists
def merge_sorted_lists(arr1, arr2):
    i = len(arr1) - 1
    j = len(arr2) - 1
    merged_index = len(arr1) + len(arr2) - 1

    arr1 += [0] * len(arr2) #since we are required to not use any space.

    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[merged_index] = arr1[i]
            i -= 1 #will put it in a decrement way from right to left if element is larger on arr1
        else:
            arr1[merged_index] = arr2[j]
            j -= 1 #same here if larger
        merged_index -= 1

    while j >= 0: #remainings after comparison from the first loop
        arr1[merged_index] = arr2[j]
        j -= 1
        merged_index -= 1

#Note: the user have to provide a ->SORTED<- list in both inputs.
input_1 = input("Enter sorted list 1 (comma-separated): ")
input_2 = input("Enter sorted list 2 (comma-separated): ")
#we need to change it to int so we can do the comparison on the if
arr1 = [int(x) for x in input_1.split(',')]
arr2 = [int(x) for x in input_2.split(',')]


merge_sorted_lists(arr1, arr2)
print("Merged and ordered list: ")
for num in arr1[:-1]: #without last element since we adding comma
    print(num, end=", ")
print(arr1[-1]) #last element without comma

