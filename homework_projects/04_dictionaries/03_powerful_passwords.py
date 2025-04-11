import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

stored_logins = {
    "user1@example.com": hash_password("password123"),
    "user2@example.com": hash_password("qwerty123"),
    "user3@example.com": hash_password("mypassword")
}

def login(email, password_to_check):
    if email in stored_logins:
        hashed_password_to_check = hash_password(password_to_check)
        if stored_logins[email] == hashed_password_to_check:
            return True
    return False

email = "user1@example.com"
password = "password123"
print(login(email, password))

email = "user2@example.com"
password = "wrongpassword"
print(login(email, password))
