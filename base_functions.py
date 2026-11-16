FILEPATH = "data/todos.txt"

def view_todos(filepath=FILEPATH):
    with open(filepath, "r", encoding="utf-8") as file:
        return [line.rstrip("\n") for line in file]

def write_todos(todos_num, filepath=FILEPATH):
    with open(filepath, "w", encoding="utf-8") as file:
        file.writelines(todo + "\n" for todo in todos_num)

if __name__ == "__main__":
    print(view_todos("todos.txt"))