# Taken from mission Acceptable Password I
def is_acceptable_password(password: str) -> bool:
    cond1 = len(password) > 6
    cond2 = any(char.isdigit() for char in password)
    cond3 = any(char.isalpha() for char in password)
    if len(password) > 9:  # cond4
        cond2 = cond3 = True
    cond5 = 'password' not in password.lower()

    return all([cond1, cond2, cond3, cond5])


# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
assert is_acceptable_password("password12345") == False
assert is_acceptable_password("PASSWORD12345") == False
assert is_acceptable_password("pass1234word") == True
