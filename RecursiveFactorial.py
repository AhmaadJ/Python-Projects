import random;

def main():
   number = random.randint(0, 9)
   print(number , " ! " , end='') 
   print(factorial(number))      

def factorial(n):
   if n == 1:
      return n
   else:
      return n*factorial(n-1)
main() 