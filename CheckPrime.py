def checkprime(num):
   for i in range(2,num):
       if (num % i) == 0:
           return False
   return True


num = int(input("Enter a number: "))

Prime = checkprime(num)

if Prime:
   print('Your number is a Prime')
else:
   print('Your number is not a Prime')
