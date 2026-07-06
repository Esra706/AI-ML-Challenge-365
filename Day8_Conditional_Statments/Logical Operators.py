

age = 20
has_id = True

# and - both conditions must be true
if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

# or - at least one condition must be true
temperature = 5
if temperature < 10 or temperature > 40:
    print("Extreme weather warning")
else:
    print("Normal weather")

# not - reverses the condition
is_raining = False
if not is_raining:
    print("No umbrella needed")

# Combining multiple logical operators
marks = 85
attendance = 90

if marks >= 80 and attendance >= 75:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")