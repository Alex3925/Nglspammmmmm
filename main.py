import os
import platform
import webbrowser

# Function to clear the screen
def clear_screen():
    # Clear screen based on OS
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# Function to print text in blue color
def print_blue(text):
    print("\033[94m" + text + "\033[0m")

# Function to print text in cyan color
def print_cyan(text):
    print("\033[96m" + text + "\033[0m")

# Function to print logo and menu in cyan color
def print_logo_and_menu(logo):
    print_box(logo, color_code="\033[96m")
    print_blue("\nMENU:")
    print_blue("1. Option 1")
    print_blue("2. Option 2")
    print_blue("3. Option 3")
    print_blue("0. Exit")

# Function to execute selected option
def execute_option(choice):
    try:
        if choice == '1':
            os.system('python nglspm.py')  # Execute option1.py
        elif choice == '2':
            os.system('python option2.py')  # Execute option2.py
        elif choice == '3':
            os.system('python option3.py')  # Execute option3.py
        elif choice == '0':
            print_blue("Exiting...")
        else:
            print_blue("Invalid choice. Please try again.")
            return False
        return True
    except Exception as e:
        print_blue("An error occurred:", e)
        input("Press Enter to continue...")
        return False

# Function to open the provided link in a web browser
def open_link_on_first_run():
    webbrowser.open("https://www.facebook.com/profile.php?id=100085861488156", new=2)

# Function to print text in a box UI with color
def print_box(text, color_code):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)

    border = color_code + '+' + '-' * (max_length + 2) + '+\033[0m'
    print(border)
    for line in lines:
        print(color_code + '| ' + line.ljust(max_length) + ' |\033[0m')
    print(border)

# Main function
def main():
    logo = """\033[96m██████╗░██╗██╗░░░░░░█████╗░████████╗
██╔══██╗██║██║░░░░░██╔══██╗╚══██╔══╝
██████╦╝██║██║░░░░░███████║░░░██║░░░
██╔══██╗██║██║░░░░░██╔══██║░░░██║░░░
██████╦╝██║███████╗██║░░██║░░░██║░░░
╚═════╝░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░\033[0m"""

    first_run = True

    while True:
        clear_screen()
        if first_run:
            print_logo_and_menu(logo)
            open_link_on_first_run()
            first_run = False
        print("\033[92m" + "Enter your choice: " + "\033[0m", end="")
        choice = input()

        if execute_option(choice):
            if choice != '0':
                clear_screen()
                print_blue("Thank you for using my tool. I love you!")
                input("Press Enter to continue...")
                clear_screen()  # Clear screen after printing the message
                break
        if choice == '0':
            break

if __name__ == "__main__":
    main()
