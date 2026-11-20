arr = [16, 17, 4, 3, 5, 2]
ans=[]
grater = arr[-1]
for i in reversed(arr):
    if i >= grater:
        grater = i
        ans.append(i)
print(ans[::-1])        