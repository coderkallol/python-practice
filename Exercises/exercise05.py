# =========================
# FUNCTIONS BASICS
# =========================

def hello():
    print('python')
    print('java')
    print('HTML')

def greet(name):
    print('Nice to meet you,', name)


# =========================
# RETURN VALUES EXAMPLE
# =========================

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


# =========================
# RANDOM NAME FUNCTION
# =========================

def askname(number):
    if number == 1:
        return 'hi , Kallol'
    elif number == 2:
        return 'hi , Sayan'
    elif number == 3:
        return 'hi , Rohit'
    elif number == 4:
        return 'hi , Deep'


# =========================
# MAIN EXECUTION
# =========================

# Call hello function twice
hello()
hello()

# Greeting with names
greet('Kallol')
greet('Python')

# Magic 8-ball style answer
print(getAnswer(random.randint(1, 9)))

# Random name greeting
print(askname(random.randint(1, 4)))