arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        print("This is i", i)
        cur_index = i
        smallest_index = cur_index
        # print(cur_index)
    
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range (i+1, len(arr)):
            if arr[smallest_index] > arr[x]:
                print("X value inside nested loop", x)
                smallest_index = x
            
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
           

    print(arr)

        # TO-DO: swap

    return arr

selection_sort(arr)
print(arr)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range (len(arr)):
        print("This is i", i)
        for j in range(0, len(arr) - i - 1):
            print("This is j", j)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


