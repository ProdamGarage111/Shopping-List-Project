def print_welcome():
    print("Welcome to the program \"Shopping List\" v 1.3")

def print_menu():
    print("Menu:")
    print("[1] Show the product list;")
    print("[2] Add an item to the product list;")
    print("[3] Remove an item from the product list;")
    print("[0] Exit the program.")

def print_shopping_list(shopping_list):
    print("Shopping list:")
    for item in shopping_list:
        print(item)

def print_succesfully_added(item):
    print("Succefully added " + item + " to the shopping list!")

def print_succesfully_removed(item):
    print("Succefully removed " + item + " from the shopping list!")

def print_exiting_the_program():
    print("Exiting the program...")

def print_command_not_recognized():
    print("Command not recognized!")