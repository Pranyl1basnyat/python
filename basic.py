# write  the program that print "hello world " and  your name 
print("Hellow world ");
print("My name is pranil basnet i want to be the  multibillionaire ");

# Create the simple calculator that adds , subtract ,multiplies and add two numbers.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

add=a+b
subtract=a-b
multiply=a*b
divide=a/b
print("The sum of the two number is:",add)
print("The difference of the two number is:",subtract)
print("The product of the two number is:",multiply)
print("The division of the two number is:",divide)


# Write a program that calculate your age in days,hour and minute 

age=int(input("Enter your age:"))
age_in_days=age*365
age_in_hours=age*365*24
age_in_minutes=age*365*24*60
age_in_second=age*365*24*60*60

print("Your age in days is:",age_in_days)
print("Your age in hours is:",age_in_hours)
print("Your age in minute is:",age_in_minutes)
print("Your age in second is:",age_in_second)

# Convert the temperature  and celsius and fahrenheit 

# Converting the celsius to fahrenheit 
F=int(input("Enter the temperature in celsius:"))
c=5/9*(F-32)
print("The temperature in celsius is:",c)

# to change the fahrenheit to celsius 
C=int(input("Enter the temperature in fahrenheit:"))
f=9/5*C+32
print("The temperature in fahrenheit is:",f)

# Write the program to check wheather the given is even or  odd 
n=int(input("Enter the number you want to check the wheathern the given number is even or odd "))
if n  %  2 == 0:
    print("It is the even number")
 

