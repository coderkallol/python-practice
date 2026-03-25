## Python Exercises (01 - 06)

This folder contains simple Python scripts meant to practice basic language features. Each `exerciseXX.py` file is a standalone program you can run individually.

### How to run

From this repository folder, run:

```powershell
python Exercises\exercise01.py
python Exercises\exercise02.py
python Exercises\exercise03.py
python Exercises\exercise04.py
python Exercises\exercise05.py
python Exercises\exercise06.py
```

Some exercises use `input()`, so you will see prompts in the terminal.

### Exercise-by-exercise guide

`Exercises/exercise01.py`
- `print()` usage (multiple arguments, `end=`, `sep=`)
- String operations (concatenation, repetition), escape sequences
- Variables and basic arithmetic
- Comments (single-line and multiline triple-quoted strings)
- Looping over a string and basic string slicing.

`Exercises/exercise02.py`
- `input()` basics (reading name/age from the user)
- `len()` for getting string length
- Type conversion using `int()` and `float()` and converting back to `str()`.

`Exercises/exercise03.py`
- Lists: indexing and nested lists
- List slicing patterns (`start:end`, negative indices, step slicing)
- Getting list length with `len()`
- Modifying list elements
- List concatenation (`+`) and replication (`*`)
- Iterating over lists using `range(len(...))`
- Membership tests with `in` / `not in`
- A small input-based pet-name check program.

`Exercises/exercise04.py`
- `if` / `elif` / `else` decision making (including an age eligibility check)
- `while` loops
- `break` and `continue`
- Input validation loops that keep asking until the user provides valid data.

`Exercises/exercise05.py`
- Functions basics (defining and calling functions)
- Function parameters (`greet(name)`)
- Returning values from functions (Magic 8-Ball-style responses)
- Using `random` to generate values and calling functions based on randomness.

`Exercises/exercise06.py`
- Working with imports (`random`, `sys`)
- Functions that demonstrate reusable program sections (random numbers, greeting, etc.)
- A “Guess the Number” game with input parsing and `try/except ValueError`
- An exit handler that uses `sys.exit()` to quit when the user types `exit` or confirms.

