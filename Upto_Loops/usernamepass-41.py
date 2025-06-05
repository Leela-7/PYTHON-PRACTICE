correct_username = "admin"
correct_password = "password123"

entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

if entered_username == correct_username:
    print("Username accepted.")
    if entered_password == correct_password:
        print("Password accepted. Login successful!")
    else:
        print("Incorrect password. Access denied.")
else:
    print("Incorrect username. Access denied.")

print("--- End of login attempt ---")