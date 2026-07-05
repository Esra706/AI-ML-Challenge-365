#Methods in Dictionary
student = {"name": "Isra", "age": 22, "field": "CS"}

# .keys() - returns all keys
print("Keys:", student.keys())

# .values() - returns all values
print("Values:", student.values())

# .items() - returns key-value pairs
print("Items:", student.items())

# .get() - safe way to access a value
print("Get name:", student.get("name"))
print("Get grade (not exists):", student.get("grade"))            # None
print("Get grade with default:", student.get("grade", "N/A"))     # N/A

# Difference between [] and .get()
print("\n--- Why .get() is safer ---")
print("Using .get():", student.get("grade", "Not Found"))  # safe, no crash

# student["grade"]   # this would crash with KeyError since 'grade' doesn't exist