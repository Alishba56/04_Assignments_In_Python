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

def main():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    if login(email, password):
        print("Login successful!")
    else:
        print("Invalid email or password.")

if __name__ == "__main__":
    main()
