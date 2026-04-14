import string
import math

def get_character_pool(password):
    pool = 0

    if any(c.islower() for c in password):
        pool += 26

    if any(c.isupper() for c in password):
        pool += 26

    if any(c.isdigit() for c in password):
        pool += 10

    if any(c in string.punctuation for c in password):
        pool += 32

    return pool

def calculate_strength(password, pool):
    if pool == 0:
        return 0

    return len(password) * math.log2(pool)

def estimate_time(strength):
    guesses_per_second = 1e9
    guesses = 2 ** strength
    seconds = guesses / guesses_per_second

    return seconds

def format_time(seconds):
    if seconds < 60:
        return "less than a minute"
    if seconds < 3600:
        return "a few minutes"
    if seconds < 86400:
        return "a few hours"
    if seconds < 31536000:
        return "a few days"
    return "a long time (years+)"

password = input("Enter a password: ")

pool = get_character_pool(password)
strength = calculate_strength(password, pool)
time = estimate_time(strength)

print("Strength score:", round(strength, 2))

if strength < 30:
    print("Rating: Weak")
elif strength < 50:
    print("Rating: Medium")
else:
    print("Rating: Strong")

print("Estimated time to crack:", format_time(time))