# 🎯 Number Guessing Game

A simple **command-line number guessing game** written in Python.

Choose a game range, select how many attempts you want, and try to guess the randomly generated secret number. As you make mistakes, the game provides increasingly useful hints.

## ✨ Features

* 🎮 Multiple game modes
* 🎯 Custom number ranges
* ⚡ Custom number of attempts
* 💡 Progressive hints
* 🎨 Colored terminal interface
* 📖 Built-in rules with multiple pages
* 🔄 Input validation
* 🚪 Simple menu system

## 📋 Game Modes

The game provides four predefined ranges:

| Mode   |                 Range |
| ------ | --------------------: |
| Easy   |                  1–10 |
| Normal |                 1–100 |
| Hard   |               1–1,000 |
| Insane |           1–1,000,000 |
| Custom | Choose your own range |

You can also create a custom range as long as the first number is smaller than the second.

## 🎚️ Difficulty

The number of attempts can be selected independently from the number range.

| Difficulty |        Attempts |
| ---------- | --------------: |
| Easy       |               4 |
| Normal     |               3 |
| Hard       |               2 |
| Insane     |               1 |
| Custom     | Choose your own |

This means you can combine any game mode with any difficulty.

For example:

> **Range:** 1–1,000,000
> **Difficulty:** 1 attempt

Good luck. 😈

## 💡 Hint System

The game provides hints after incorrect guesses.

### Basic hints

After the first few misses, the game tells you whether the secret number is:

* **Higher**
* **Lower**

### Distance hints

After more misses, the hints change to describe how close your guess was:

* **Very close** — within 2
* **Close** — within 5
* **Warm** — within 10
* **Far** — more than 10 away

## 📁 Project Structure

```text
.
├── main.py       # Application entry point
├── menu.py       # Main menu and rules interface
├── game.py       # Game logic, difficulty, and hints
├── colors.py     # ANSI terminal color definitions
└── rules.txt     # In-game rules and instructions
```

### `main.py`

The entry point of the application. It starts the main menu.

### `menu.py`

Handles the user interface, including:

* Main menu
* Rules viewer
* Screen clearing
* Menu navigation

### `game.py`

Contains the core game functionality:

* Game mode selection
* Custom ranges
* Difficulty selection
* Secret number generation
* Guess handling
* Hint generation

### `colors.py`

Contains ANSI escape codes used to add colors and formatting to the terminal interface.

### `rules.txt`

Contains the game's rules displayed through the built-in paginated rules menu.

Pages are separated using:

```text
---PAGE---
```

## 🚀 Getting Started

### Requirements

* Python **3.8+**
* A terminal that supports ANSI color codes

The project uses only Python's standard library, so **no external packages are required**.

### Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd <project-directory>
```

Then start the game:

```bash
python main.py
```

On some systems you may need:

```bash
python3 main.py
```

## 🎮 How to Play

1. Start the application.
2. Select **Start Game**.
3. Choose a number range.
4. Select a difficulty.
5. Enter your guesses.
6. Use the hints to narrow down the secret number.
7. Guess correctly before you run out of attempts.

From the main menu you can also open **Rules** to read the game's instructions.

## 🛠️ Technologies

* **Python**
* `random` — secret number generation
* `os` — terminal screen clearing
* `pathlib` — filesystem utilities
* ANSI escape sequences — terminal colors

No third-party dependencies are currently required.

Have fun guessing! 🎯

