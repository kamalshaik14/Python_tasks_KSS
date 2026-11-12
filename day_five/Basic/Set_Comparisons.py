# 8.Common Elements Using Sets: Given two lists:

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
 

#convert to sets

set1=set(list1)
set2=set(list2)

# Common elements.

print("common:",set1 & set2)


# Elements present only in the first list.

print("only in the frist:",set1-set2)

# All unique elements from both lists. 

print("unique elements:",set1 | set2)
