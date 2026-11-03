def sec_larg_element_with_out_using_sort_and_max(arr):
    larg = -1
    seclar = -1

    for i in range(len(arr)):
        if arr[i] > larg:
            larg = arr[i]
            
    for i in range(len(arr)):
        if arr[i] != larg and arr[i] > seclar:
            seclar = arr[i]
    return seclar

print(sec_larg_element_with_out_using_sort_and_max([56,63,69,89,85,1,2,5,6]))
                
                   