"""Check whether a year is a leap year or not. """

"""Leap Year Rules:
It is divisible by 4
BUT not divisible by 100,
UNLESS it is also divisible by 400."""

# num=int(input("enter any number : "))
# if num%4 ==0 and num%400==0 or num%100!=0:
#     print("number is leap year ")
# else:
#     print("number is not leap year ")


""" Check if a number is a multiple of 5 or 3."""

# num=int(input("enter any number :-"))
# if num%3==0 and num%5==0:
#     print("number is divide by 5 and 3 ")

# elif num%3==0 :
#     print("number is multiple of  3 ")
# elif(num%5==0):

#     print("number is multiple of 5 ")
# else:
#     print("not multiple of 5 and 3 ")

"""Input a character and check if it is a vowel or consonant. """
# input=input("enter any character :-")
# if input=="a" or input=="e" or input=="i" or input=="o" or input=="u":
    
#     print("value is vowel")
# else:
#     print("value is consonent ")




#                Medium Level 

"""Input marks and print the grade:
90-100: A
75-89: B
60-74: C
<60: D """        

# input=int(input("enter a marks :="))
# if input>=90 and input<=100:
#     print("GRADE A")
# elif(input>=75 and input<=89):
#     print("GRADE B")
# elif(input>=60 and input<=74):
#     print("GRADE C ")
# elif(input<60):
#     print("GRADE D")


"""Take three numbers and print the smallest one."""
# num1=int(input("enter the num1 "))
# num2=int(input("enter the num2 "))
# num3=int(input("enter the num3 "))
# if num1>num2 or num1>num3:
#     print("num1 is greter ")
# elif(num2>num2 or num2>num3):
#     print("num2 is greter")
# elif(num3>num1 or num3>num2 ):
#     print("num3 is greter ")

"""Real-world: Discount Calculator

If purchase > ₹1000, give 10% discount
If > ₹500, give 5%
Otherwise, no discount"""

purchase=int(input("enter a number :-"))
if purchase >1000:
    discount=10/100*purchase
    print(f"10% discount is {purchase-discount}")
elif(purchase >500):
    discount=5/100*purchase
    print(f"5% discount is {purchase-discount}")
else:
    print("no discount")
