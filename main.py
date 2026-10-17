print("Welcome to Git Practice!")

name = input("Enter your name: ")
print(f"Hello, {name}!")

tasks = ["Learn Git", "Practice GitHub", "Push code"]

print("\nMy learning tasks:")
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")

print("I am learning Git commands in VS Code!")