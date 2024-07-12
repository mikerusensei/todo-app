# Terminal Version of todo-app
# Usin python :>
# by: mikerusensei
# 7/12/2024

class Todo:
    def __init__(self, id:str, name:str, description:str, due_date:str) -> None:
        self.__id = id
        self.__name = name
        self.__description = description
        self.__due_date = due_date

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return sef.__description

    def get_due_date(self):
        return self.__due_date

if __name__ == '__main__':
    todo_list = {}

    running = True

    while running:
        print("Welcome to todo-app [Terminal Version]")
        print("[1] View Todos\n[2] Add Todo\n[3] Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            running = False
            print("Exiting program...")
        else:
            print("Incorrect input press [Space] to continue!")
            input()

