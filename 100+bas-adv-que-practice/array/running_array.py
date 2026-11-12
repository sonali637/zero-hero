def running_arr(num):
    n = len(num)
    for i in range(1,n):
        num[i] += num[i -1]
    return num
num = [1,2,3,4,5]
print(running_arr(num))    