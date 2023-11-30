#ICA
def insertionSort(list_):
    for step in range (1 ,len(list_)):
        key = list_[step]
        j = step -1
        while j >= 0 and key < list_[j]:
            list_[j+1] = list_[j]
            j-=1
        list_[j + 1] = key

data = [14,15,2,9,8]
insertionSort(data)
print(data)