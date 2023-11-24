def to_print():
        print("Choice an option:")
        print("1. Add task.")
        print("2. Finish task.")
        print("3. Remove pendig task.")
        print("4. View pending tasks.")
        print("5. View completed tasks.")
        print("6. View all")
        print("7. Exit")


def main():
    
    pending = []
    done = []
    
    print("---------------WELCOME---------------")
    while (True):
        to_print()
        n = int(input("Type 1, 2, 3, 4, 5, 6 or 7:\n"))
        if n == 1:
            pending.append(input("Write a task:"))
        elif n == 2:
            task = input("What task you finished?")
            if task in pending:
                pending.remove(task)
                done.append(task)
            else:
                print("We don't find this task.")
        elif n == 3:
            task = input("Write a pending task to remove:")
            if task in pending:
                pending.remove(task)
            else:
                print("We don't find this task.")
        elif n == 4:
            print("Pending tasks:")
            for item in pending:
                print(item)
        elif n == 5:
            print("Done tasks:")
            for item in done:
                print(item)
        elif n == 6:
            print("Pending tasks")
            for item in pending:
                print(item)
            print("Done tasks:")
            for item in done:
                print(item)
        elif n == 7:
            break
        else:
            print("Write a valide number!")
if __name__ == "__main__":
    main()