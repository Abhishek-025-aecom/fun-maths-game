# CLAUDE.md

## Project Overview

Fun Maths Game is a simple interactive command-line Python maths quiz. It generates 5 random arithmetic questions (addition and multiplication), tracks the user's score, and provides immediate feedback. This is a beginner learning project for practicing Python basics and GitHub workflows.

## Tech Stack

- **Language:** Python 3 (standard library only)
- **Dependencies:** None — uses only the built-in `random` module
- **No build tools, package managers, or frameworks**

## Repository Structure

```
fun-maths-game/
├── game.py      # Entire application — single-file CLI quiz game
├── README.md    # Project description and goals
├── LICENSE      # MIT license
└── CLAUDE.md    # This file
```

## Running the Game

```bash
python3 game.py
```

The game is interactive — it reads from stdin and writes to stdout. There is no way to run it non-interactively.

## Development Workflow

### No formal tooling is configured

- No test framework (no pytest, unittest)
- No linter or formatter (no flake8, black, pylint)
- No type checker (no mypy)
- No CI/CD pipeline
- No pre-commit hooks
- No `.gitignore`

### Making changes

1. Edit `game.py` directly — all game logic lives in this single file
2. Test manually by running `python3 game.py`
3. Commit with clear messages following the existing style (imperative mood, e.g., "Add Fun Maths Game that quizzes user on addition")

## Code Conventions

- Simple, flat Python — no classes or functions, just a sequential script
- Uses f-strings for output formatting
- Uses emoji in user-facing messages (e.g., `Correct! ✅`, `Wrong ❌`)
- Variables use short, descriptive names (`score`, `a`, `b`, `answer`, `operation`)

## Key Design Decisions

- The game asks exactly 5 questions per session (hardcoded in `range(5)`)
- Random integers are between 1 and 10 inclusive
- Two operations are supported: addition (`+`) and multiplication (`*`)
- User input is converted directly with `int()` (no error handling for non-numeric input)

## Common Tasks for AI Assistants

- **Adding new operations:** Add to the `random.choice` list and add a corresponding `elif` branch
- **Changing difficulty:** Modify the `random.randint` range or the number of questions in `range(5)`
- **Adding error handling:** Wrap `int(input(...))` in a try/except block
- **Refactoring:** Extract game logic into functions (e.g., `generate_question()`, `check_answer()`, `play_game()`)
