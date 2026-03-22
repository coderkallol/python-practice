# -------- input() Function --------
print("What is your name?")
name = input()
print("My name is", name + ".")


# -------- len() Function --------
print("Length of 'Kallol' is:", len("Kallol"))


# -------- Type Conversion --------
print("I am", str(29), "years old.")

print(int(34))        # Output: 34
print(int(34.85))     # Output: 34

print(float(3.15))    # Output: 3.15
print(float(10))      # Output: 10.0


# -------- Age Example --------
print("What is your age?")
age = input()

next_age = int(age) + 1
print("You will be", str(next_age), "in next year.")