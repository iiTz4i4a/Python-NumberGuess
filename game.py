from colors import RED, YELLOW, GREEN, BOLD, RESET


def start_game():
    while True:
        print(f"{GREEN}{BOLD}=== Start Game ==={RESET}")
        print_game_modes()

        try:
            user_action = int(input(f"{YELLOW}Choose an option: {RESET}"))

            if user_action == 6:
                break

            game_mode = select_game_template(user_action)

            if game_mode is None:
                print(f"{RED}Wrong option: Please try again{RESET}")
                input("Press Enter to continue...")
            else:
                print("Selected:", game_mode)

        except ValueError:
            print(f"{RED}Wrong option: Please try again{RESET}")
            input("Press Enter to continue...")


def print_game_modes():
    game_modes = [
        "1. Easy (1-10)",
        "2. Normal (1-100)",
        "3. Hard (1-1000)",
        "4. Insane (1-1000000)",
        "5. Custom",
        "6. Close",
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
    elif n == 6:
        return "Close"

    else:
        return None
