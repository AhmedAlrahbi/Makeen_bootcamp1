#ICA, 30112023
def binary_Search(listSorted, key):
    listSorted.sort()
    li = 0
    hi = len(listSorted)- 1
    while(li<=hi):
        mid = int((li + hi)/2)
        if (listSorted[mid] == key):
            print(f"You've found {listSorted} at {mid}")
            break
        elif (listSorted[mid]< key):
            li = mid + 1

        else:
            hi = mid - 1
    else:
        print ('Not found')
binary_Search([10,50,20,70,80,40,30], 80)

