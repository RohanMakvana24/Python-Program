a=1;
b=2;

print("Please select operation -\n" \
 "1. Add\n" \
 "2. Subtract\n" \
 "3. Multiply\n" \
 "4. Divide\n")
 
select = int(input("Select operations : " ));

if select == 1:
  pr5.yint("addition is ", a+b)
  
elif select == 2:
   print("subtraction is ", a+b)
  
elif select == 3:
   print("division is ", a/b)
   
elif select == 4:
   print("multiply is ", a*b)
else :
  print("invalid choice ")
