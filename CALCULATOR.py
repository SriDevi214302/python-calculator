def calculator(a,b,user_input):
    if user_input=="add":
        return a+b
    elif user_input=="sub":
        return a-b 
    elif user_input=="mul":
        return a*b 
    elif user_input=="div":
        if a!=0 and b!=0:
          return a/b
        else:
            return "INVALID OPERATION"
    else:
        return "NO INPUT"

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
while True:

   
    user_input=input("ENTER THE OPERATION YOU WANT(add,sub,mul,div):")
    final_result=calculator(a,b,user_input)
    print("Final Result is:",final_result)

    choice=input("Enter if you wan tto perform another operation(yes/no):")
    if choice.lower()=="yes":
        print("CALCULATOR CLOSED")
        break



