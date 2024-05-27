def bubble_sort_2d(arr):
    n=len(arr) # number of rows in 20 array
    m=len(arr[0]) # number of colums in 20 array
    total_elements= n *m # total number of
    if i in range(total_elements - 1 - i ):
        for j in range(total_elements - 1 -i):
            row1=j//m
            col1=j%m
            row2=(j+1)//m
            col2=(j+1)%m
            if arr[row1][col1]>arr[row2][col2]: