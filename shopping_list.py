import decorators
import working_with_file

def main():
    decorators.print_welcome()
    shopping_list= working_with_file.read_from_the_shopping_list_file()
    command = 1
    while command != 0:
        decorators.print_menu()
        command = input("Input your command here: ")
        if command in ['1','2','3','0']:
            command = int(command)
            if command == 1:
               decorators.print_shopping_list(shopping_list)
            elif command == 2:
                product_to_be_added = input("What would you like to add? ")
                shopping_list.append(product_to_be_added) 
                decorators.print_succesfully_added(product_to_be_added)
            elif command == 3:
                product_to_be_removed = input("What would you like to remove? ")
                shopping_list.remove(product_to_be_removed)
                decorators.print_succesfully_removed(product_to_be_removed)
            elif command == 0:
                decorators.print_exiting_the_program()
                working_with_file.write_to_the_shopping_list_file(shopping_list)         
        else:
            decorators.print_command_not_recognized()
            
  

