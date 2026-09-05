correctUsername = "python"
correctPassword = "rules"

attempt = 0

while attempt < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correctUsername and password == correctPassword:
        print("Welcome")
        break

    else:
        attempt = attempt + 1
        if attempt < 5:
             print("Incorrect username or password. Please try again.")
        
if attempt == 5:
    print("Access denied")