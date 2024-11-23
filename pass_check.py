import re

def check_strength(password):
    # Check criteria
    length = len(password) >= 12
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_number = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Count the criteria met
    score = sum([length, has_upper, has_lower, has_number, has_special])
    
    # Determine strength
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    # Suggestions
    tips = []
    if not length:
        tips.append("- Use at least 12 characters.")
    if not has_upper:
        tips.append("- Add an uppercase letter.")
    if not has_lower:
        tips.append("- Add a lowercase letter.")
    if not has_number:
        tips.append("- Include a number.")
    if not has_special:
        tips.append("- Use a special character (!@#$%^&* etc.).")
    
    return strength, tips

# Main program
if __name__ == "__main__":
    print("🔐 Welcome to the Password Checker!")
    pwd = input("Enter your password: ")
    strength, tips = check_strength(pwd)
    
    print(f"\nPassword Strength: {strength}")
    if tips:
        print("Tips to improve your password:")
        for tip in tips:
            print(tip)
    else:
        print("✅ Great job! Your password is strong.")
