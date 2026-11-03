arr = [1,2,3,4,5,6]
start = 0
end = 5
while start < end :
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

    start = start +1
    end = end - 1
print(arr)