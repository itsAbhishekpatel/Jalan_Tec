
# function which return the array in order of Max value follow by min value 
def maxMin(arr):
    n = len(arr)

    # variale to store index of first and last element 
    small, large = 0, n-1
    flag = True #flag variable

    # temp array of original size of array
    temp = n*[None]

    for i in range(n):
        if flag is True:
            temp[i] = input[large]
            large -= 1

        else:
            temp[i] = input[small]
            small += 1
        flag = bool(1-flag)

    # copy temp array to original array
    for i in range(n):
        input[i] = temp[i]
    
    return input 

# customized input 
input = [10,50,110,120,200]

print(f"Input Array: {input}\n")
print(f"Result: {maxMin(input)}")

