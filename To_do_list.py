def show_choices():
    print("|-----To Do List-----|")
    print("1. Show The Tasks")
    print("2. Assign tasks")
    print("3. Delete tasks")
    print("4. Exit")
    print("---------------------|")

def main():

    tasks = []

    while True:
        show_choices()
        user_choice = input("What do you want to do? (1-4)\n")
        if user_choice.isdigit():
            choice = int(user_choice)
        else:
            print("Incorrect, choose between (1-4)\n")

        if choice == 1:

            if not tasks:
                print("Bro nothing is in tasks! Like lock in!!\n")

            else:
                print("These are your tasks:\n")
                for index, elements in enumerate(tasks, start = 1):
                    print(f"{index}. {elements}\n")

        elif choice == 2:
            new_task = input("What task do you want to add\n")

            if new_task:
                tasks.append(new_task)
                print(f"{new_task} has been added\n")
            else:
                print("Bro actually add things\n")

        elif choice == 3:
            if not tasks:
                print("Nothing in tasks to delete\n")
                continue

            print("------Tasks Currently Assigned------\n")
            for index, elements in enumerate(tasks, start = 1):
                    print(f"{index}.{elements}\n")

            try:
                delete_task = int(input("Which task do you want to delete?\n"))

                if 1 <= delete_task <= len(tasks):
                    removed = tasks.pop(delete_task - 1)
                    print(f"{removed} has been deleted\n")
                else:
                    print("Incorrect tasks number\n")
            except ValueError:
                print("Enter a valid number\n")

        elif choice == 4:
            print("thanks for caring bri\n")
            break


if __name__ == "__main__":
    main()
