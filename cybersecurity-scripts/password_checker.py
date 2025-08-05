import re

def check_password_strength(password):
    if len(password) < 8:
        return "❌ Password too short (min 8 characters)."
    
    if not re.search(r"[A-Z]", password):
        return "❌ Add at least one uppercase letter."
    
    if not re.search(r"[a-z]", password):
        return "❌ Add at least one lowercase letter."
    
    if not re.search(r"\d", password):
        return "❌ Add at least one digit."
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "❌ Add at least one special character."

    return "✅ Password is strong!"

# --------- Run it ---------
password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
