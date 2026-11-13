#A number is a Palindrome if it reads the same forward and backward. 


number = input("enter the number:")

if number == number[::-1]:
   
    print("is a palindrome")

else:
    print("is not a palindrom")
