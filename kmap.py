''' This program devloped by Nirdesh Tiwari'''
''' Minor project first year'''
print("This is Two variale k -map. Sum of product finder")
print("Enter it's all positions")
def check(x):
 n = 0
 while n <= 16 :
    if x == "0000" :
          print("x = 0")
          break
    elif x == "0001" :
          print("x = ab")
          break
    elif x == "0010"  :
          print("x = ab' ")
          break
    elif x == "0011" :
          print("x = a ")
          break
    elif x == "0100":
           print("x = a'b ")
           break
    elif x == "0101" :
          print("x = b")
          break
    elif x == "0110" :
          print("x = a'b+ab' ")
          break
    elif x == "0111" :
          print("x = a + b ")
          break
    elif x == "1000" :
          print("x = a'b' ")
          break
    elif x == "1001" :
          print("x = a'b'+ab ")
          break
    elif x == "1010" :
          print("x = b' ")       
          break
    elif x == "1011" :
          print("x = a +b' ")  
          break
    elif x == "1100" :
          print("x = a' ") 
          break
    elif x == "1101" :
          print("x = a'+b ")
          break
    elif x == "1110" :
          print("x = a'+b' ")
          break
    elif x == "1111" :
          print("x = 1 ")
          break  
    
    n = n + 1
n = 0
while n <= 16 :
    
    a = str(input("position 0 : "))
    b = str(input("position 1 : "))
    c = str(input("position 2 : "))
    d = str(input("position 3 : "))
    x = a+b+c+d
    check(x)
    n = n+1
    
 
