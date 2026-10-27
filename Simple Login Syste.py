print("===== LOGIN SYSTEM =====")

correct_username = "vania"
correct_password = "python123"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful! Welcome. ")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts

        if remaining > 0:
            print("Incorrect details.")
            print("Attempts remaining:", remaining)
        else:
            print("Account temporarily locked.")