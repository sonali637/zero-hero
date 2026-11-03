def third_largest_element(arr):
    n = len(arr)
    larg = 1
    senlar = 1
    thirlar = 1

    for i in range(n):
        if arr[i] > larg:
            larg = arr[i]
    for i in range(n):
            if arr[i] != larg and arr[i] >senlar:
                senlar = arr[i]
    for i in range(n):
            if  arr[i] != larg and arr[i] != senlar and arr[i] > thirlar:
                thirlar = arr[i]
    return thirlar

arr = [56,98,63,58,65,852,4568]      
print(third_largest_element(arr))                   