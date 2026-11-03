# 1.second largest element
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

# 2.third largest element
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

# 3. Reverse array
# using function
# def reverse_array(arr):
#     k = arr[::-1]
#     return k
# arr = [10,9,8,7,6,5,4,3,2,1]
# print(reverse_array(arr))

# 4. reverse with out using functions
# first_part = [10,9,8,7,6,5,4,3,2,1]
# reversed_part = []

# for i in first_part:
#     reversed_part = [i] + reversed_part
# print(reversed_part)    

# reverse only first k element
def reverse_first_element(arr, k):
    first_part= arr[:k]
    first_part = first_part[::-1]
    reverse_part = arr[k:]
    return first_part + reverse_part
arr = [10,9,8,7,6,5,4,3,2,1]
k = 3
print(reverse_first_element(arr, k))