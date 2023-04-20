def password(string):
    if len(string) >= 8:
        if hasNumber(string):
            if hasUpper(string):
                if hasLower(string):
                    return True
    return False

def hasNumber(string):
    for char in string:
        if char.isnumeric():
            return True
    return False

def hasUpper(string):
    for char in string:
        if char.isupper():
            return True
    return False

def hasLower(string):
    for char in string:
        if char.islower():
            return True
    return False