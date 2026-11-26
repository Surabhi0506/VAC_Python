age = 15

try:
    if age < 18:
        raise ValueError("You must be 18 or older")
    print("Eligible")
except ValueError as e:
    print("You must be 18 or older")
else:
    print("Access granted")
print("Program completed")