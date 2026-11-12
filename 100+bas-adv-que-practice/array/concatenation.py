def concadination(num):
    n = len(num)
    ans = [0] * (2*n)
    for i in range(n):
        ans[i] = num[i]
        ans[i + n] = num[i]
    return ans
num = [1,2,3]
print(concadination(num))     