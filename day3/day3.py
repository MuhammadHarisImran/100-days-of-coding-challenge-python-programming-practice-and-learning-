#so its day 3 and we are learing about control flow

number = int(input("please enter a number = "))

if number / 2 == 0:
    print("the entered number is even")
else:
    print("the number is odd")

#this task was to get familiar with if else statements in python

#<================ Task 2 =================>
height = float(input("please enter your height in meters :"))
weight = float(input("please enter your weight in kilograms :"))

BMI = weight / height ** 2

if BMI < 18.5:
    print("your are underweight")
elif BMI <=25:
    print("your weight is normal")
elif BMI <=30:
    print("you are overweight")
elif BMI <=35:
    print("you are obese")
elif BMI > 35:
    print("you are in danger")

print("this is the main code")