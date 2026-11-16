import base_functions

def add_todo(todos, todo):
    if not todo:
        print("\tВведіть тудушку")
        return True
    todos.append(todo)
    base_functions.write_todos(todos)
    return True

def show_todos(todos, todo_number):
    if not todos:
        print("\tСписок порожній")
    for number, todo in enumerate(todos, start=1):
        print(f"{number} : {todo}")
    return True

def edit_todo(todos, todo_number):
    todo_number = int(todo_number)
    if todo_number < 1 or todo_number > len(todos):
        raise IndexError
    new_todo = input("ВВедіть змінену задачу: ").strip()
    if not new_todo:
        print("\tВведіть тудушку")
        return True
    todos[todo_number - 1] = new_todo
    base_functions.write_todos(todos)
    return True

def complete_todo(todos, todo_number):
    todo_number = int(todo_number)
    if todo_number < 1 or todo_number > len(todos):
        raise IndexError
    todos.pop(todo_number - 1)
    base_functions.write_todos(todos)
    return True

def exit_program(todos, todo_number):
    print("До зустрічі!")
    return False

def help(todos, todo_number):
    print("Доступні команди:")
    print("\tдодати <текст> - додати нову справу")
    print("\tпоказати - показати список справ")
    print("\tзмінити <номер> - змінити текст справи за номером")
    print("\tвиконати <номер> - видалити виконану справу за номером")
    print("\tзакрити - завершити роботу програми")
    return True

COMMANDS = {
    "додати": add_todo,
    "показати": show_todos,
    "змінити": edit_todo,
    "виконати": complete_todo,
    "закрити": exit_program,
    "допомога": help,
}

def dispatch(todos, user_action):
    parts = user_action.strip().split(maxsplit=1)
    if not parts:
        print("\tВведіть команду. Введіть 'допомога' для довідки.")
        return True
    command = parts[0]
    todo_number = parts[1] if len(parts) > 1 else ""

    handler = COMMANDS.get(command)

    if handler is None:
        print("\tНевідома команда. Введіть 'допомога' для списку команд.")
        return True
    try:
        return handler(todos, todo_number)
    except ValueError:
        print("\tВведіть цілий номер справи")
        return True
    except IndexError:
        print("\tНевірний номер справи")
        return True

