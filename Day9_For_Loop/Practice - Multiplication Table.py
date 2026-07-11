
num = 5

print(f"Multiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Bonus: print tables for multiple numbers using nested loop
print("\n--- Tables from 1 to 3 ---")
for num in range(1, 4):
    print(f"\nTable of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Bonus: using enumerate to number the output
print("\n--- Numbered output using enumerate ---")
table_of = 7
results = [table_of * i for i in range(1, 11)]
for index, result in enumerate(results, start=1):
    print(f"Step {index}: {table_of} x {index} = {result}")