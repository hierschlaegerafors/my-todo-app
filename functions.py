FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Return the lines of the todo file"""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__== "__main__":
    print(x)
    print(get_todos())