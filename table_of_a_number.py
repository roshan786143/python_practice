print("python program to print Table of a number using while loop")
table_of_a_number=int(input("Enter the number you wish to get it's table : "))
i=0
while(i<10):
    i=i+1
    result=table_of_a_number*i
    #i=i+1
    print(table_of_a_number,"x",i,"=",result)
    print("---------------------------------")



print("python program to print Table of a number using for loop")
table_of_a_number=int(input("Enter the number you wish to get it's table : "))
i=0
for i in range (11):
    result=table_of_a_number*i
    print(table_of_a_number,"x",i,"=",result)
