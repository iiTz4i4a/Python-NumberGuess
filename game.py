from colors import RED, YELLOW, GREEN, BOLD, RESET


def start_game():
    print(f"{GREEN}{BOLD}=== Start Game ==={RESET}")
    print_game_modes()

    try:
        userAction = select_game_template(
            int(input(f"{YELLOW}Choose an option: {RESET}"))
        )

        if userAction is None:
            print(f"{RED}Wrong option: Please try again{RESET}")
        else:
            print("Selected Game Mode :", userAction)
    except ValueError:
        print(f"{RED}Wrong option: Please try again{RESET}")


def print_game_modes():
    game_modes = [
        "1. Easy (1-10)",
        "2. Normal (1-100)",
        "3. Hard (1-1000)",
        "4. Insane (1-1000000)",
        "5. Custom",
    ]
    for modes in game_modes:
        print(modes)


def select_game_template(n):
    if n == 1:
        return "Easy (1-10)"
    elif n == 2:
        return "Normal (1-100)"
    elif n == 3:
        return "Hard (1-1000)"
    elif n == 4:
        return "Insane (1-1000000)"
    elif n == 5:
        return "Custom"
    else:
        return None
