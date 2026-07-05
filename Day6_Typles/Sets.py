

# Creating a set - duplicates are automatically removed
fruits = {"apple", "banana", "apple", "mango", "banana"}
print("Fruits set (duplicates removed):", fruits)

# Converting a list to a set to remove duplicates
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print("Unique numbers:", unique_numbers)

# Set operations - real example: class students
class_A = {"Ali", "Sara", "Bilal", "Isra", "Ahmed"}
class_B = {"Isra", "Ahmed", "Zara", "Hamza"}

print("\nClass A:", class_A)
print("Class B:", class_B)

print("Union (all students combined):", class_A | class_B)
print("Intersection (common students):", class_A & class_B)
print("Only in A (A - B):", class_A - class_B)
print("Only in B (B - A):", class_B - class_A)
print("Symmetric difference (in only one class):", class_A ^ class_B)

# Fast lookup - O(1) check
print("\nIs 'Isra' in Class A?", "Isra" in class_A)