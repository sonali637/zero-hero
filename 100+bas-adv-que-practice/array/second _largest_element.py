def Sec_larg(arr):
    n = len(arr)
    largest = -1
    secLarg = -1
    for i in range(n):
     if arr[i] > largest:
        largest = arr[i]
    for i in range(n):
     if  arr[i]!= largest and arr[i] > secLarg:
        secLarg = arr[i]        
    return secLarg
arr = [12,53,82,94,88]       
print(Sec_larg(arr))
