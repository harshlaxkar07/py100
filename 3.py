
print("#swap 1 using tuple unpacking")
a = 11
b = 21
print(f"before swap a: {a} , b: {b} ")  
b,a = a, b 
print(f"after swap a: {a} , b: {b} \n")  

print("#swap 2 using temp variable")
a = 12 
b = 22
print(f"before swap a: {a} , b: {b} ")  
temp = a 
b = a
a = temp    
print(f"after swap a: {a} , b: {b} \n")  

print("# swap 3 using arithmetic operations")
a = 13
b = 23 
print(f"before swap a: {a} , b: {b} ")
a = a + b   
b = a - b
a = a - b   
print(f"after swap a: {a} , b: {b} \n")

print("# swap 4 using bitwise XOR")
a = 14
b = 24
print(f"before swap a: {a} , b: {b} ")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"after swap a: {a} , b: {b} \n")

print("# swap 5 using multiplication and division")
a = 15
b = 25
print(f"before swap a: {a} , b: {b} ")
a = a * b
b = a // b
a = a // b
print(f"after swap a: {a} , b: {b} \n")

print("# swap 6 using Python's built-in function")
a = 16          
b = 26
print(f"before swap a: {a} , b: {b} ")
a, b = divmod(a * b, b)  # Using divmod to swap
print(f"after swap a: {a} , b: {b} \n")