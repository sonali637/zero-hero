org_list = [8,7,6,5,4,3,2,1]
rever_list = []
for i in org_list:
    rever_list = [i] + rever_list
print(rever_list)

# another way
def reverse_num(n):
    rev_num=[]
    while n > 0:
        digit = n % 10
        rev_num = (rev_num * 10) + digit
        n = n // 10
    return rev_num

