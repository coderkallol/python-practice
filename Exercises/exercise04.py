# =========================
# IF STATEMENTS
# =========================

# Example 1
name = "Kallol"  # it should match
if name == "Kallol":
    print("Enter your last name:")
    lastname = "Mandal"
    print("Hello Mr.", lastname)
    print("Nice to meet you,", name)

# Example 2
user_name = "Kallol"
if user_name == "Kallol":
    print("Welcome user,", user_name)
else:
    print("Name doesn't match")

# Example 3
user_name = "Kallol"
if user_name == "Kallol":
    print("Hey", user_name)
    print("Nice to meet you")
else:
    print("Hello")

# Example 4 (Age check)
b = int(input("Enter your age: "))
if b >= 18:
    print("Welcome back Kallol")
elif 18 > b >= 2:
    print("You are very young")
else:
    print("You are not eligible")

# =========================
# WHILE LOOP STATEMENTS
# =========================

# Example 1
i = 1
while i <= 3:
    print("Learn Python")
    i += 1

# Example 2
a = 10
while a >= 5:
    print("Welcome")
    a -= 1

# =========================
# BREAK STATEMENTS
# =========================

name = "Kallol"
while True:
    user_input = input("Enter your name: ")
    if user_input == name:
        print("Thank you")
        break
    print("Invalid name, try again")

# =========================
# CONTINUE STATEMENTS
# =========================

# Example 1
i = 0
while True:
    print(i)
    i += 1
    if i == 15:
        break
    continue

# Example 2
i = 0
while True:
    i += 1
    print(i, end=" ")
    if i == 15:
        break

# =========================
# WHILE LOOP WITH INPUT VALIDATION
# =========================

# Example 1
while True:
    name = input("Enter your name: ")
    if name != "Kallol":
        print("Invalid name, please enter your correct name")
        continue

    age = int(input("Enter your age: "))
    if age <= 20:
        print("Invalid age")
        continue

    break

print("Welcome to Python")

# Example 2
while True:
    name = input("Enter your name: ")
    if name != "Kallol":
        print("Invalid name, please enter your correct name")
        continue

    age = int(input("Enter your age: "))
    if age >= 20:
        print("Thanks")
        break
    else:
        print("Invalid data")

print("Welcome to Python")