def sec_small_element(arr):
    n = len(arr)
    smallest = 1000
    secSmall = 1000

    for i in range(n):
        if arr[i] < smallest:
            smallest = arr[i]
    for i in range(n):
        if arr[i] != smallest and arr[i] < secSmall:
            secSmall = arr[i]
    return secSmall
arr = [9,5,2,4,8,1,-20,-53]
print(sec_small_element(arr))                
