todos = []

while True:
    user_action = input("Type add or show: ")
    
    match user_action:
        case "add":
            todo = input("Enter a todo: ").lower()
            if todo in todos:
                print("Todo already exists")
            else:
                todos.append(todo)
        case "show":
            print(todos)
        case "delete":
            todo = input("Enter a todo to delete: ").lower()
            if todo in todos:
                todos.remove(todo)
            else:
                print("Todo not found")
        case "exit":
            exit()
        case _:
            print("Unknown command")