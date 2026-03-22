# ==============================
# THE LIST DATA TYPE
# ==============================

print(1, 2, 3)

name = ['Kallol', 'Rahul', 'Sayan', 'Deep']
print(name[1])
# print(name[2.01])  # Error: index must be integer

print(name[int(2.0)])
print('Hello, ' + name[0])


# ==============================
# NESTED LISTS
# ==============================

spam = [['cat', 'dog'], ['rahul', 'rahim']]

print(spam[0])
print(spam[1][0])


# ==============================
# LIST SLICING
# ==============================

spam = ['cat', 'dog', 'lion', 'elephant']

print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])
print(spam[::2])
print(spam[1:])
print(spam[:])


# ==============================
# LIST LENGTH
# ==============================

spam = ['cat', 'dog', 'moose']
print(len(spam))


# ==============================
# MODIFYING LIST VALUES
# ==============================

spam = ['cat', 'bat', 'rat', 'elephant']

spam[1] = 'aardvark'
print(spam)

spam[2] = spam[1]
print(spam)

spam[-1] = 12345
print(spam)


# ==============================
# LIST CONCATENATION & REPLICATION
# ==============================

print([1, 2, 3] + ['A', 'B', 'C'])
print(['X', 'Y', 'Z'] * 3)

spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)


# ==============================
# FOR LOOPS WITH LISTS
# ==============================

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


# ==============================
# IN / NOT IN OPERATORS
# ==============================

print('howdy' in ['hello', 'hi', 'howdy', 'heya', 'yes'])

spam = ['hello', 'hi', 'howdy', 'heya']
print('cat' in spam)
print('howdy' not in spam)
print('cat' not in spam)


# ==============================
# SIMPLE PROGRAM (INPUT CHECK)
# ==============================

myPets = ['Zophie', 'Pooka', 'Fat-tail']

print('Enter a pet name:')
name = input()

if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')