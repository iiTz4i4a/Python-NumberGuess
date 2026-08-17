import random

from colors import RED, YELLOW, GREEN, BOLD, RESET


def start_game():
    while True:
        print(f"{GREEN}{BOLD}=== Start Game ==={RESET}")

        game_mode = select_game_template()

        if game_mode == "Close":
            break

        if game_mode is None:
            print(f"{RED}Wrong option: Please try again{RESET}")
            input("Press Enter to continue...")
            continue

        min_number, max_number = game_mode

        attempts = select_difficulty()

        if attempts == "Close":
            break

        if attempts is None:
            print(f"{RED}Wrong difficulty: Please try again{RESET}")
            input("Press Enter to continue...")
            continue

        play_game(
            min_number,
            max_number,
            attempts,
        )


def select_game_template():
    game_modes = [
        "1. Easy (1-10)",
        "2. Normal (1-100)",
        "3. Hard (1-1000)",
        "4. Insane (1-1000000)",
        "5. Custom",
        "6. Close",
    ]

    for mode in game_modes:
        print(mode)

    try:
        user_action = int(input(f"{YELLOW}Choose an option: {RESET}"))

        if user_action == 1:
            return 1, 10

        elif user_action == 2:
            return 1, 100

        elif user_action == 3:
            return 1, 1000

        elif user_action == 4:
            return 1, 1000000

        elif user_action == 5:
            return select_custom_range()

        elif user_action == 6:
            return "Close"

        else:
            return None

    except ValueError:
        return None


def select_custom_range():
    while True:
        try:
            min_number = int(input("Enter first number: "))
            max_number = int(input("Enter second number: "))

            if min_number >= max_number:
                print(f"{RED}This range is not possible{RESET}")
                input("Press Enter to continue...")
            else:
                return min_number, max_number

        except ValueError:
            print(f"{RED}Only numbers!{RESET}")


def select_difficulty():
    game_difficulties = [
        "1. Easy (4 attempts)",
        "2. Normal (3 attempts)",
        "3. Hard (2 attempts)",
        "4. Insane (1 attempt)",
        "5. Custom",
        "6. Close",
    ]

    for difficulty in game_difficulties:
        print(difficulty)

    try:
        user_action = int(input(f"{YELLOW}Choose difficulty: {RESET}"))

        if user_action == 1:
            return 4

        elif user_action == 2:
            return 3

        elif user_action == 3:
            return 2

        elif user_action == 4:
            return 1

        elif user_action == 5:
            try:
                l = int(input("Enter amount of guesses: "))
                return l
            except ValueError:
                print(f"{RED}Only numbers!{RESET}")

        elif user_action == 6:
            return "Close"

        else:
            return None

    except ValueError:
        return None


def play_game(min_number, max_number, attempts):
    secret_number = random.randint(min_number, max_number)

    miss_count = 0

    while attempts > 0:
        print(f"\nAttempts left: {attempts}")

        try:
            guess = int(input("Enter your guess: "))

        except ValueError:
            print(f"{RED}Only numbers!{RESET}")
            continue

        if guess == secret_number:
            print(f"{GREEN}You guessed the number!{RESET}")
            return True

        attempts -= 1
        miss_count += 1

        if attempts == 0:
            break

        hint_level = get_hint_level(miss_count)

        hint = get_hint(
            guess,
            secret_number,
            hint_level,
        )

        print(f"{YELLOW}Hint: {hint}{RESET}")

    print(f"{RED}You lost! The secret number was {secret_number}.{RESET}")

    return False


def get_hint_level(miss_count):
    if miss_count <= 2:
        return 1

    else:
        return 2


def get_hint(guess, secret_number, hint_level):
    if hint_level == 1:
        return get_basic_hint(guess, secret_number)

    elif hint_level == 2:
        return get_distance_hint(guess, secret_number)

    return None


def get_basic_hint(guess, secret_number):
    if guess < secret_number:
        return "Higher"

    return "Lower"


def get_distance_hint(guess, secret_number):
    distance = abs(guess - secret_number)

    if distance <= 2:
        return "Very close"

    elif distance <= 5:
        return "Close"

    elif distance <= 10:
        return "Warm"

    return "Far"
