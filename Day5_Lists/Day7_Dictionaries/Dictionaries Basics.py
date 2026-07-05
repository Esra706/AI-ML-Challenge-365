

# Creating a dictionary
student = {
    "name": "Isra",
    "age": 22,
    "field": "Computer Science"
}
print("Student dict:", student)

# Accessing values using keys
print("Name:", student["name"])
print("Age:", student["age"])
print("Field:", student["field"])

# Updating a value
student["age"] = 23
print("Updated age:", student["age"])

# Adding a new key-value pair
student["grade"] = "A"
print("After adding grade:", student)

# Removing a key-value pair
del student["grade"]
print("After removing grade:", student)