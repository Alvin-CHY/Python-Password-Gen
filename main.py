import math
import string

def calculate_pool(password):
    pool = 0

    if any(c.islower() for c in password):
        pool += 26

    if any(c.isupper() for c in password):
        pool += 26

    if any(c.isdigit() for c in password):
        pool += 10

    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)

    return pool

def entropy(password, pool):
    if pool == 0:
        return 0
    return len(password) * math.log2(pool)

def crack(entropy_value):
    guesses_per_second = 1e9
    total_guesses = 2 ** entropy_value
    return total_guesses / guesses_per_second

def time(seconds):
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365

    if seconds < 60:
        return f"{seconds:.2f} seconds"
    if minutes < 60:
        return f"{minutes:.2f} minutes"
    if hours < 24:
        return f"{hours:.2f} hours"
    if days < 365:
        return f"{days:.2f} days"
    return f"{years:.2f} years"

def strength(entropy_value):
    if entropy_value < 28:
        return "Very Weak"
    elif entropy_value < 36:
        return "Weak"
    elif entropy_value < 60:
        return "Moderate"
    elif entropy_value < 128:
        return "Strong"
    else:
        return "Very Strong"

password = input("Enter a password: ")

pool = calculate_pool(password)
ent = entropy(password, pool)
time_to_crack = crack(ent)

print("Entropy:", round(ent, 2), "bits")
print("Strength:", strength(ent))
print("Estimated crack time:", time(time_to_crack))