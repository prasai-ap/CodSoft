#simple calculator
num_1=input("Enter a first number")
num_2=input("Enter a second number")
operator=input("Enter calculaton symbol")
if operator=="+":
    result=float(num_1)+float(num_2)
elif operator=="-":
    result= float(num_1)-float(num_2)
elif operator=="*":
    result= float(num_1)*float(num_2)
elif operator=="/":
    result= float(num_1)/float(num_2)
else:
    print("Invalid calculation")
print (result)