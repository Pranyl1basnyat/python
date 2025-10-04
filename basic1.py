# Write the program in the python to calcualte the  sum of all the memebers of the  list
#list  in the python
#A built in data types that stores set of values
# it can store element of different types (integer,float ,string etc)
"""
arks1=94.5
marks2=87
marks3=95.6 #to ignore this we have  the list 

#to implememt these we have the list 
marks=[94.5,95.2,87,84,72]
print(marks)

print(marks[0])
print(marks[1])
print(len(marks))

# It can store the elements of the differernt types (integer,float ,string)

#list [2,1,3]
# list .append(4) add one element at the end 
#list.sort()# sort in the ascending order 
#list.sort(reverse=True) sorts in the ascending order b
#list.reverse() reverse  the list 
#list.insert(idx,el)  insert element at index 

marks=[99,97,96,95,94]
marks.append(88)
marks.sort()
marks.sort(reverse=True)#sorts in descending order 
marks.reverse()
print(marks)
print(marks.sort(reverse=True))




# program to find the sum of  the element of the list
total=[55,56,57,58,59,60]
a= sum(total)
print("sum:",a)



#loops are used to execute a blocks of code repeatedly based
# on a condition ort sequence 
 there are two types of loop in the python they are 
for loop 
while loop

Syntax  of the for loop
for variable in Sequence 



fruits=["apple","banana","cherry","orange","mango"]
for fruit in fruits:
    print(fruit)
    

i=1
for i in range(100):
    print(i)

    while loop 
    The while loop continue to execute as long as a condition is 
    true 

    Syntax:
    while condition:
        block of the code to execute







    

    #write the program to determine  wheather an input number is even or odd 
n=int(input("Enter the number you want to check"))
if n%2==0 :
    print("it is the even number")
else:
        print("it is not divisible")
        

        # Write the program to input the any number and print whether it is positive .negative or zero

n= int(input("Enter the number you want to check"))
if n>0 :
    print("It is the positive number ")
elif n==0:
    print("It is the null number")
else:
    print("it is the  negative number")


Question no 3: 
Write the program to calculate the simple interest and total amount where principal amount time
and rate  should be fed by the user while programmme is being executed ,keep the option for more entries 


p=float(input("Enter the principal"))
t=float(input("Enter the time ") )
r= float(input("Enter the rate "))
i= p*t*r/100
print(i)


question no 4: Write a program to input the cost price and selling price of an item 
the program should find the whether the seller  had made profit orincured loss and also
find how much profit he made or loss incured 

cp= int(input("Enter the costprice b of the product"))
sp=int(input("Enter the selling price of the product"))
profit= sp-cp
loss=cp-sp
if sp>cp :
    print( "The profit  that the seller make:",profit)
else:
    print("The loss that the seller make:",loss)
"""






























