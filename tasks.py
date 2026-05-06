#task4
#name = input("Enter your name: ")
#age = input("Enter your age: ")
#department = input("Enter your department: ")
#print("\n--- User Details ---")
#print("Name:", name)
#print("Age:", age)
#print("Department:", department)

#task5

#age = input("Enter your age: ")
#print("Before conversion:")
#print("Value:", age)
#print("Datatype:", type(age))
#age = int(age)
#print("\nAfter conversion:")
#print("Value:", age)
#print("Datatype:", type(age))

#task6


#age = int(input("Enter your age: "))
#if age >= 18:
    #print("Eligible")
#else:
    #print("Not Eligible")








a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
a += b
print("After += :", a)
a -= b
print("After -= :", a)
a *= b
print("After *= :", a)
a /= b
print("After /= :", a)
a %= b
print("After %= :", a)
a //= b
print("After //= :", a)
a **= b
print("After **= :", a)


age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
if age >= 18 and marks >= 50:
    print("Eligible")
else:
    print("Not Eligible")
if age < 18 or marks < 50:
    print("Not Eligible (using OR condition)")
else:
    print("Eligible (using OR condition)")
if not(age >= 18 and marks >= 50):
    print("Condition reversed using NOT: Not Eligible")
else:
    print("Condition reversed using NOT: Eligible")



num = int(input("Enter a number: "))
print("AND with 5:", num & 5)  
# AND compares bits of both numbers and it sets bit to 0 if any one bit is 0
print("OR with 3:", num | 3)  
# OR compares bits of bot numbers and it sets bit to 1 if any one bit is 1
print("XOR with 2:", num ^ 2)  
# XOR sets bit to 1 if bits are different
print("Left Shift by 2:", num << 2)  
# shifts bits to left (multiplies by 2^2)
print("Right Shift by 1:", num >> 1)  
# shifts bits to right (divides by 2)
print("NOT:", ~num)  
# gives negative value (-(num+1))
