#8. Write a program to find the second largest number in a list.







num = [10,20,30,60,50,50,60,90,80,70,]

num1=sorted(set(num))
second_largest_num=num1[-2]
print("second largest:",second_largest_num)
