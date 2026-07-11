
fruits = ["apple", "banana", "mango"]

# Old way - using range(len())
print("--- Old way (range + len) ---")
for i in range(len(fruits)):
    print(i, fruits[i])

# Better way - using enumerate()
print("\n--- Better way (enumerate) ---")
for i, fruit in enumerate(fruits):
    print(i, fruit)

# enumerate() with custom start index
print("\n--- enumerate() starting from 1 ---")
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

# enumerate() with a string
print("\n--- enumerate() with a string ---")
for i, letter in enumerate("Isra"):
    print(i, letter)