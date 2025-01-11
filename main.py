from weather import get_weather
from todo import add_task, remove_task, view_tasks

def main():
    print("Welcome to your AI Agent!")
    print("Choose an option:")
    while True:
        print("\nOptions:")
        print("1. Get weather information")
        print("2. Add a task to your to-do list")
        print("3. Remove a task from your to-do list")
        print("4. View your to-do list")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            city = input("Enter the name of the city: ").strip()
            print(get_weather(city))
        elif choice == "2":
            task = input("Enter a task to add: ").strip()
            print(add_task(task))
        elif choice == "3":
            task = input("Enter a task to remove: ").strip()
            print(remove_task(task))
        elif choice == "4":
            print(view_tasks())
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
