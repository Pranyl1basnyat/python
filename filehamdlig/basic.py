with open("student.txt","a") as f:
    n=int(input("How many records do you wamt to add "))
    for i in range(1,n):
         name=str(input("Enter the name of the student "))
         age=int(input("Enter the age of the student "))
         grade=str(input("Enter the grade of the student "))
         address=str(input("Enter the address  of the student "))
         math=int(input("Enter the marks of  the maht "))
         f.write(f"{name},{age},{grade},{address},{math}\n")
    f.close()
    
    
