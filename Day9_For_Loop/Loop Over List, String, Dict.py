"""
Day 9: Looping Over List, String, and Dict
"""

# Loop over a list
print("--- Looping over a list ---")
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# Loop over a string
print("\n--- Looping over a string ---")
for letter in "Isra":
    print(letter)

# Loop over a dict - keys only
print("\n--- Looping over dict keys ---")
student = {"name": "Isra", "age": 22, "field": "CS"}
for key in student:
    print(key)

# Loop over dict values
print("\n--- Looping over dict values ---")
for value in student.values():
    print(value)

# Loop over dict items (key + value together)
print("\n--- Looping over dict items ---")
for key, value in student.items():
    print(f"{key}: {value}")