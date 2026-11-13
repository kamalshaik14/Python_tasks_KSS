#6.Given a list `[1, 2, 3, 2, 4, 1, 5, 3]`, remove duplicate elements while preserving the original order. Do not use `set()`.


numbers = [1,2,3,2,4,1,5,3]        # Original list


uniqe_numbers = []                #empty list


for i in numbers:               #check each number in original list
    

    if i not in uniqe_numbers:        # Add it only if it is not already in the new list
        uniqe_numbers.append(i)


print(uniqe_numbers)    #print list without duplicates
