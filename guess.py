uiState = True

# Colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
BOLD = "\033[1m"


def showUI():
    print(f"{GREEN}{BOLD}Number Guessing Game\n{RESET}")
    print(f"{RED}{BOLD}\n10. Quit{RESET}")

    try:
        userAction = action(int(input(f"{YELLOW}\nChoose an option: {RESET}")))
    except ValueError:
        print("Not allowed option !")


def action(n):
    global uiState
    if n == 10:
        uiState = False


while uiState:
    showUI()
