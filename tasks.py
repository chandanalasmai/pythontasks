#task4
name = input("Enter your name: ")
age = input("Enter your age: ")
department = input("Enter your department: ")
print("\n--- User Details ---")
print("Name:", name)
print("Age:", age)
print("Department:", department)

#task5

age = input("Enter your age: ")
print("Before conversion:")
print("Value:", age)
print("Datatype:", type(age))
age = int(age)
print("\nAfter conversion:")
print("Value:", age)
print("Datatype:", type(age))

#task6


age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")