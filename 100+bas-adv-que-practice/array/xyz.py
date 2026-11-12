# # Here i  am gone do coding practice all DSA problem again and again
# # 1.second largest element
# def sec_largest_element(arr):
#     n = len(arr)
#     largest = 1
#     seclargest = 1
#     for i in range(n):
#         if arr[i] > largest:
#             largest = arr[i]
#     for i in range(n):
#         if arr[i] != largest and arr[i] > seclargest:
#             seclargest = arr[i]
#     return seclargest
# arr = [12,56,89,5,69]
# print(sec_largest_element(arr))               

# # 2.third largest element
# def sec_largest_element(arr):
#     n = len(arr)
#     largest = 1
#     seclargest = 1
#     thirdlargest =1
#     for i in range(n):
#         if arr[i] > largest:
#             largest = arr[i]
#     for i in range(n):
#         if arr[i] != largest and arr[i] > seclargest:
#             seclargest = arr[i]
#     for i in range(n):
#         if arr[i] != largest and arr[i] != seclargest and arr[i] > thirdlargest:
#             thirdlargest = arr[i]        
#     return thirdlargest
# arr = [12,56,89,5,69]
# print(sec_largest_element(arr)) 

# # 3. Reverse array
# # using function
# def reverse_array(arr):
#     k = arr[::-1]
#     return k
# arr = [10,9,8,7,6,5,4,3,2,1]
# print(reverse_array(arr))

# # 4. reverse with out using functions
# first_part = [10,9,8,7,6,5,4,3,2,1]
# reversed_part = []

# for i in first_part:
#     reversed_part = [i] + reversed_part
# print(reversed_part)    

# # reverse only first k element
# def reverse_first_element(arr, k):
#     first_part= arr[:k]
#     first_part = first_part[::-1]
#     reverse_part = arr[k:]
#     return first_part + reverse_part
# arr = [10,9,8,7,6,5,4,3,2,1]
# k = 3
# print(reverse_first_element(arr, k))

# # reverse array with out usig new list
# arr = [1,2,3,4,5]
# start = 0
# end = 4
# while start<end:
#     temp = arr[start]
#     arr[start] = arr[end]
#     arr[end] = temp
#     start = start + 1
#     end = end - 1 
# print(arr)       

# second largest element
# def second_largest(arr):
#     n = len(arr)
#     largest = 1
#     seclarg = 1
#     for i in range(n):
#         if arr[i] > largest:
#             largest = arr[i]
#     for i in range(n):
#         if arr[i] != largest and arr[i] > seclarg:
#             seclarg = arr[i]
#     return seclarg
# arr = [10,30,40,50,60,90]                
# print(second_largest(arr))

# reverse the array using built in function
# def reverse_arr(arr):
#     k = arr[::-1]
#     return k
# arr = [1,2,3,4,5]
# k = 2
# print(reverse_arr(arr))

# reverse array with out using new list
# arr = [1,2,3,4,5]
# start = 0
# end = 4
# while start<end:
#     temp = arr[start]
#     arr[start] = arr[end]
#     arr[end] = temp   
#     start = start + 1
#     end = end - 1  
# print(arr)        

# # palindrom number
# arr = [1,2,3,2,1]
# revers_arr = arr[::-1]
# if arr == revers_arr:
#     print(True)
# else:
#     print(False)    

# # revers only 1st k element
# def reverse_fist_k_element(arr, k):
#     first_part = arr[:k]
#     first_part = arr[::-1]
#     sec_part = arr[k:]
#     return first_part + sec_part
# arr = [1,2,3,4,5,6,7,8,9]
# k = 3
# print(reverse_fist_k_element(arr, k))

# reverse arr with out using function
# original_array = [4,5,9,8,6]
# reversed_array = []
# for i in original_array:
#     reversed_array = [i] + reversed_array
# print(reversed_array)    

# mpve zeros to end
# def move_zero(arr):
#     l = 0
#     for r in range(len(arr)):
#         if arr[r]:
#          arr[l],arr[r] = arr[r],arr[l]
#          l += 1
#     return arr
# arr = [1,0,2,0,6,0,6,3,0,0]
# print(move_zero(arr))    

# # reverse array
# def reverse_arr(arr):
#     l = 0
#     r = len(arr) - 1
#     while l < r:
#         arr[l],arr[r] = arr[r],arr[l]
#         l = +1
#         r = -1
#     return arr
# arr = [1,2,3,4,5,6]
# print(reverse_arr(arr))       

# concadination
def concad(num):
    n = len(num)
    ans = [0] * (2*n)
    for i in range(n):
        ans[i] = num[i]
        ans[i+n] = num[i]
    return ans
num = [1,2,3,4]
print(concad(num))    
