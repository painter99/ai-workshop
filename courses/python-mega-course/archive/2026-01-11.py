while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case "edit":
            number = int(input("Enter the number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Enter the number of the todo to complete: "))
            number = number - 1
            todos.pop(number)
        case "exit":
            break

print("Goodbye!")