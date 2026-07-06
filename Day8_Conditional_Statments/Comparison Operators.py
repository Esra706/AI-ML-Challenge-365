
a = 10
b = 5

print("a == b:", a == b)   # False
print("a != b:", a != b)   # True
print("a > b:", a > b)     # True
print("a < b:", a < b)     # False
print("a >= b:", a >= 10)  # True
print("a <= b:", a <= 5)   # False

# Common mistake demo
x = 5
print("\nAssignment vs Comparison:")
print("x =", x)          # assignment - sets value
print("x == 5:", x == 5)  # comparison - checks equality

# Using comparisons in conditions
score = 85
if score == 100:
    print("Perfect score!")
elif score >= 80:
    print("Great score!")
else:
    print("Keep improving!")