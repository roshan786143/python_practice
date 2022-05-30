print("python program to print Square pattern")
n=int(input("Enter the desired number to get it's square pattern : "))
for x in range(0,n):
    for y in range(0,x+1):
        print("* ",end="")
    print("")
