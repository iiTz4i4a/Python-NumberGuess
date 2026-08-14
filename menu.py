from colors import GREEN, BLUE, RED, YELLOW, BOLD, RESET
from game import start_game

uiState = True


def showUI():
    print(f"{GREEN}{BOLD}Number Guessing Game{RESET}\n")
    print(f"{BLUE}{BOLD}1. Start Game{RESET}")
    print(f"{RED}{BOLD}2. Quit{RESET}")

    try:
        userAction = int(input(f"{YELLOW}\nChoose an option: {RESET}"))
        action(userAction)
    except ValueError:
        print("You have only two options. Cmon")


def action(n):
    global uiState

    if n == 1:
        start_game()
    elif n == 2:
        uiState = False
    else:
        print("You have only two options. Cmon")


def start_menu():
    global uiState

    while uiState:
        showUI()
