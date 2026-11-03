def kth_largest(arr,k):
    arr.sort(reverse = True)
    return arr[k-1]

arr =[56,98,35,89,29,59]
k = 2
print(kth_largest(arr, k))