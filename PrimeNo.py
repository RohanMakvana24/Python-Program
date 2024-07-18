no =5
f = False
for i in range(2 , no):
   if (no % i) == 0 :
     f=True
     break
     
if f:
  print("not prime number")
else :
  print("prime number ")