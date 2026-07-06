
#Day 8: Conditionals - if/elif/else Basics

marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Below C")

# Testing with different values
age = 17

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Simple if without elif/else
temperature = 40
if temperature > 35:
    print("It's very hot today!")