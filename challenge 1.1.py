# Python 3 program to find
# factorial of given number 
def factorical(n):

  if (n==0 or n==1):
    return 1
  else:
    return n * factorical(n - 1)
num=5
r=factorical(num)
print("Factorical of {} is {} .".format(num,r))
    
    