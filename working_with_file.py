import utilities

def read_from_the_shopping_list_file():
    shopping_list = list(map(utilities.remove_two_last_characters_from_a_string, open('shopping_list.txt','r').readlines()))
    return shopping_list

def write_to_the_shopping_list_file(shopping_list):
    file = open("shopping_list.txt","w")
    for item in shopping_list:
        file.write(item + "\n")
    file.close()