# org_list = [8,7,6,5,4,3,2,1]
# rever_list = []
# for i in org_list:
#     rever_list = [i] + rever_list
# print(rever_list)

# another way
def reverse_num(n):
    revers_arr = []
    for i in n:
        revers_arr = [i] + revers_arr
    return revers_arr
n = [1,2,3,4]
print(reverse_num(n))    
    