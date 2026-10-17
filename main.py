print("Welcome to Git Practice!")

name = input("Enter your name: ")
print(f"Hello, {name}!")

tasks = ["Learn Git", "Practice GitHub", "Push code"]

print("\nMy learning tasks:")
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")

print("I am learning Git commands in VS Code!")

def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful!"
    return "Invalid username or password"


print(login("admin", "1234"))