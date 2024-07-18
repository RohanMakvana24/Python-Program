operation = input("Enter Operation + , - , * , /")
a=2
b=3
match operation:
 case '+' :
  print("The addition is " , a+b)
 case '-':
  print("The subtarction is " , a-b)
 case '*':
  print("The multiplication is " , a*b)
 case '/':
  print("The division is " , a/b)
 case _ :
  print("Somenthing Went Wrong");
