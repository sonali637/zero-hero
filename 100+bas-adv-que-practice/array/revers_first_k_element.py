def reverse_first_k_element(arr, k):
    first_part = arr [:k]
    first_part = first_part[::-1]
    second_part = arr[k:]
    return first_part + second_part

arr = [1,2,3,4,5]
k = 3
print(reverse_first_k_element(arr, k))