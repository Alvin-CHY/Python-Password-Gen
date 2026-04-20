import math
import string
import random

def analyze(passwordList):
    lowerCase = False
    upperCase = False
    digit = False
    symbol = False

    for c in passwordList:
        if c.islower():
            lowerCase = True
        elif c.isupper():
            upperCase = True
        elif c.isdigit():
            digit = True
        elif c in string.punctuation:
            symbol = True

    pool = 0
    if lowerCase:
        pool += 26
    if upperCase:
        pool += 26
    if digit:
        pool += 10
    if symbol:
        pool += len(string.punctuation)

    if pool == 0:
        entropy = 0
    else:
        entropy = len(passwordList) * math.log2(pool)

    guesses = 2 ** entropy
    seconds = guesses / 1e9

    return entropy, seconds

def timeEstimate(seconds):
    if seconds < 60:
        return str(round(seconds, 2)) + " seconds"
    minutes = seconds / 60
    if minutes < 60:
        return str(round(minutes, 2)) + " minutes"
    hours = minutes / 60
    if hours < 24:
        return str(round(hours, 2)) + " hours"
    days = hours / 24
    if days < 365:
        return str(round(days, 2)) + " days"
    years = days / 365
    return str(round(years, 2)) + " years"

def strength(entropy):
    if entropy < 28:
        return "Very Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Moderate"
    elif entropy < 128:
        return "Strong"
    else:
        return "Very Strong"

def generatePassword(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    result = ""
    for i in range(length):
        result += random.choice(chars)
    return result

choice = input("Type 1 to check password. Type 2 to generate: ")

if choice == "2":
    length = int(input("Enter length: "))
    password = generatePassword(length)
    print("Generated password:", password)
else:
    password = input("Enter a password: ")

passwordList = list(password)

entropy, seconds = analyze(passwordList)

print("Entropy:", round(entropy, 2), "bits")
print("Strength:", strength(entropy))
print("Estimated crack time:", timeEstimate(seconds))