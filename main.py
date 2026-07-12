#GatOS 0.1V
from programs import *
from colors import Colors
def new_user(user, pc):
    return f"{Colors.RED}{user.lower()}{Colors.RESET}{Colors.GREEN}@{pc.lower()}{Colors.RESET}"

user = input("Enter user name: ")
pc = input("Enter pc name: ")

user_pc = new_user(user, pc)

def main():
    while 1:
        user_input = input(f'{user_pc}>> ').lower()
        if user_input == "q" or user_input == "quit":
            break
        elif user_input == 'calc':
            calcul.launch()

        elif user_input == 'help' or user_input == 'h':
            print("type quit - to exit the program\ntype help - to help\ntype calc - to start Calculator\ntype prog - to show all programs")
        elif user_input == "prog":
            calcul.show_all_programs()
        else:
            print("type help - to help")

if __name__ == "__main__":
    main()