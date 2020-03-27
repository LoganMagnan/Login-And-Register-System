username = input("Enter a username: ")
password = input("Enter a password: ")
email = input("Enter an email: ")
age = input("Enter your age: ")

print("Congratulations! You have successfully created an account on our application!")

register_and_login_system = open("database.txt", "a")

username1 = register_and_login_system.write("\nUsername: " + username)
password1 = register_and_login_system.write("\nPassword: " + password)
email1 = register_and_login_system.write("\nEmail: " + email)
age1 = register_and_login_system.write("\nAge: " + age)

register_and_login_system.close()

print("Login:")

login_username = input("Username: ")
login_password = input("Password: ")

if login_username == username and login_password == password:
    print("Congratulations! You have successfully logged in on our application!")
else:
    print("You have entered invalid credentials.")


