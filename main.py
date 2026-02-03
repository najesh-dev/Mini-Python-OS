# Menu and functions
from menu import start_screen, menu_screen
from function import *
#COLORS AND DESIGNS
from colors import *
PASSWORD=69
#Password
while True:
    try:
        a=int(input(f"{BOLD}Enter the Password: {RESET}\n"))
        if a==PASSWORD:
            clear_screen()
            start_screen()
            break
        else:
            print(f"{BOLD}{RED}Wrong password, TRY AGAIN!{RESET}")
            continue
    
    except ValueError:
        print("invalid, please enter number")
        continue 
# Choosing option from menu for running programs
while True:
            print("\n")
            menu_screen()
            choice=int(input("Choose an option: \n"))
            if choice==1:
                clear_screen()
                calculator()
            elif choice==2:
                clear_screen()
                show_time()
            elif choice==3:
                clear_screen()
                show_date()
            elif choice==4:
                clear_screen()
                print("exiting system...") # exits the system
                break
            else:
                print("Invalid option!")
                continue

        
   