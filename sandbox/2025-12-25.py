todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            number = int(input("Enter the number of the todo to edit: "))
            now_todo = todos[number - 1]
            new_todo = input("Enter the new todo: ")
            todos[number - 1] = new_todo
        case "exit":
            break

print("Goodbye!")