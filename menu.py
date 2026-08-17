import os
from pathlib import Path
from colors import GREEN, BLUE, RED, YELLOW, BOLD, RESET
from game import start_game

uiState = True


def showUI():
    print(f"{GREEN}{BOLD}Number Guessing Game{RESET}\n")
    print(f"{BLUE}{BOLD}1. Start Game{RESET}")
    print(f"{BLUE}{BOLD}2. Rules{RESET}")
    print(f"{RED}{BOLD}3. Quit{RESET}")

    try:
        userAction = int(input(f"{YELLOW}\nChoose an option: {RESET}"))
        action(userAction)
    except ValueError:
        print("\nYou have only two options. Cmon")
        input("Press Enter to continue...")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_rules():
    with open("rules.txt", "r", encoding="utf-8") as file:
        pages = file.read().split("---PAGE---")

    current_page = 0
    total_pages = len(pages)

    while True:
        clear_screen()

        print(pages[current_page].strip())

        print("\n----------------------------------------")
        print(f"Page {current_page + 1}/{total_pages}")
        print("----------------------------------------")
        print(f"{RED}{BOLD}[N] Next    [B] Back    [Q] Quit{RESET}")

        action = input("\nChoose an option: ").strip().lower()

        if action == "n":
            if current_page < total_pages - 1:
                current_page += 1

        elif action == "b":
            if current_page > 0:
                current_page -= 1

        elif action == "q":
            break

        else:
            print("\nWrong option!")
            input("Press Enter to continue...")


def action(n):
    global uiState
    if n == 1:
        start_game()
    elif n == 2:
        show_rules()
    elif n == 3:
        uiState = False
    else:
        print("You have only two options. Cmon")
        input("Press Enter to continue...")


def start_menu():
    global uiState

    while uiState:
        showUI()
