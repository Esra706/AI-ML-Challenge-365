
# PART 1: TUPLES (Immutable List)

print("===== TUPLES =====")

# Creating a tuple
student = ("Isra", 22, "Computer Science")
print("Student tuple:", student)

# Unpacking - extracting values from a tuple
name, age, field = student
print(f"Name: {name}, Age: {age}, Field: {field}")

# Indexing - same as lists
print("First item:", student[0])
print("Last item:", student[-1])


# Real-life use case: coordinates that should never change
sukkur_location = (27.7052, 68.8574)
print("Sukkur coordinates:", sukkur_location)

# Using a tuple as a dictionary key (a list cannot be used here)
locations = {
    (27.7052, 68.8574): "Sukkur",
    (24.8607, 67.0011): "Karachi"
}
print("Location lookup:", locations[(27.7052, 68.8574)])


