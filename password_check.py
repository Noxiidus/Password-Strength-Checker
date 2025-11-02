import re

password = input("Enter password: ")

score = 0
if len(password) >= 8:
    score += 1
if re.search(r"\d", password):
    score += 1
if re.search(r"[A-Z]", password):
    score += 1
if re.search(r"[a-z]", password):
    score += 1
if re.search(r"\W", password):
    score += 1

strength = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
print(f"Password strength: {strength[score]}")
