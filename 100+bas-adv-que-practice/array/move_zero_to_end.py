def move_zero(arr):
    l = 0
    for r in range(len(arr)):
        if arr [r]:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
    return arr
arr =[1,0,5,0,0,0,3,4,9]
print(move_zero(arr))        