print("---------------------------Welcome to instagram-------------------------")
#while(True):
for x in range(3,-1,-1):
    user_name=input("Enter your username : ")
    pass_word=input("Enter your password : ")
    if(user_name=="roshan" and pass_word=="roshan"):
        print("access granted")
        print("hello",user_name,"welcome to instagram :)")
        break
    else:
        print("access denied")
        print("you have only",x,"attempts left")
        continue
#print("our systems detected an unauthorised access from your account,so your account has been temporarily blocked")

