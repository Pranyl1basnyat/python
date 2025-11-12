def average(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg

average(10,20,30)

"""
Functions in python 
Built in function 
print()
len()
type()
range()
built function are those function which is already
defined in python
    user defined function
def func_name(param1, param2):

"""
#Write a program to print the length of the list 

list1=[10,20,30,40,50]
print(len(list1))
print(type(list1))  
print(range(10))


  # WAP to print the element of a list in a
  #  single line of code
  #  list=[10,20,30,40,50]
  #  output:10 20 30 40 50

list=[10,20,30,40,50]
for i in list:
    print(i,end=" ")
print() # by default end with \n    
 
 print("Nischal is the don of the tokha")