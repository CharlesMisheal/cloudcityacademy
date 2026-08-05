"""
Real technical lecture material for CloudCity Academy.
3 class sessions per week. No pedagogy templates — only subject matter.
"""
from __future__ import annotations

from curriculum import TOPICS, weeks_for

# ── helpers ───────────────────────────────────────────────────


def _split_topic(topic: str) -> tuple[str, str]:
    if "—" in topic:
        a, b = topic.split("—", 1)
        return a.strip(), b.strip()
    return topic.strip(), topic.strip()


def _pack(
    title: str,
    overview: str,
    lectures: list[tuple[str, str]],
    example: str,
    lab: list[str],
    vocab: list[tuple[str, str]],
    objectives: list[str],
    mcqs: list[tuple],
    subjective: str,
    upload: str,
) -> dict:
    assert len(lectures) == 3, title
    return {
        "title": title,
        "overview": overview.strip(),
        "lectures": lectures,
        "example": example.strip(),
        "lab": lab,
        "vocab": vocab,
        "objectives": objectives,
        "mcqs": mcqs,
        "subjective": subjective,
        "upload": upload,
    }


# ── Python for Beginners (12) ─────────────────────────────────


def _py_beginners(week: int, topic: str) -> dict:
    t, d = _split_topic(topic)
    banks = {
        1: _pack(
            t,
            "Python is a programming language. Programs are text files run by the Python interpreter in order, top to bottom.",
            [
                (
                    "What a program is",
                    "A program is a sequence of instructions a computer carries out. Python code is usually saved as a `.py` file. "
                    "When you run `python hello.py`, the interpreter reads each line, parses it, and executes it. "
                    "Python is case-sensitive: `Print` is not the same as `print`. Indentation (spaces at the start of a line) "
                    "matters later for blocks; this week keep every line starting at the left edge unless told otherwise.\n\n"
                    "The `print` function sends text to the console (the black/white output panel). Arguments go inside parentheses. "
                    "Strings (text) are wrapped in quotes: double `\"...\"` or single `'...'`.",
                ),
                (
                    "Comments and readability",
                    "Anything after `#` on a line is a comment — ignored by Python, useful for humans. Write why something exists, not what is obvious.\n\n"
                    "Good first program:\n"
                    "```\n"
                    "# greeting.py — first CloudCity script\n"
                    "print(\"Hello, CloudCity\")\n"
                    "print(\"I am learning Python\")\n"
                    "```\n"
                    "Run it. Confirm both lines appear. If you see `SyntaxError`, check missing quotes or parentheses.",
                ),
                (
                    "Using the REPL and files",
                    "You can type Python in interactive mode (`python` then enter) for tiny experiments. For class work, prefer a file so you can save and submit. "
                    "Pick one editor (IDLE, VS Code, Thonny). Always know: (1) where the file is saved, (2) which terminal folder you run from.\n\n"
                    "Escape sequences inside strings: `\\n` starts a new line, `\\t` is a tab. Example: `print(\"Line1\\nLine2\")`.",
                ),
            ],
            'print("Hello, CloudCity")\nprint("Week 1")\n# print("this is commented out")',
            [
                "Create folder PythonBeginners and file week01_hello.py",
                "Print three separate lines: your full name, course name, one sentence goal",
                "Add two useful comments at the top",
                "Run and fix any SyntaxError until it runs cleanly",
            ],
            [
                ("Interpreter", "Program that reads and runs Python code"),
                ("String", "Text data inside quotes"),
                ("SyntaxError", "Code that violates Python’s grammar"),
                ("Comment", "Note after # ignored by Python"),
            ],
            [
                "Run a .py file that prints multiple lines",
                "Use comments correctly",
                "Explain what print and strings are",
            ],
            [
                ("What does print do?", ["Delete files", "Show output in the console", "Install Python", "Format disks"], "Show output in the console"),
                ("A string is written as:", ["hello without quotes usually wrong", '"hello" or \'hello\'', "only numbers", "only # comments"], '"hello" or \'hello\''),
                ("# starts a:", ["comment", "loop", "function call", "file name"], "comment"),
            ],
            "In your own words: what is an interpreter, and what happens when Python hits a missing closing quote?",
            "Screenshot of your week01 script running successfully (code visible + console output).",
        ),
        2: _pack(
            t,
            "Variables store values under a name. Types include int, float, str, bool. Operators combine values.",
            [
                (
                    "Assignment",
                    "`name = value` stores a value. The name is a label, not a box that is “typed forever” in beginner Python — the same name can later hold a different type, but avoid confusion.\n\n"
                    "Rules for names: start with letter or `_`, then letters/digits/`_`. No spaces. Prefer `student_name` over `sn`. Names are case-sensitive.\n\n"
                    "```\nage = 16\nheight_m = 1.65\nfirst = \"Ada\"\nis_enrolled = True\nprint(first, age)\n```",
                ),
                (
                    "Common types",
                    "**int** — whole numbers (`42`). **float** — decimals (`3.14`). **str** — text. **bool** — `True` or `False` only.\n\n"
                    "`type(x)` reports the type. Use it when debugging.\n\n"
                    "Arithmetic: `+ - * /`  Division `/` always makes a float in Python 3 (`7/2` → `3.5`). Integer division `//` floors (`7//2` → `3`). Remainder `%` (`7%2` → `1`). Power `**` (`2**3` → `8`).",
                ),
                (
                    "Expressions and updating",
                    "An expression is calculated, then can be stored: `total = price * qty`.\n\n"
                    "Update patterns: `score = score + 1` or shorthand `score += 1` (also `-= *= /=`).\n\n"
                    "String `+` concatenates: `\"Hi \" + name`. You cannot add a string and int without converting (`str(age)`).\n\n"
                    "Compare later with week control flow; for now master storing and printing.",
                ),
            ],
            'name = "Ada"\nage = 16\nprice = 250.0\nqty = 3\ntotal = price * qty\nprint(name, "owes", total)',
            [
                "File week02_vars.py: store name, age, two product prices and quantities",
                "Compute two line totals and a grand total with variables (no hard-coded final number only)",
                "Print a clear receipt-style summary",
                "Use type() once in a comment or print to verify a float vs int",
            ],
            [
                ("Variable", "Name bound to a value"),
                ("int / float", "Whole number / decimal number"),
                ("Expression", "Code that calculates a value"),
                ("+=", "Add-and-assign shorthand"),
            ],
            ["Create and update variables", "Use int, float, str", "Compute with operators"],
            [
                ("How do you store 10 in count?", ["count == 10", "count = 10", "10 = count", "int count 10"], "count = 10"),
                ("7 / 2 in Python 3 is:", ["3", "3.5", "3.0 only as int", "error always"], "3.5"),
                ("\"3\" + \"4\" gives:", ["7", "\"34\"", "34 as int", "error always"], "\"34\""),
            ],
            "Explain the difference between = (assignment) and a mathematical equals sign people say in speech.",
            "Screenshot of week02 script and its printed values.",
        ),
        3: _pack(
            t,
            "Programs need data from the user. input() always returns a string; convert with int() or float() when you need numbers.",
            [
                (
                    "input()",
                    "`answer = input(\"Prompt: \")` displays the prompt, waits for Enter, returns the text the user typed as a **str**.\n\n"
                    "Even if they type 42, you get `\"42\"`. That matters for calculations.",
                ),
                (
                    "Conversion",
                    "`int(\"42\")` → 42. `float(\"3.5\")` → 3.5. If the text is not a valid number, Python raises `ValueError`.\n\n"
                    "```\nraw = input(\"Age: \")\nage = int(raw)\nprint(\"Next year you will be\", age + 1)\n```\n"
                    "Pattern: read → convert → use.",
                ),
                (
                    "Building a small interactive tool",
                    "Design prompts that are clear. Do not assume the user knows internal names. "
                    "Example tool: ask for item name, quantity, price; compute total; print a one-line invoice.\n\n"
                    "Optional: handle empty input by checking `if raw.strip() == \"\":` and printing a message (intro to decisions; full if next week).",
                ),
            ],
            'name = input("Your name: ")\nq = int(input("Quantity: "))\np = float(input("Unit price: "))\nprint(name, "total:", q * p)',
            [
                "week03_input.py: ask for two numbers and print sum, difference, product",
                "Ask for a person name and favourite subject; print a full sentence using both",
                "Build mini invoice: item, qty, price → total",
            ],
            [
                ("input()", "Read text from the keyboard as str"),
                ("int() / float()", "Convert text to numbers"),
                ("ValueError", "Conversion failed because text is not a valid number"),
            ],
            ["Use input", "Convert types safely for numeric work", "Print formatted results"],
            [
                ("input() returns type:", ["always int", "always str", "always float", "bool"], "always str"),
                ("To compute age+1 from input you must:", ["int(...) first", "print only", "use // forever", "delete quotes from code file"], "int(...) first"),
                ("int(\"hi\") causes:", ["ValueError", "prints hi", "returns 0 always", "infinite loop"], "ValueError"),
            ],
            "Why is converting user input necessary before multiplication?",
            "Screenshot of running interactive program with sample typing visible if possible.",
        ),
        4: _pack(
            t,
            "Operators compare and calculate. Comparison produces True/False (bool), the fuel for if-statements next week.",
            [
                (
                    "Arithmetic review with power and remainder",
                    "You already use `+ - * / // % **`. Remainder is useful for even/odd: `n % 2 == 0` means even. "
                    "Parentheses change order: `(a+b)*c` vs `a+(b*c)`.",
                ),
                (
                    "Comparison operators",
                    "`== != < <= > >=` compare two values and return bool.\n\n"
                    "```\nprint(5 > 3)    # True\nprint(5 == 5)   # True\nprint(5 != 2)   # True\nprint(\"a\" == \"A\")  # False (case-sensitive)\n```\n"
                    "Never confuse `==` (compare) with `=` (assign).",
                ),
                (
                    "Boolean logic intro",
                    "`and` — both sides True. `or` — at least one True. `not` flips True/False.\n\n"
                    "```\nage = 16\nhas_pass = True\nprint(age >= 13 and has_pass)\n```\n"
                    "Truth tables in words: for `and`, if left is False, result is False. For `or`, if left is True, result is True.",
                ),
            ],
            "score = 72\nprint(score >= 50)  # True\nprint(score >= 50 and score < 80)",
            [
                "week04_ops.py: ask for a score; print whether pass (>=50), distinction (>=70), fail",
                "Without if: use print of comparison expressions",
                "Even/odd checker with %",
            ],
            [
                ("==", "Equality comparison"),
                ("bool", "True or False"),
                ("and / or / not", "Combine or flip bools"),
            ],
            ["Use comparisons", "Explain and/or/not", "Apply % for even/odd"],
            [
                ("5 == 5.0 is:", ["True", "False", "Error", "None"], "True"),
                ("Operator for not equal:", ["=!", "!=", "<> only in Python 3 always", "==="], "!="),
                ("True and False is:", ["True", "False", "None", "1"], "False"),
            ],
            "Explain why `age = 16` then `age == 16` uses two different symbols.",
            "Screenshot of week04 outputs for pass/fail checks.",
        ),
        5: _pack(
            t,
            "if / elif / else choose which block of code runs. Indentation defines the block.",
            [
                (
                    "The if statement",
                    "```\nscore = int(input(\"Score: \"))\nif score >= 50:\n    print(\"Pass\")\nelse:\n    print(\"Fail\")\n```\n"
                    "The condition after `if` must be an expression with True/False result. "
                    "Indented lines (4 spaces) form the body. Unindent ends the body.",
                ),
                (
                    "elif chains",
                    "Use `elif` for extra branches; only one branch runs.\n\n"
                    "```\nif score >= 70:\n    print(\"A\")\nelif score >= 60:\n    print(\"B\")\nelif score >= 50:\n    print(\"C\")\nelse:\n    print(\"F\")\n```\n"
                    "Order matters: put more specific/higher thresholds first.",
                ),
                (
                    "Nested decisions and pitfalls",
                    "You can put if inside if, but keep nesting shallow (readability). "
                    "Pitfalls: using `=` instead of `==`; forgetting colon `:`; wrong indent mixing tabs/spaces.\n\n"
                    "Validate ranges: reject scores outside 0–100 with an if before grading.",
                ),
            ],
            "temp = 36\nif temp >= 38:\n    print(\"Fever\")\nelif temp >= 37.5:\n    print(\"Elevated\")\nelse:\n    print(\"Normal range (rough)\")",
            [
                "week05_if.py: ticket price by age (child/adult/senior) with clear thresholds you define",
                "Login mock: correct password string → success else failure",
                "Grade letter from score 0–100 with validation",
            ],
            [
                ("Branch", "One path chosen by if/elif/else"),
                ("Indentation", "Spaces that group a block"),
                ("elif", "Else-if intermediate condition"),
            ],
            ["Write if/elif/else programs", "Validate input ranges", "Avoid = vs =="],
            [
                ("Body of if must be:", ["indented", "in quotes", "after print only", "without colon ever"], "indented"),
                ("if x = 5: is wrong because:", ["= assigns, need == for compare", "5 is illegal", "if cannot use numbers", "Python forbids 5"], "= assigns, need == for compare"),
                ("Only one branch runs in if/elif/else:", ["True", "False always both run", "Random", "Never"], "True"),
            ],
            "Write graded rules you chose for A/B/C/F and why order of elif matters.",
            "Screenshot of branch program for two different inputs.",
        ),
        6: _pack(
            t,
            "while repeats as long as a condition stays True. Control infinite loops with updates and break.",
            [
                (
                    "while structure",
                    "```\nn = 1\nwhile n <= 5:\n    print(n)\n    n = n + 1\n```\n"
                    "If you forget to update `n`, the loop never ends (infinite loop). Stop with Ctrl+C in the terminal.",
                ),
                (
                    "Sentinel loops",
                    "Loop until user types a stop word:\n"
                    "```\ncmd = \"\"\nwhile cmd != \"quit\":\n    cmd = input(\"Command (quit to stop): \")\n    print(\"You said\", cmd)\n```\n"
                    "Or `while True:` with `if ...: break` inside when done.",
                ),
                (
                    "break and continue",
                    "`break` exits the loop immediately. `continue` skips to the next iteration. "
                    "Use sparingly but know them for menu programs and input retries.",
                ),
            ],
            "secret = \"blue\"\nwhile True:\n    g = input(\"Guess colour: \")\n    if g == secret:\n        print(\"Correct\")\n        break\n    print(\"Try again\")",
            [
                "week06_while.py: print numbers 1..N from user input",
                "Sum numbers until user enters 0 (sentinel)",
                "Simple password retry: max 3 attempts then lock message",
            ],
            [
                ("Iteration", "One pass of a loop"),
                ("Infinite loop", "Condition never becomes False"),
                ("break", "Exit loop early"),
            ],
            ["Write while loops", "Use sentinels", "Prevent accidental infinite loops"],
            [
                ("while needs a condition that can become False or a break:", ["True", "False", "Only for files", "Only for lists"], "True"),
                ("n = n + 1 in a counting loop is for:", ["Updating so the loop progresses", "Deleting n", "Printing once", "Importing math"], "Updating so the loop progresses"),
                ("break does:", ["Leave the loop", "Restart computer", "Define a function", "Open a file"], "Leave the loop"),
            ],
            "Describe a real loop bug you could cause and how you would spot it.",
            "Screenshot of sentinel sum or retry program running.",
        ),
        7: _pack(
            t,
            "for loops iterate sequences. range() makes number series. Prefer for when you know how many times.",
            [
                (
                    "for over range",
                    "```\nfor i in range(5):\n    print(i)  # 0,1,2,3,4\n```\n"
                    "`range(start, stop)` stop is exclusive. `range(1, 6)` → 1..5. `range(0, 10, 2)` steps by 2.",
                ),
                (
                    "for over strings and lists intro",
                    "```\nfor ch in \"Ada\":\n    print(ch)\nfor item in [\"pen\", \"book\"]:\n    print(item)\n```\n"
                    "Each iteration binds the loop variable to the next element.",
                ),
                (
                    "Patterns: accumulate and table",
                    "Running total: `total = 0` then `total += x` inside the loop. "
                    "Multiplication table: nested for loops (outer and inner). "
                    "Know when while is better (unknown repetitions) vs for (known sequence).",
                ),
            ],
            "total = 0\nfor n in range(1, 6):\n    total += n\nprint(total)  # 15",
            [
                "week07_for.py: sum of 1..N with for",
                "Print a 1..10 times table for a user-chosen number",
                "Count vowels in a typed word (a,e,i,o,u)",
            ],
            [
                ("range", "Sequence of integers used by for"),
                ("Exclusive stop", "range end is not included"),
                ("Accumulator", "Variable that grows across iterations"),
            ],
            ["Use for and range", "Accumulate totals", "Iterate characters"],
            [
                ("range(3) yields:", ["0,1,2", "1,2,3", "0,1,2,3", "3 only"], "0,1,2"),
                ("for is best when:", ["Sequence length known", "You hate while always", "No variables", "Only floats"], "Sequence length known"),
                ("range(1,5) includes:", ["1,2,3,4", "1,2,3,4,5", "0,1,2,3,4", "5 only"], "1,2,3,4"),
            ],
            "When would you choose while over for? Give a concrete program idea.",
            "Screenshot of table or vowel counter.",
        ),
        8: _pack(
            t,
            "Lists store ordered collections. Indexing, slicing, and methods let you work with many values.",
            [
                (
                    "Create and index",
                    "```\nnums = [10, 20, 30]\nprint(nums[0])   # 10 first item\nprint(nums[-1])  # 30 last item\nnums[1] = 25     # change\n```\n"
                    "IndexError if index is out of range.",
                ),
                (
                    "Methods and length",
                    "`append(x)` add to end. `insert(i, x)`. `remove(x)` first match. `pop()` last or `pop(i)`. "
                    "`len(list)` length. `x in list` membership True/False.\n\n"
                    "Loop: `for item in nums:` or `for i in range(len(nums)):`.",
                ),
                (
                    "Slicing intro",
                    "`nums[1:3]` from index 1 up to but not 3. `nums[:2]` head. `nums[2:]` tail. "
                    "Slicing returns a new list. Useful for copies: `copy = nums[:]` .",
                ),
            ],
            "scores = [70, 55, 90]\nscores.append(60)\nprint(sum(scores)/len(scores))",
            [
                "week08_lists.py: start empty list; append 5 scores from input; print min, max, average",
                "Remove one score by value; print list",
                "Print scores above average only",
            ],
            [
                ("Index", "Position starting at 0"),
                ("append", "Add item to end of list"),
                ("len", "Number of items"),
            ],
            ["Build and update lists", "Compute aggregate stats", "Filter with a loop"],
            [
                ("First item index is:", ["0", "1", "-1 only", "len"], "0"),
                ("append adds:", ["at end", "at start always", "in middle only", "nowhere"], "at end"),
                ("len([1,2,3]) is:", ["3", "2", "0", "1"], "3"),
            ],
            "Explain why lists are better than five separate variables for class scores.",
            "Screenshot of list program output.",
        ),
        9: _pack(
            t,
            "Strings are sequences of characters with useful methods for cleaning and searching text.",
            [
                (
                    "Indexing like lists",
                    "`s[0]`, `s[-1]`, slices `s[1:4]`. Strings are immutable — you cannot do `s[0] = \"A\"`; build a new string instead.",
                ),
                (
                    "Core methods",
                    "`lower()`, `upper()`, `strip()` remove edge whitespace, `replace(a,b)`, `startswith`, `endswith`, "
                    "`find(sub)` index or -1, `split()` → list of words, `join` on a separator.\n\n"
                    "```\nraw = \"  Hello World  \"\nclean = raw.strip().lower()\nprint(clean)  # hello world\n```",
                ),
                (
                    "f-strings formatting",
                    "```\nname = \"Ada\"\nage = 16\nprint(f\"{name} is {age} years old\")\n```\n"
                    "Prefer f-strings for readable output in modern Python 3.",
                ),
            ],
            "msg = \"Banana Bread\"\nprint(msg.lower().replace(\"banana\", \"mango\"))",
            [
                "week09_str.py: read a sentence; print word count (split), character count, uppercase version",
                "Palindrome check ignoring case and spaces (optional stretch)",
                "Simple censor: replace a banned word with ****",
            ],
            [
                ("Immutable", "Cannot change characters in place"),
                ("strip", "Remove surrounding whitespace"),
                ("f-string", "Formatted string with {expressions}"),
            ],
            ["Use string methods", "Format with f-strings", "Split text into words"],
            [
                ("\"Hi\".lower() is:", ["hi", "HI", "Hi", "error"], "hi"),
                ("Strings are:", ["immutable", "always lists", "ints", "files"], "immutable"),
                ("split() without args splits on:", ["whitespace", "commas only", "dots only", "tabs only always"], "whitespace"),
            ],
            "Give two real cases where strip() saves you from buggy comparisons.",
            "Screenshot of string processing program.",
        ),
        10: _pack(
            t,
            "Functions package reusable steps. Parameters take inputs; return sends a result back.",
            [
                (
                    "Defining and calling",
                    "```\ndef greet(name):\n    return f\"Hello, {name}\"\n\nprint(greet(\"Ada\"))\n```\n"
                    "`def` creates the function. Call with parentheses. Without call, nothing runs.",
                ),
                (
                    "Parameters, returns, scope",
                    "Parameters are local names for inputs. `return` exits and yields a value. "
                    "Code after return in that function does not run. "
                    "Variables created inside a function are local — invisible outside.",
                ),
                (
                    "Design habit",
                    "One function ≈ one job: `area_rect(w, h)`, `is_pass(score)`, `average(nums)`. "
                    "Avoid giant functions that print, calculate, and format everything; split them. "
                    "Docstring optional: first string under def describing purpose.",
                ),
            ],
            "def average(nums):\n    return sum(nums)/len(nums)\n\nprint(average([10, 20, 30]))",
            [
                "week10_fn.py: functions celsius_to_f, fahrenheit_to_c",
                "function is_even(n) returning bool",
                "function max_of_three(a,b,c) without using max() built-in (use if)",
            ],
            [
                ("Parameter", "Input name in def"),
                ("return", "Send result to caller"),
                ("Local variable", "Exists only inside the function"),
            ],
            ["Write functions with return", "Call functions from main code", "Keep one-job functions"],
            [
                ("def starts a:", ["function definition", "loop", "import", "class only"], "function definition"),
                ("Without return, function returns:", ["None", "0", "False always", "error"], "None"),
                ("Calling greet means:", ["greet()", "greet", "def greet", "return greet"], "greet()"),
            ],
            "Why return a value instead of only printing inside the function?",
            "Screenshot of function-based script.",
        ),
        11: _pack(
            t,
            "Files store data beyond one program run. Text mode read/write with open and context managers.",
            [
                (
                    "Writing text",
                    "```\nwith open(\"note.txt\", \"w\", encoding=\"utf-8\") as f:\n    f.write(\"Line one\\n\")\n    f.write(\"Line two\\n\")\n```\n"
                    "`w` overwrites. `a` appends. Always consider encoding for international text (`utf-8`).",
                ),
                (
                    "Reading text",
                    "```\nwith open(\"note.txt\", \"r\", encoding=\"utf-8\") as f:\n    text = f.read()\n# or\nwith open(\"note.txt\", encoding=\"utf-8\") as f:\n    for line in f:\n        print(line.strip())\n```\n"
                    "`with` closes the file automatically — preferred over bare `open/close`.",
                ),
                (
                    "Paths and errors",
                    "If the file is missing on read → `FileNotFoundError`. Save the .py and data file locations you understand. "
                    "Relative path `data/note.txt` depends on the working directory when you run Python.",
                ),
            ],
            "with open(\"scores.txt\", \"w\", encoding=\"utf-8\") as f:\n    f.write(\"70\\n85\\n90\\n\")\n\nwith open(\"scores.txt\", encoding=\"utf-8\") as f:\n    nums = [int(line) for line in f]\nprint(sum(nums)/len(nums))",
            [
                "week11_files.py: write 5 names to names.txt (one per line)",
                "Read them back and print numbered list",
                "Read a scores file you created; print average",
            ],
            [
                ("with open", "Context manager — auto close"),
                ("Mode w/a/r", "write / append / read"),
                ("encoding", "How bytes map to characters"),
            ],
            ["Write and read text files", "Use with open", "Handle simple numeric files"],
            [
                ("Mode \"w\" will:", ["overwrite existing file", "always append", "read only", "delete Python"], "overwrite existing file"),
                ("with open is preferred because:", ["it closes the file reliably", "it is slower always bad", "no paths allowed", "skips utf-8"], "it closes the file reliably"),
                ("Missing file on read raises:", ["FileNotFoundError", "SyntaxError", "IndentationError", "True"], "FileNotFoundError"),
            ],
            "What is the difference between write mode and append mode?",
            "Screenshot showing file contents and program output.",
        ),
        12: _pack(
            t,
            "Capstone: combine input, decisions, loops, lists, functions, and optionally files into one menu-driven program.",
            [
                (
                    "Menu architecture",
                    "```\nwhile True:\n    print(\"1) Add  2) List  3) Quit\")\n    choice = input(\"> \")\n    if choice == \"1\":\n        ...\n    elif choice == \"3\":\n        break\n```\n"
                    "Keep data in a list. Put each action in its own function.",
                ),
                (
                    "Capstone brief options",
                    "Choose one: (A) student score book — add, list, average, save to file; "
                    "(B) mini shop — add items with price, show cart, total; "
                    "(C) flashcard quiz — ask questions from a list, tally score.",
                ),
                (
                    "Quality bar",
                    "Runs without crash on happy path; invalid menu choice prints message; "
                    "functions used; readable prompt text; optional file save for bonus; "
                    "you can demo in under 2 minutes.",
                ),
            ],
            "def average(scores):\n    return sum(scores)/len(scores) if scores else 0\n\nscores = []\n# menu loop calls functions…",
            [
                "Implement your chosen capstone fully",
                "At least 4 user-visible operations",
                "Use ≥2 functions of your own",
                "README comment at top with how to run and sample session",
            ],
            [
                ("Menu loop", "while True with choices"),
                ("State", "Data kept in lists/variables between actions"),
            ],
            ["Ship a small complete program", "Structure with functions", "Handle bad menu input"],
            [
                ("A menu program often uses:", ["while True", "only print once", "no variables", "import os only"], "while True"),
                ("Capstone should:", ["combine course skills", "be empty", "be only comments", "crash always"], "combine course skills"),
                ("Invalid menu input should:", ["show a message and continue", "format C drive", "kill Python forever without message", "ignore silently forever only"], "show a message and continue"),
            ],
            "Capstone report: goal, features list, how to demo, one limitation.",
            "Screenshot of capstone menu + one feature result.",
        ),
    }
    return banks[week]


# ── Python Data Apps (16) — user called out CSV week ──────────


def _py_data(week: int, topic: str) -> dict:
    t, d = _split_topic(topic)
    banks = {
        1: _pack(
            t,
            "Refresh pure Python needed for data work: lists of rows, dict rows, loops, functions, and clear printed tables.",
            [
                (
                    "Data as nested structures",
                    "A table in memory can be a list of lists:\n"
                    "`rows = [[\"Ada\", 70], [\"Ben\", 85]]`\n"
                    "Or list of dicts (often clearer):\n"
                    "`rows = [{\"name\":\"Ada\",\"score\":70}, {\"name\":\"Ben\",\"score\":85}]`\n"
                    "You will iterate rows and access fields by index or key.",
                ),
                (
                    "Small utilities",
                    "Write helpers: `mean(values)`, `print_table(rows)`, `to_float(text)`. "
                    "Guard empty lists when averaging. Convert carefully; bad numeric text appears constantly in real data.",
                ),
                (
                    "Lab mindset",
                    "Data programs: load → inspect → transform → summarise → output. "
                    "Always print a few raw rows before computing so you trust the input.",
                ),
            ],
            "rows = [{\"name\":\"Ada\",\"score\":70},{\"name\":\"Ben\",\"score\":85}]\nprint(sum(r[\"score\"] for r in rows)/len(rows))",
            [
                "Build list-of-dicts for 6 students with name, gender, score",
                "Print a text table with aligned columns (use f-strings widths)",
                "Functions: mean_score, count_passed(threshold)",
            ],
            [("row", "One record"), ("field/column", "One attribute"), ("inspect", "Look before summarise")],
            ["Represent tables in Python", "Compute simple summaries", "Print readable text tables"],
            [
                ("List of dicts models a table by:", ["each dict a row", "each dict a filename", "only headers", "only charts"], "each dict a row"),
                ("Before averaging you should:", ["check values exist and convert types", "delete all rows", "only plot", "ignore data"], "check values exist and convert types"),
                ("mean of empty list is a problem because:", ["division by zero", "strings cannot print", "Python deletes files", "loops fail always"], "division by zero"),
            ],
            "Why list-of-dicts is often clearer than list-of-lists for student data.",
            "Screenshot of printed table and mean.",
        ),
        2: _pack(
            t,
            "CSV is the standard plain-text table format: rows of fields separated by commas (or other delimiters), often with a header row.",
            [
                (
                    "CSV anatomy",
                    "CSV = Comma-Separated Values. Example file `marks.csv`:\n\n"
                    "```\n"
                    "name,subject,score\n"
                    "Ada,Math,78\n"
                    "Ben,Math,85\n"
                    "Ada,English,91\n"
                    "```\n\n"
                    "Line 1 is usually the **header** (column names). Each following line is a **record**. "
                    "Fields are separated by a **delimiter** (comma, or sometimes `;` or tab).\n\n"
                    "Rules that bite beginners:\n"
                    "• A field containing a comma must be quoted: `\"Lagos, Nigeria\"`\n"
                    "• Quotes inside fields are doubled: `\"He said \"\"hi\"\"\"`\n"
                    "• Prefer UTF-8 encoding so names with accents or special characters do not corrupt\n"
                    "• Do not put two different tables in one CSV without a clear scheme",
                ),
                (
                    "Create and open CSVs correctly",
                    "You can create CSV in Excel/Google Sheets: enter headers in row 1, data below, "
                    "Save/Download as CSV (UTF-8 if offered). Open the file in a plain text editor to verify "
                    "you see commas and headers — not a binary mess.\n\n"
                    "In Excel, a cell that looks like `0012` may become `12` (number). For codes that need leading zeros, "
                    "store as text or accept normalisation.\n\n"
                    "Never use a photo of a table as your data source for analysis programs; export real CSV text.",
                ),
                (
                    "Read CSV with Python’s csv module",
                    "```python\n"
                    "import csv\n\n"
                    "with open(\"marks.csv\", newline=\"\", encoding=\"utf-8\") as f:\n"
                    "    reader = csv.DictReader(f)\n"
                    "    rows = list(reader)\n\n"
                    "for r in rows:\n"
                    "    print(r[\"name\"], r[\"score\"])\n"
                    "```\n\n"
                    "`csv.DictReader` uses the header to make each row a dict: `{\"name\":\"Ada\", \"subject\":\"Math\", \"score\":\"78\"}`. "
                    "Notice: **all values are strings** until you convert. `int(r[\"score\"])` or `float(...)` is required for maths.\n\n"
                    "`newline=\"\"` on open is the recommended Windows-safe setting for the csv module.\n\n"
                    "Writing:\n"
                    "```python\n"
                    "with open(\"out.csv\", \"w\", newline=\"\", encoding=\"utf-8\") as f:\n"
                    "    w = csv.DictWriter(f, fieldnames=[\"name\", \"score\"])\n"
                    "    w.writeheader()\n"
                    "    w.writerow({\"name\": \"Ada\", \"score\": 78})\n"
                    "```",
                ),
            ],
            "import csv\n\nwith open(\"marks.csv\", newline=\"\", encoding=\"utf-8\") as f:\n"
            "    rows = list(csv.DictReader(f))\n"
            "scores = [int(r[\"score\"]) for r in rows]\n"
            "print(\"rows\", len(rows), \"mean\", sum(scores)/len(scores))",
            [
                "By hand create marks.csv with headers name,subject,score and at least 8 data rows (reuse students across 2 subjects)",
                "Write read_csv_mean.py that prints row count, min/max/mean of score",
                "Write a filtered print: only rows where score >= 70",
                "Export filtered rows to pass_list.csv with DictWriter",
            ],
            [
                ("CSV", "Plain text table; fields separated by a delimiter"),
                ("Header row", "First line naming columns"),
                ("DictReader", "csv reader that maps header → values per row"),
                ("Delimiter", "Character between fields, often comma"),
                ("UTF-8", "Common text encoding for international characters"),
            ],
            [
                "Explain CSV structure (header, rows, delimiter, quoting)",
                "Create a valid CSV and inspect it as text",
                "Load with csv.DictReader and convert numeric fields",
                "Write a new CSV with DictWriter",
            ],
            [
                (
                    "After DictReader, r[\"score\"] is usually:",
                    ["str until you convert", "always int", "always float list", "a file handle"],
                    "str until you convert",
                ),
                (
                    "A field that contains a comma should be:",
                    ["inside double quotes in the CSV", "deleted", "turned into a photo", "spaces only"],
                    "inside double quotes in the CSV",
                ),
                (
                    "newline=\"\" when opening for csv on Windows is:",
                    ["recommended", "forbidden", "only for images", "only for PDF"],
                    "recommended",
                ),
            ],
            "Explain: (1) what a header is, (2) why scores must be converted to int/float, "
            "(3) what goes wrong if someone saves an Excel file as .xls and renames it to .csv without exporting.",
            "Screenshot: text of marks.csv + program output with mean + pass_list.csv open or printed.",
        ),
        3: _pack(
            t,
            "Real data is messy: missing cells, extra spaces, mixed case, wrong types, duplicate rows, outliers.",
            [
                (
                    "Kinds of mess",
                    "Missing: empty string or `NA`. Whitespace: `\" Ada \"`. Case: `math` vs `Math`. "
                    "Types: `\"78%\"` with a percent sign. Duplicates: same student entered twice. "
                    "Outliers: score 780 when max is 100 — may be typo.",
                ),
                (
                    "Cleaning patterns in Python",
                    "```python\n"
                    "name = r[\"name\"].strip().title()\n"
                    "raw = r[\"score\"].replace(\"%\", \"\").strip()\n"
                    "score = int(raw) if raw not in (\"\", \"NA\", \"N/A\") else None\n"
                    "```\n"
                    "Build a new list of cleaned dicts; do not overwrite raw files until you are sure — write `clean_marks.csv`.",
                ),
                (
                    "Validation report",
                    "Count how many rows dropped and why. Print: `dropped_missing_score: 2`. "
                    "Transparency beats silent deletion. Keep a `issues.txt` log for class grading evidence.",
                ),
            ],
            "raw = \" 78% \"\nclean = int(raw.replace(\"%\",\"\").strip())  # 78",
            [
                "Create messy.csv deliberately with spaces, %, blank scores, inconsistent subject case",
                "Write clean_data.py producing clean.csv + print drop counts",
                "Assert all scores are int 0–100 in the clean file",
            ],
            [
                ("strip/title", "Normalise whitespace/case"),
                ("Sentinel missing", "NA/empty meaning no value"),
                ("Outlier", "Value far from plausible range"),
            ],
            ["Identify common messes", "Clean to a new file", "Report drops"],
            [
                ("Why write clean.csv instead of only editing in memory?", ["Save reproducible clean data", "Python forbids memory", "CSV cannot exist", "To delete headers"], "Save reproducible clean data"),
                ("\" 78% \".strip().replace(\"%\",\"\") helps:", ["parse int", "draw charts only", "encrypt", "rename disks"], "parse int"),
                ("Silent delete of bad rows without counting is:", ["bad practice", "required by CSV", "UTF-8", "DictWriter"], "bad practice"),
            ],
            "Describe three cleaning rules you implemented and one row you rejected.",
            "Screenshot of messy vs clean samples and drop counts.",
        ),
        4: _pack(
            t,
            "Summaries compress tables: count, sum, mean, min, max, median idea, rate (percent).",
            [
                (
                    "Measures",
                    "count = len. sum. mean = sum/count. min/max. "
                    "Percent pass = count_pass/count * 100. "
                    "Always state the group: mean of all scores vs mean Math only.",
                ),
                (
                    "Implement from scratch",
                    "Use loops or generator expressions. "
                    "`mean = sum(vals)/len(vals)`. "
                    "For grouped means you will bucket later; this week overall + one subset filter.",
                ),
                (
                    "Communicate results",
                    "Print rounded human output: `round(mean, 2)`. "
                    "Never invent precision that was not in the data. "
                    "One insight sentence: “Math average is below English by …”",
                ),
            ],
            "vals = [70, 85, 90]\nprint(min(vals), max(vals), sum(vals)/len(vals))",
            [
                "From clean CSV compute count, mean, min, max, pass rate at 50 and at 70",
                "Write results to summary.txt as labelled lines",
            ],
            [("mean", "Average"), ("pass rate", "Share meeting threshold"), ("round", "Display precision")],
            ["Compute core statistics", "Export a short text summary", "State the population measured"],
            [
                ("Pass rate needs:", ["count meeting rule / total", "only max", "only min", "file size"], "count meeting rule / total"),
                ("mean of [10,20] is:", ["15", "30", "10", "20"], "15"),
                ("round(3.14159, 2) is:", ["3.14", "3", "3.14159", "14"], "3.14"),
            ],
            "Explain mean vs max and when max alone misleads a teacher.",
            "Screenshot of summary.txt content.",
        ),
        5: _pack(
            t,
            "Charts show patterns if axes and chart type match the question. Matplotlib-style mental model (or school tool).",
            [
                (
                    "Chart types",
                    "Bar: compare categories (mean by subject). Line: trend over time. Histogram: distribution of scores. "
                    "Pie: parts of whole only for few categories. Wrong type confuses more than it helps.",
                ),
                (
                    "Anatomy of an honest chart",
                    "Title states the question. Axis labels with units. "
                    "Start bar axes at 0 when comparing magnitudes. "
                    "Don’t explode 3D effects. Legend only if needed. "
                    "Source note: which file / date.",
                ),
                (
                    "Minimal plotting workflow",
                    "Prepare two lists: labels and values. Plot. Save figure as PNG for reports. "
                    "If your lab uses a simpler tool, same rules apply.",
                ),
            ],
            "# pseudo\n# labels = subjects; values = means\n# bar chart titled \"Mean score by subject\"",
            [
                "Compute mean score per subject from CSV",
                "Create a bar chart image mean_by_subject.png",
                "Write one insight sentence under a chart label file",
            ],
            [("axis", "Scale line on a chart"), ("bar chart", "Category comparison"), ("distribution", "How values spread")],
            ["Choose chart type for a question", "Label charts properly", "Export PNG"],
            [
                ("Bar charts are good for:", ["categories", "raw binary files", "passwords", "RAM"], "categories"),
                ("A chart title should:", ["state what is shown", "be empty", "be only emoji", "hide units always"], "state what is shown"),
                ("Bars for magnitude comparisons usually start at:", ["0", "mean", "max", "random"], "0"),
            ],
            "Why a pie chart of 30 subjects would be a bad idea.",
            "Screenshot of chart image.",
        ),
        6: _pack(
            t,
            "Analysis starts with a clear question that data can actually answer.",
            [
                (
                    "Good vs bad questions",
                    "Bad: “Is education good?” (vague). "
                    "Better: “What is the pass rate in Math for this class CSV?” "
                    "Best questions name the measure, population, and time/scope.",
                ),
                (
                    "Question → columns → method",
                    "Write: Question; Columns needed; Method (filter/group/mean); Expected chart; "
                    "Limitation (sample size, bias). This is your analysis plan.",
                ),
                (
                    "Avoid fishing",
                    "Randomly slicing until something “significant” appears without a prior question leads to false stories. "
                    "Pre-register your question in notes, then compute.",
                ),
            ],
            "Q: Mean English vs Math?\nCols: subject, score\nMethod: filter each subject; mean\nLimit: one class only",
            [
                "Write 3 analysis questions for your student CSV",
                "Answer one fully with numbers + chart or table",
                "List 2 limitations of the answer",
            ],
            [("population", "Who/what the data covers"), ("limitation", "What you cannot conclude")],
            ["Write answerable data questions", "Map questions to columns", "Report limitations"],
            [
                ("A good question names:", ["measure and population", "only vibes", "only colours", "only file size"], "measure and population"),
                ("Limitations matter because:", ["scope of claims", "CSV forbids means", "Python fails", "charts illegal"], "scope of claims"),
                ("Fishing without a question risks:", ["misleading stories", "faster CPUs", "UTF-8", "headers"], "misleading stories"),
            ],
            "Rewrite a vague question into an answerable one with measure + population.",
            "Screenshot of plan + numeric answer.",
        ),
        7: _pack(
            t,
            "Filtering keeps rows matching a rule. Grouping splits data to summarise each group.",
            [
                (
                    "Filter",
                    "```python\n"
                    "math = [r for r in rows if r[\"subject\"].lower() == \"math\"]\n"
                    "```\n"
                    "Combine rules with `and`/`or`. Keep original list intact.",
                ),
                (
                    "Group-by mental model",
                    "Dictionary of lists: key = group label, value = list of scores. "
                    "```python\n"
                    "from collections import defaultdict\n"
                    "groups = defaultdict(list)\n"
                    "for r in rows:\n"
                    "    groups[r[\"subject\"]].append(int(r[\"score\"]))\n"
                    "```\n"
                    "Then mean each group.",
                ),
                (
                    "Pivot thinking",
                    "Teacher dashboards often need subject × statistic. "
                    "Produce a small text pivot: subject | count | mean | pass_rate.",
                ),
            ],
            "groups = {}\nfor r in rows:\n    groups.setdefault(r[\"subject\"], []).append(int(r[\"score\"]))",
            [
                "Implement group means by subject",
                "Filter one gender or section if column exists (add column if needed)",
                "Print a sorted table by mean descending",
            ],
            [("filter", "Keep matching rows"), ("group-by", "Split then summarise"), ("pivot", "Table of group stats")],
            ["Filter programmatically", "Group and aggregate", "Sort summary tables"],
            [
                ("Filter does:", ["select rows by rule", "delete CSV format", "train AI always", "sort disks"], "select rows by rule"),
                ("Group-by needs a key such as:", ["subject", "random RGB only", "file size only", "CPU temp"], "subject"),
                ("setdefault/defaultdict helps:", ["bucket rows", "draw pies only", "hash passwords for web", "open images"], "bucket rows"),
            ],
            "Explain filter vs group-by with a school example.",
            "Screenshot of group summary table.",
        ),
        8: _pack(
            t,
            "Joining combines tables that share a key (e.g. student_id in scores and in profiles).",
            [
                (
                    "Why join",
                    "Normalised data lives in multiple files: students.csv (id, name, class) and scores.csv (id, subject, score). "
                    "Join on id to analyse name + score together.",
                ),
                (
                    "Join types (conceptual)",
                    "Inner: only keys in both. Left: all left rows, match right when present, else missing. "
                    "Missing matches create nulls — handle them.",
                ),
                (
                    "Implement simple inner join",
                    "Index the right table in a dict by key → row. Loop left rows and merge fields into new dicts. "
                    "Detect missing keys and count unmatched.",
                ),
            ],
            "by_id = {r[\"id\"]: r for r in students}\nfor s in scores:\n    stu = by_id.get(s[\"id\"])\n    if stu: merged.append({**stu, **s})",
            [
                "Make students.csv and scores.csv with shared ids",
                "Inner-join and write merged.csv",
                "Report how many score rows had no student match",
            ],
            [("key", "Field used to match rows"), ("inner join", "Intersection of keys"), ("unmatched", "Rows without partner")],
            ["Justify multi-table design", "Perform an inner join in Python", "Report unmatched keys"],
            [
                ("Join key example:", ["student_id", "random colour", "chart type", "mean only"], "student_id"),
                ("Inner join keeps:", ["matching keys in both", "all left only always", "no rows", "headers only"], "matching keys in both"),
                ("Unmatched scores mean:", ["orphan foreign keys", "perfect data", "UTF-8 fail only", "always mean 0"], "orphan foreign keys"),
            ],
            "Why store students and scores separately instead of one giant sheet forever?",
            "Screenshot of merged sample + unmatched count.",
        ),
        9: _pack(
            t,
            "A tiny analysis script or notebook: reproducible steps from raw file to insight.",
            [
                (
                    "Reproducibility",
                    "Anyone re-running your script on the same CSV should get the same numbers. "
                    "Hard-code paths carefully; put parameters (threshold, input path) near the top.",
                ),
                (
                    "Script structure",
                    "1 constants 2 load 3 clean 4 analyse 5 output files/prints. "
                    "Functions for load_csv, clean_row, summarise. "
                    "No analysis buried only in interactive typing you cannot replay.",
                ),
                (
                    "Documentation",
                    "Top comment: dataset description, date, author, question answered. "
                    "That is professional data work hygiene.",
                ),
            ],
            "# config\nPATH = \"clean_marks.csv\"\nPASS = 50\n# load … clean … print summary … save chart",
            [
                "Build analysis_week09.py answering one fixed question end-to-end",
                "Outputs summary.txt + optional chart",
                "Header comment documents dataset + question",
            ],
            [("reproducible", "Same input → same result"), ("pipeline", "Ordered data steps")],
            ["Ship a replayable analysis script", "Structure code in stages", "Document the question"],
            [
                ("Reproducible analysis means:", ["re-run yields same numbers", "numbers change randomly", "no CSV", "only screenshots"], "re-run yields same numbers"),
                ("Config thresholds belong:", ["near top constants", "hidden in binaries", "only in email", "nowhere"], "near top constants"),
                ("Pipeline order start:", ["load then clean", "chart then invent data", "delete then guess", "upload only"], "load then clean"),
            ],
            "List the stages of your pipeline and files written.",
            "Screenshot of script header + outputs.",
        ),
        10: _pack(
            t,
            "Dashboards: choose inputs (filters) and metrics users watch. Not all charts belong on page one.",
            [
                (
                    "Metric design",
                    "Primary metric answers the main job (e.g. class pass rate). "
                    "Secondary metrics explain it (mean, n students, by subject). "
                    "Too many metrics = noise.",
                ),
                (
                    "Filters as inputs",
                    "User picks subject or term → recompute metrics. "
                    "In a simple app this is input() menus; later GUI/web forms.",
                ),
                (
                    "Layout sketch",
                    "Top title + date of data. Big number KPI. Table of breakdown. One chart. Footer source. "
                    "Draw this on paper before coding.",
                ),
            ],
            "KPI: pass_rate\nFilters: subject\nBreakdown: table by subject\nChart: bars of means",
            [
                "Paper or text mock of a teacher dashboard for your dataset",
                "Implement a menu: (1) overall KPI (2) by subject (3) quit",
                "Use functions for each view",
            ],
            [("KPI", "Key metric"), ("filter input", "User choice that narrows data"), ("breakdown", "Split of the KPI")],
            ["Select KPIs", "Mock a dashboard", "Implement menu views"],
            [
                ("A KPI should:", ["match the user’s main job", "be random always", "hide n", "be 20 charts"], "match the user’s main job"),
                ("Filters let users:", ["narrow data", "change Python version", "format C:", "remove headers forever"], "narrow data"),
                ("Too many metrics cause:", ["noise", "faster joins", "automatic integrity", "UTF8"], "noise"),
            ],
            "Justify your one primary KPI for a school teacher.",
            "Screenshot of menu dashboard views.",
        ),
        11: _pack(
            t,
            "Batch vs streaming: process whole files at once vs continuous data. Concepts and trade-offs.",
            [
                (
                    "Batch",
                    "Classic classwork: read entire CSV, analyse, write results. Simple, easy to debug, fine until data huge.",
                ),
                (
                    "Streaming idea",
                    "Process line-by-line without loading all memory; or process events as they arrive (sensors, logs). "
                    "You update running counts: n, sum. You may never store every raw row.",
                ),
                (
                    "When it matters",
                    "Phone with huge log file; live score ticker. For school CSVs, batch is fine — but know the vocabulary for exams/jobs.",
                ),
            ],
            "n = s = 0\nfor line in f:\n    v = int(line)\n    n += 1; s += v\nprint(s/n)",
            [
                "Implement mean of a large number file in streaming style (one pass)",
                "Contrast: also load all into list and mean — compare code",
                "Write short note: memory trade-off",
            ],
            [("batch", "Process complete dataset"), ("streaming/one-pass", "Update as data arrives"), ("running sum", "Accumulate without storing all")],
            ["Contrast batch vs stream", "Write one-pass statistics", "State memory trade-off"],
            [
                ("Streaming is helpful when:", ["data is huge or continuous", "always only 3 rows", "no numbers", "only PDF"], "data is huge or continuous"),
                ("Running mean needs:", ["count and sum (or equivalent)", "only max", "only charts", "joins always"], "count and sum (or equivalent)"),
                ("Batch analysis typically:", ["loads then computes", "never loads", "only sensors", "only encryption"], "loads then computes"),
            ],
            "When would streaming be overkill for school marks?",
            "Screenshot of one-pass program.",
        ),
        12: _pack(
            t,
            "Data ethics: privacy, consent, bias, and careful claims.",
            [
                (
                    "Personal data",
                    "Names, phone numbers, health, and student IDs need care. "
                    "Do not publish class CSVs with real full names on public websites. "
                    "Anonymise: Student_01 or hash IDs for demos.",
                ),
                (
                    "Bias and fairness",
                    "If attendance data under-represents a group, conclusions may harm that group. "
                    "Ask: who is missing from this file? What decisions might this wrong table cause?",
                ),
                (
                    "Honest communication",
                    "Do not overclaim causality from a classroom sample. "
                    "Say “in this dataset” not “all students nationwide”.",
                ),
            ],
            "Policy: no public upload of real phones/emails; demo data only for portfolio.",
            [
                "Anonymise a CSV (replace names with codes); save anon.csv",
                "Write 8–10 sentence ethics memo for your project data",
                "List two biased conclusions you refuse to draw",
            ],
            [("anonymise", "Remove/replace identifying fields"), ("bias", "Systematic skew"), ("consent", "Permission to use data")],
            ["Anonymise demo data", "Write ethics constraints", "Limit claims"],
            [
                ("Publishing real student phones publicly is:", ["unsafe/unethical", "required for CSV", "a chart type", "UTF-8"], "unsafe/unethical"),
                ("Anonymising helps:", ["reduce identity risk", "increase mean", "sort faster always", "join keys magically"], "reduce identity risk"),
                ("“All teens nationwide” from one class is:", ["overclaim", "perfect science", "inner join", "batch job"], "overclaim"),
            ],
            "What will you refuse to put in a public portfolio dataset and why?",
            "Screenshot of anon.csv sample + ethics memo text.",
        ),
        13: _pack(
            t,
            "Exports for humans: clear tables, CSV for analysts, short written insights for non-technical readers.",
            [
                (
                    "Audience",
                    "Principal may want one paragraph + one table, not raw dumps. "
                    "Analyst peer may want clean CSV + data dictionary (column meanings).",
                ),
                (
                    "Data dictionary",
                    "For each column: name, meaning, type, example, allowed range. "
                    "Prevents misuse (e.g. treating ID as a quantity).",
                ),
                (
                    "Narrative structure",
                    "Context → key numbers → chart → limitation → recommended action. "
                    "Keep adjectives honest.",
                ),
            ],
            "Column score: int 0-100, test percentage points, e.g. 78",
            [
                "Write data_dictionary.md for your class CSV",
                "Produce principal_summary.txt (≤15 lines) with 3 numbers + 1 action",
                "Export the underlying clean.csv",
            ],
            [("data dictionary", "Column documentation"), ("insight", "Interpreted finding"), ("actionable", "Suggests a next step")],
            ["Write a data dictionary", "Produce non-technical summary", "Ship clean export"],
            [
                ("Data dictionary describes:", ["columns", "only colours", "CPU", "only filenames"], "columns"),
                ("Non-technical summary should include:", ["key numbers + plain meaning", "raw dumps only", "source code only", "machine code"], "key numbers + plain meaning"),
                ("Actionable insight suggests:", ["a next step", "random emoji", "deleting Python", "hiding n"], "a next step"),
            ],
            "Paste your principal summary and note what you left out on purpose.",
            "Screenshot of dictionary + summary files.",
        ),
        14: _pack(
            t,
            "Automate a weekly report: same script, new CSV drop-in, outputs refresh.",
            [
                (
                    "Automation ideas",
                    "Parameters: input path, pass mark, output folder. "
                    "Script prints “Report generated: …” with timestamp. "
                    "Avoid click-only Excel steps you cannot replay.",
                ),
                (
                    "Folder contract",
                    "`incoming/week.csv` → script → `reports/YYYY-MM-DD/summary.txt` + chart. "
                    "Document the contract so another student can run it.",
                ),
                (
                    "Failure modes",
                    "Missing file, empty file, wrong headers. "
                    "Check headers with `if reader.fieldnames != expected: raise SystemExit(\"bad headers\")`.",
                ),
            ],
            "expected = [\"name\",\"subject\",\"score\"]\nif list(reader.fieldnames) != expected:\n    raise SystemExit(\"bad headers\")",
            [
                "Build weekly_report.py with path constants",
                "Validate headers; write dated report folder",
                "Run twice on two CSVs to prove replay",
            ],
            [("automation", "Repeatable unattended-ish run"), ("header validation", "Check columns before analyse"), ("timestamp", "When report was generated")],
            ["Automate report generation", "Validate inputs", "Use an output folder scheme"],
            [
                ("Header validation prevents:", ["analysing wrong columns", "all ethics issues", "need for mean", "UTF-8"], "analysing wrong columns"),
                ("Dated output folders help:", ["organise runs", "break CSV", "remove keys", "join automatically"], "organise runs"),
                ("Automation value is:", ["replay with new data", "one manual only forever", "no numbers", "random charts"], "replay with new data"),
            ],
            "Describe your folder contract and how a classmate runs the report.",
            "Screenshot of two report runs.",
        ),
        15: _pack(
            t,
            "App shell: form-like input adds rows into a table file — the start of a data app.",
            [
                (
                    "Form → table",
                    "Menu: Add record / List / Save / Quit. "
                    "Fields validated (score 0–100). "
                    "Persist to CSV so data survives restarts.",
                ),
                (
                    "Validation UX",
                    "On bad input, message and re-ask; do not crash. "
                    "Confirm saves. Show last 5 rows after add.",
                ),
                (
                    "Scope control",
                    "Do not build a full web app yet unless free time — solid CLI data app is the goal.",
                ),
            ],
            "def add_row(rows):\n    name = input(\"Name: \").strip()\n    ...\n    rows.append({...})",
            [
                "Implement data_app.py: add/list/save/load CSV",
                "Validate score range",
                "Reload file on start if exists",
            ],
            [("persist", "Save beyond memory"), ("validate", "Reject bad field values"), ("CRUD-lite", "Create/read actions")],
            ["Build input form loop", "Persist to CSV", "Validate fields"],
            [
                ("Persist means:", ["write durable file", "only print", "only RAM forever", "draw chart"], "write durable file"),
                ("Score 150 should:", ["be rejected", "be stored silently", "crash OS", "become header"], "be rejected"),
                ("Load on start enables:", ["continue previous data", "delete Python", "break CSV rules", "skip validation forever"], "continue previous data"),
            ],
            "Walk through what happens when user enters a bad score.",
            "Screenshot of add + list after restart load.",
        ),
        16: _pack(
            t,
            "Capstone: small data app or analysis pack with chart, clean data, insight write-up, ethics note.",
            [
                (
                    "Deliverable options",
                    "A) Teacher marks analyser (CSV in → summary + chart + report). "
                    "B) Mini data app that collects and analyses. "
                    "Pick one and finish polish, not half of both.",
                ),
                (
                    "Rubric",
                    "Loads real CSV; cleaning documented; ≥2 metrics; ≥1 chart or clear table pivot; "
                    "written insight + limitation + ethics; reproducible script; sample data included.",
                ),
                (
                    "Demo script",
                    "Prepare a 2-minute demo path: show raw → run → key number → chart → limitation.",
                ),
            ],
            "# Capstone folder:\n# data/raw.csv data/clean.csv src/analyse.py reports/summary.txt reports/chart.png README.txt",
            [
                "Build complete capstone folder as above",
                "README: how to run, question answered, ethics",
                "Self-check against rubric before submission",
            ],
            [("capstone", "End-of-course integrated project"), ("rubric", "Grading criteria"), ("demo path", "Rehearsed show")],
            ["Integrate the term’s skills", "Document run steps", "Include ethics and limits"],
            [
                ("Capstone should answer:", ["a clear question with evidence", "nothing", "only comedy", "only ethics with no data"], "a clear question with evidence"),
                ("Sample data in submission helps:", ["teacher re-run", "hide bugs", "remove metrics", "break charts"], "teacher re-run"),
                ("Ethics note is:", ["required for responsible data work", "optional fluff always", "a chart type", "a join key"], "required for responsible data work"),
            ],
            "Capstone report: question, methods, results, limits, ethics, next steps.",
            "Screenshot set: folder structure, main output, chart/table.",
        ),
    }
    if week in banks:
        return banks[week]
    return _generic_tech("python-data-apps", week, 16, t, d)


# ── Domain technical engines (real subject matter only) ──────


def _lectures_triple(h1, b1, h2, b2, h3, b3):
    return [(h1, b1), (h2, b2), (h3, b3)]


def _py_dev(week: int, topic: str) -> dict:
    """24-week Python Developer — real language/tooling content."""
    t, d = _split_topic(topic)
    W = {
        1: (
            "Install CPython from python.org (or school image). Check `python --version` / `py --version` on Windows. "
            "Know python vs python3. Create a project folder; save `hello.py`. Run from that folder so imports later resolve. "
            "Use a code editor; enable 4-space indent. Understand stderr vs stdout when errors print.",
            "Script anatomy: shebang optional on Windows; encoding comments rarely needed on py3; "
            "`if __name__ == \"__main__\":` guard for library-friendly files. First script: argv later; this week print + simple variables.",
            "Troubleshooting PATH, wrong interpreter in the editor, and running the wrong file. "
            "Create `notes.md` with install path and version for your lab machine.",
            'print("ok")\nimport sys\nprint(sys.version)',
            ["Verify interpreter version", "hello.py runs from project folder", "Document install notes"],
            [("CPython", "Default Python implementation"), ("PATH", "Where OS finds python.exe"), ("__main__", "Entry script pattern")],
        ),
        2: (
            "Types: int, float, str, bool, NoneType. Assignment rebinds names. "
            "Mutability preview (lists later). `id()` curiosity only. Prefer expressive names.",
            "Operators: arithmetic, floor div, mod, **; comparisons; boolean `and or not`; "
            "operator precedence and parentheses. Augmented assignment.",
            "Conversions: int/float/str/bool rules (bool of empty string vs \"0\"). "
            "Chained comparisons `0 <= x <= 100`.",
            "x = 2**3 + 1\nprint(type(x), x)\nprint(bool(\"\"), bool(\"0\"))",
            ["Type quiz program", "Expression sheet computed in code", "Safe conversion helper"],
            [("rebind", "Name points at new object"), ("precedence", "Order of ops"), ("None", "Null value")],
        ),
        3: (
            "Boolean context: what values are truthy/falsey. if/elif/else structure, colon, indent blocks.",
            "Nested if vs elif flattening. Guard clauses: validate then return early in functions later; "
            "this week print-based. Ternary expression `a if cond else b` sparingly.",
            "Case study: fee calculator with discounts and invalid input messages without crashing when possible.",
            "score = 73\nband = \"A\" if score >= 70 else \"B\" if score >= 60 else \"C\"\nprint(band)",
            ["Multi-branch grader", "Discount rules", "Invalid input messages"],
            [("truthy", "Value treated as True in if"), ("guard", "Early validation branch"), ("elif", "Chained alternative")],
        ),
        4: (
            "while for unknown repetition; for for known iterables. range(start, stop, step). Infinite loop causes and Ctrl+C.",
            "break, continue, else-on-loop (runs if no break) — know existence. Nested loops and complexity awareness.",
            "Patterns: accumulation, search with flag, menu loops, retry with attempt counter.",
            "for i in range(1, 4):\n    for j in range(1, 4):\n        print(i, j, i*j)",
            ["Nested table", "Search first match", "Retry limit loop"],
            [("iterable", "Object for can walk"), ("accumulate", "Running total"), ("flag", "Boolean state")],
        ),
        5: (
            "def, parameters, return, docstring. Positional vs keyword args. Defaults (mutable default trap later).",
            "Scope LEGB in practical terms: locals vs globals; avoid global until necessary; return values instead.",
            "Decomposition: split a gradebook into functions pure vs with I/O. Type hints optional `def f(x: int) -> int`.",
            "def clamp(n, lo, hi):\n    return max(lo, min(hi, n))",
            ["Pure math helpers", "I/O wrapper main()", "Docstring on two functions"],
            [("pure function", "No side effects"), ("default arg", "Optional parameter"), ("docstring", "Usage string")],
        ),
        6: (
            "list methods; tuple immutability and packing; set uniqueness and & | - ; dict key→value maps.",
            "Choose structure: list when order/dupes matter; set for membership; dict for labels; tuple for fixed records.",
            "Comprehensions: `[x*2 for x in xs if x>0]`, dict/set comps. Readability limit — don’t nest heavily.",
            "ages = {\"Ada\":16,\"Ben\":15}\nprint({n:a for n,a in ages.items() if a>=16})",
            ["Word frequency with dict", "Unique items with set", "List comp filter"],
            [("hashable", "Can be dict key"), ("membership", "in test"), ("comprehension", "Compact build")],
        ),
        7: (
            "str methods for cleaning; encoding awareness; pathlib optional preview. "
            "Text vs binary file modes. with open.",
            "Read patterns: read, readline, iterate lines. Write and append. CSV touch using csv module briefly.",
            "Path issues on Windows backslashes; use pathlib or raw paths. "
            "Process a log file: count ERROR lines.",
            "from pathlib import Path\ntext = Path(\"a.txt\").read_text(encoding=\"utf-8\")",
            ["Write/read report", "Count keywords in file", "csv read of small file"],
            [("pathlib", "OO paths"), ("text mode", "Decoded str I/O"), ("append", "Add to file end")],
        ),
        8: (
            "Exception hierarchy idea: Exception, ValueError, TypeError, KeyError, FileNotFoundError, ZeroDivisionError.",
            "try/except/else/finally. Catch specific types. Re-raise. Never bare `except:`. "
            "Validate with exceptions vs return codes.",
            "Design a `safe_int(prompt)` retry helper. Log error messages for users vs developers.",
            "try:\n    n = int(\"x\")\nexcept ValueError as e:\n    print(\"bad\", e)",
            ["safe_int", "File open with friendly error", "Multi-except demo"],
            [("stack trace", "Error location printout"), ("raise", "Throw exception"), ("finally", "Always runs")],
        ),
        9: (
            "import module; from x import y; package folders with __init__.py; module search path myth-busting.",
            "Standard library tour: math, random, statistics, datetime, json, pathlib, collections.",
            "Write a small reusable module `util_stats.py` imported by `main.py`. Avoid circular imports.",
            "import statistics as stats\nprint(stats.mean([1,2,3]))",
            ["Two-file project", "Use datetime for stamp", "collections.Counter exercise"],
            [("module", "Importable .py"), ("package", "Folder of modules"), ("stdlib", "Batteries included")],
        ),
        10: (
            "venv creation: `python -m venv .venv`; activate Windows `\\.venv\\Scripts\\activate`. "
            "pip install; freeze requirements.txt; why isolation matters.",
            "Pinning versions, upgrading carefully, school lab constraints without admin rights.",
            "Create project with requests OR any allowed lib; document install. "
            "If network blocked, still demonstrate venv + freeze of empty env and local module.",
            "pip freeze > requirements.txt",
            ["Create venv", "Install one package or local editable layout", "requirements.txt"],
            [("venv", "Isolated environment"), ("pip", "Package installer"), ("pin", "Lock version")],
        ),
        11: (
            "class defines blueprint; instance attributes in __init__; methods with self; "
            "repr for debugging.",
            "Encapsulation by convention (_private). Properties optional. "
            "Class attributes vs instance attributes.",
            "Model a simple domain: BankAccount or Student with methods deposit/apply_score.",
            "class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def dist0(self):\n        return (self.x**2+self.y**2)**0.5",
            ["Class with 3 methods", "Two instances interact", "Custom __repr__"],
            [("instance", "Object created from class"), ("self", "Current instance"), ("__init__", "Constructor")],
        ),
        12: (
            "Inheritance: subclass extends base; super().__init__. Method overriding. isinstance checks.",
            "Composition vs inheritance: “has-a” often clearer than deep trees. "
            "ABC idea optional.",
            "Example hierarchy Employee/Manager payroll OR Shape area methods; prefer composition for a Logger inside Service.",
            "class Animal:\n    def speak(self): return \"...\"\nclass Dog(Animal):\n    def speak(self): return \"woof\"",
            ["Override method", "Composition example", "When not to inherit short note"],
            [("subclass", "Derived class"), ("super", "Parent access"), ("composition", "Object inside object")],
        ),
        13: (
            "JSON as data interchange: objects/arrays/strings/numbers/bool/null. json.loads/dumps; load/dump files.",
            "HTTP mental model: URL, method GET/POST, status codes 200/404/500, headers, JSON body. "
            "requests.get(url).json() if allowed; else urllib.",
            "Public demo API or local JSON file mock. Handle timeouts and non-200 statuses.",
            "import json\nprint(json.dumps({\"ok\": True}))",
            ["Parse JSON file", "Build JSON export", "HTTP GET of JSON (or mock)"],
            [("JSON", "Text data format"), ("status code", "HTTP result class"), ("deserialize", "Text→objects")],
        ),
        14: (
            "assert for simple checks. pytest vs unittest awareness; write functions that return values for testing.",
            "Arrange-Act-Assert pattern. Edge cases: empty, zero, None, large. "
            "Test file naming test_*.py.",
            "Write 5 asserts or pytest tests for pure functions from earlier weeks.",
            "def add(a,b): return a+b\nassert add(2,3)==5",
            ["Test pure functions", "Document edge cases", "Failing test then fix"],
            [("assertion", "Check that must be true"), ("edge case", "Boundary input"), ("regression", "Bug that returns")],
        ),
        15: (
            "Debugging: reproduce, minimise, form hypothesis, print/log, binary search the code. "
            "Read tracebacks bottom-up.",
            "Tools: print, logging module basics, editor breakpoints if available. "
            "Rubber-duck the control flow.",
            "Take a deliberately buggy script and produce a short debug log of hypotheses tested.",
            "import logging\nlogging.basicConfig(level=logging.DEBUG)\nlogging.debug(\"x=%s\", x)",
            ["Fix seeded bugs", "Use logging", "Write debug report"],
            [("traceback", "Stack of calls"), ("reproduce", "Make bug happen again"), ("logging", "Structured messages")],
        ),
        16: (
            "Git: init, status, add, commit, log, diff. .gitignore for venv and __pycache__. "
            "Commit messages imperative and specific.",
            "Branch idea; clone/push only if remote available. "
            "Never commit secrets.",
            "Local repo for a small project with 3 meaningful commits.",
            "git init\ngit add .\ngit commit -m \"Add mean helper and tests\"",
            ["Init repo", "Three commits", ".gitignore"],
            [("commit", "Snapshot"), ("staging", "Index before commit"), (".gitignore", "Untracked patterns")],
        ),
        17: (
            "PEP 8 spirit: naming, line length, imports order, blank lines, spaces around ops. "
            "Tools: ruff/flake8/black awareness.",
            "Readable code beats clever one-liners. Comments for why. "
            "Dead code removal.",
            "Reformat an ugly script to PEP 8 style manually.",
            "# good\nmean_score = total / count",
            ["Lint a file by hand checklist", "Rename variables", "Split long function"],
            [("PEP 8", "Style guide"), ("lint", "Static style/error check"), ("refactor rename", "Improve names")],
        ),
        18: (
            "argparse: positional vs optional flags, types, help text, defaults. "
            "Build CLI that processes a file path.",
            "Exit codes 0 success non-zero failure. "
            "Sys.argv minimal vs argparse.",
            "CLI: `--input file --threshold 50` printing pass rate.",
            "import argparse\np=argparse.ArgumentParser()\np.add_argument(\"--threshold\", type=int, default=50)",
            ["argparse tool", "Help text useful", "Non-zero exit on missing file"],
            [("CLI", "Command line interface"), ("flag", "Optional switch"), ("exit code", "Process status int")],
        ),
        19: (
            "Validation layers: type checks, range checks, regex simple patterns, schema idea. "
            "Fail fast with clear messages.",
            "Normalise inputs (strip, casefold email domains later). "
            "Return Result objects or raise — pick one style.",
            "Validate registration fields: name non-empty, age 5–100, score 0–100.",
            "def require_score(s):\n    n=int(s)\n    if not 0<=n<=100: raise ValueError(\"score\")\n    return n",
            ["Validator module", "Friendly error strings", "Tests for validators"],
            [("sanitize", "Clean input"), ("schema", "Expected shape"), ("fail fast", "Error early")],
        ),
        20: (
            "SQLite: database file, tables, rows, SQL SELECT/INSERT/UPDATE/DELETE basics. "
            "sqlite3 module connect, cursor, execute, commit.",
            "Parameterised queries `?` placeholders — never f-string SQL with user input. "
            "Primary keys.",
            "Create students table; insert; query by name; update score.",
            "import sqlite3\ncon=sqlite3.connect(\"app.db\")\ncon.execute(\"CREATE TABLE IF NOT EXISTS t(id INTEGER PRIMARY KEY, name TEXT)\")",
            ["Create DB schema", "CRUD operations", "Parameterised SELECT"],
            [("SQL", "Query language"), ("parameterised", "Safe query bind"), ("commit", "Persist transaction")],
        ),
        21: (
            "Library module design: public functions, hide helpers with _. "
            "Version variable. Example usage in README.",
            "Avoid side effects on import. "
            "Expose a small API surface.",
            "Ship `textkit.py` with word_count, avg_word_len imported by demo.",
            "# textkit.py\ndef word_count(s): return len(s.split())",
            ["Library + demo", "No side effects on import", "README usage"],
            [("API surface", "What callers use"), ("side effect", "Change outside return"), ("helper", "Internal function")],
        ),
        22: (
            "Refactoring: extract function, rename, remove duplication, simplify conditionals. "
            "Keep tests green while refactoring.",
            "Code smells: long function, magic numbers, dead parameters. "
            "Before/after metrics lines of code not the goal — clarity.",
            "Refactor a messy 80-line script into modules with same behaviour.",
            "# extract\ndef load_rows(path): ...\ndef summarise(rows): ...",
            ["Before/after files", "List smells fixed", "Behaviour unchanged proof"],
            [("refactor", "Improve structure"), ("duplication", "Repeated logic"), ("magic number", "Unexplained literal")],
        ),
        23: (
            "Project layout: src/ or flat package, tests/, data/, README, requirements.txt. "
            "Relative imports carefully.",
            "Entry points: python -m package. Entry scripts. "
            "Config via env or argparse not hardcoded secrets.",
            "Reorganise capstone skeleton into clean layout.",
            "project/\n  README.md\n  requirements.txt\n  app/\n    __init__.py\n    main.py\n  tests/",
            ["Create layout", "Move code into package", "README run instructions"],
            [("package layout", "Folder structure"), ("entry point", "How program starts"), ("README", "Human run guide")],
        ),
        24: (
            "Capstone: multi-file Python app solving a real small problem (CLI tool, grader, inventory, quiz engine). "
            "Must include tests or asserts, README, sample data.",
            "Quality: error handling, validation, clear UX CLI, no crashes on bad input common cases.",
            "Demo + limitations write-up. Code review checklist self-pass.",
            "# main.py orchestrates modules validated + tested",
            ["Complete multi-file project", "README + sample run", "Self review checklist done"],
            [("capstone", "Final integrated project"), ("acceptance", "Done means criteria met")],
        ),
    }
    if week not in W:
        return _generic_tech("python-developer", week, 24, t, d)
    l1, l2, l3, ex, lab, vocab = W[week]
    return _pack(
        t,
        f"Python Developer week {week}: {d}. Three technical sessions — concepts, code technique, applied build.",
        _lectures_triple(
            f"{t} — foundations",
            l1,
            f"{t} — technique",
            l2,
            f"{t} — apply & pitfalls",
            l3,
        ),
        ex,
        lab if isinstance(lab, list) else [lab],
        vocab,
        [f"Apply: {t}", "Write working code for the lab", "Explain trade-offs in your own words"],
        _mcq_topic(t, d),
        f"Explain the core idea of “{t}” with a short code mental model and one mistake to avoid.",
        f"Screenshot of working code/output for week {week}: {t}.",
    )


def _mcq_topic(title: str, detail: str):
    return [
        (f"Which statement best matches “{title}”?",
         [f"It is about: {detail}", "It is only about wallpapers", "It deletes the OS", "It ignores data always"],
         f"It is about: {detail}"),
        ("When code fails first look at:",
         ["The error message/traceback", "Random settings forever", "Only the filename length", "Disk colour"],
         "The error message/traceback"),
        ("A solid lab solution should:",
         ["Run and match the brief", "Be empty", "Crash always", "Hide all output"],
         "Run and match the brief"),
    ]


def _website(week: int, topic: str) -> dict:
    t, d = _split_topic(topic)
    bodies = {
        1: (
            "The browser requests a URL over the network; a server returns HTML/CSS/JS/assets. "
            "DNS maps names to IPs. HTTPS encrypts. View-source shows HTML the browser received. "
            "Static vs dynamic: files as-is vs generated per request.",
            "DevTools Elements/Network overview. Status codes 200/301/404. "
            "Local workflow: write `index.html`, open in browser or use a tiny static server.",
            "URL parts: scheme, host, path, query. Relative vs absolute links. "
            "Project folder discipline for multi-page sites.",
            "<!DOCTYPE html>\n<html lang=\"en\">\n<head><meta charset=\"utf-8\"><title>Demo</title></head>\n<body><h1>Hello</h1></body></html>",
        ),
        2: (
            "Document outline with h1–h6. One h1 per page typically. p for paragraphs; ul/ol/li lists; strong/em. "
            "HTML is structure/meaning, not final look.",
            "Nesting rules; indent for humans. Invalid nesting causes accessibility/CSS pain. "
            "Comments <!-- -->.",
            "Build a one-page notes sheet: title, intro, two lists, two subheadings.",
            "<h1>Course</h1>\n<p>Welcome.</p>\n<ul><li>HTML</li><li>CSS</li></ul>",
        ),
        3: (
            "a href for links; target and rel for new tabs carefully. img src alt width. "
            "Semantic tags: header nav main article section footer — improve structure/a11y/SEO.",
            "alt text describes purpose not “image”. Decorative images empty alt. "
            "Figures and figcaption when useful.",
            "Multi-section page with nav jump links #id.",
            "<a href=\"about.html\">About</a>\n<img src=\"photo.jpg\" alt=\"Lab classroom\">",
        ),
        4: (
            "CSS attaches via link stylesheet. Selectors: element, class, id, descendant. "
            "Cascade and specificity basics (id > class > element).",
            "Colour, font-family, font-size, line-height, text-align. Units px/rem. "
            "Google Fonts load carefully (privacy/performance).",
            "Box model: content padding border margin. box-sizing: border-box recommended.",
            "body{font-family:Georgia,serif;line-height:1.5}\n.card{padding:1rem;margin:1rem 0;border:1px solid #ccc}",
        ),
        5: (
            "Flexbox: container display:flex; direction; justify-content; align-items; gap; flex-wrap. "
            "Children flex growth.",
            "Common patterns: nav row, centred hero text, equal-height cards row. "
            "Avoid abs positioning for simple layouts.",
            "Build a header with logo left / links right using flex.",
            ".row{display:flex;gap:1rem;align-items:center;justify-content:space-between}",
        ),
        6: (
            "Responsive: viewport meta; fluid widths; media queries `@media (max-width:600px)`. "
            "Mobile first: base styles small screens, enhance up.",
            "Readable type sizes; tap targets. Images max-width:100%. "
            "Test by resizing browser.",
            "Make last week’s layout stack on narrow screens.",
            "@media (max-width:600px){.row{flex-direction:column}}",
        ),
        7: (
            "Information architecture: pages users need. Shared nav on every page. "
            "Relative paths between folders.",
            "Footer with secondary links. Active page styling. "
            "Consistent header component by copy or later templating.",
            "3-page mini site Home/About/Contact with shared look.",
            "<!-- nav on each page -->\n<nav><a href=\"index.html\">Home</a></nav>",
        ),
        8: (
            "form, label, input types text email password number, textarea, select, button. "
            "name attributes; method get/post conceptual (static sites often no backend).",
            "Validation attributes required min max pattern; still re-validate on server later. "
            "label for= and id association.",
            "Build a contact form UI (no backend required) with clear labels.",
            "<label for=\"em\">Email</label>\n<input id=\"em\" type=\"email\" required>",
        ),
        9: (
            "a11y: keyboard focus, semantic HTML, contrast (text vs background), alt text, "
            "don’t rely on colour alone. Headings in order.",
            "Focus outlines not removed carelessly. Language lang attribute. "
            "Skip link optional advanced.",
            "Audit your site with keyboard only tab through links/forms.",
            "/* poor */ color:#aaa; background:#ddd; /* better contrast needed */",
        ),
        10: (
            "Image formats jpg/png/webp/svg use cases. Compression. width/height to reduce layout shift. "
            "Lazy loading loading=\"lazy\" where appropriate.",
            "Hero images large; icons small. Don’t scale 4k images for 40px UI. "
            "Favicons brief.",
            "Optimise and replace one heavy image; note before/after size.",
            "<img src=\"hero.webp\" alt=\"\" width=\"1200\" height=\"600\" loading=\"lazy\">",
        ),
        11: (
            "JS in browser: script tag defer. querySelector; textContent; addEventListener click. "
            "Change classes for UI state.",
            "Keep JS progressive: site works without JS if possible for content pages. "
            "console.log debugging.",
            "Button toggles a mobile nav class or dark mode class on body.",
            "document.querySelector(\"#btn\").addEventListener(\"click\",()=>{...});",
        ),
        12: (
            "Hosting static files: GitHub Pages, Netlify, PythonAnywhere static, school server. "
            "Upload folder structure intact. HTTPS.",
            "Custom domain later. Cache awareness after deploy. "
            "404 page nice-to-have.",
            "Deploy your mini site or package a zip with run notes if deploy blocked.",
            "# deploy checklist: index.html at site root, asset paths correct",
        ),
        13: (
            "UX writing: clear headings, scannable bullets, button labels as verbs. "
            "Remove lorem when shipping. Error messages specific.",
            "Content hierarchy matches visual hierarchy. "
            "Tone consistent school/professional.",
            "Rewrite one page removing fluff; measure word count drop.",
            "Primary button: \"Submit application\" not \"Click here\"",
        ),
        14: (
            "SEO basics: unique title; meta description; one h1; descriptive URLs; alt text; "
            "fast load; mobile friendly. No keyword stuffing.",
            "Open Graph optional. Sitemap/robots later for larger sites.",
            "Write titles/descriptions for your three pages.",
            "<title>CloudCity Club — Home</title>\n<meta name=\"description\" content=\"…\">",
        ),
        15: (
            "Project: multi-section landing — hero, about, features, FAQ, contact. "
            "Consistent design tokens: colours, type scale, spacing.",
            "Self QA checklist browser widths; broken links; forms labels.",
            "Build full landing to standard.",
            "/* CSS variables */\n:root{--ink:#111;--bg:#f6f3ee;--accent:#0b6b75}",
        ),
        16: (
            "Capstone site personal/business: ≥4 pages or long landing equal depth; responsive; accessible basics; "
            "deployed or zipped; README.",
            "Rubric: structure, visuals, content quality, responsiveness, a11y, professionalism.",
            "Polish week: fix contrast, spacing, copy, image weight.",
            "<!-- final site root with clear nav -->",
        ),
    }
    if week not in bodies:
        return _generic_tech("website-development", week, 16, t, d)
    l1, l2, l3, ex = bodies[week]
    return _pack(
        t,
        f"Website Development — {d}. HTML/CSS/JS subject content for three class meetings.",
        _lectures_triple(f"Lecture A: {t}", l1, f"Lecture B: {t}", l2, f"Lecture C: lab technique — {t}", l3),
        ex,
        [f"Implement the week {week} page/site piece for: {t}", "Check in browser at mobile and desktop widths", "Validate structure (headings, alt, labels as applicable)"],
        [("HTML", "Structure"), ("CSS", "Presentation"), ("responsive", "Fits viewports"), ("accessibility", "Usable more people")],
        [f"Build with correct {t} techniques", "Explain structure vs style", "Show responsive behaviour"],
        _mcq_topic(t, d),
        f"Describe the HTML/CSS (or JS) techniques you used for “{t}” and why.",
        f"Screenshot of the page for week {week} (full section visible).",
    )


def _corel(week: int, topic: str) -> dict:
    t, d = _split_topic(topic)
    tips = {
        1: "Document setup: page size (A4/business card), orientation, units mm/inches. Pick tool, Toolbox, Property bar, Docker concept. Save .cdr early. Wireframe vs enhanced view.",
        2: "Rectangle/Ellipse tools; constrain with Ctrl; rounded corners. Select/marquee; Free Transform; size from property bar numeric for precision.",
        3: "Uniform vs fountain fills; outline width/colour; colour palettes CMYK vs RGB intent. Eyedropper. Limit palette early.",
        4: "Artistic text for logos/short words; paragraph text frames for body. Font choice; tracking/kerning intro; convert to curves only when needed (irreversible edits).",
        5: "Rulers, guidelines, snap to objects/guidelines. Align and distribute. Margins: keep content away from trim. Grid for posters.",
        6: "Group/ungroup; weld, trim, intersect for shape building. Order (to front/back). Non-destructive planning before weld.",
        7: "Logo craft: mark + wordmark. Start in black/white silhouette strength. Simple geometry; negative space. Sketch paper first.",
        8: "Variants: mono, reversed, stacked, horizontal. Export PNG transparent; sizing for favicon vs poster. Keep master .cdr.",
        9: "Poster hierarchy: dominant headline, secondary, body, CTA. Margins and alignment axes. Eye path Z/F patterns. Contrast.",
        10: "Bleed for print; safe area; PDF export settings school printer; RGB vs CMYK overview; rich black caution.",
        11: "Brand kit page: logo, colours with values, type samples, do/don’t. Consistency rules sheet.",
        12: "Client brief interpretation; deliverables package flyer or card set; PDF + PNG + source; rationale paragraph.",
    }
    body = tips.get(week, d)
    return _pack(
        t,
        f"CorelDRAW production skills: {d}.",
        _lectures_triple(
            f"Interface & concepts — {t}",
            body + " Teachers demonstrate tool locations; you note shortcut if any on your build.",
            f"Precision craft — {t}",
            "Work with numeric sizes, alignment, and constrained shapes. Professionals type dimensions instead of only eyeballing. "
            "Lock proportions when scaling unless distortion is intentional. Duplicate with controlled offsets for patterns.",
            f"Production output — {t}",
            "Save source .cdr. Export the sharing format required (PNG/PDF). Name files with version Week%02d. "
            "Crit: holds at arm’s length? Enough margin? Limited colours?" % week,
        ),
        f"File: YourName_Week{week:02d}.cdr\nExport preview PNG\nChecklist: page size, margins, alignment, limited colours, hierarchy",
        [
            f"Complete a design study focused on: {t}",
            "Use guides/align for at least three elements",
            "Export PNG preview + keep .cdr",
            "Write 4-line process note: intent, type, colour, one fix you made",
        ],
        [("vector", "Math curves/shapes"), ("bleed", "Print overflow area"), ("hierarchy", "Visual order of importance"), (".cdr", "Corel source file")],
        [f"Execute {t}", "Align cleanly", "Export correctly"],
        _mcq_topic(t, d),
        f"Explain how you used Corel tools for “{t}” (tools + settings).",
        f"Screenshot of Corel workspace showing week {week} design + filename.",
    )


def _scratch_pack(week: int, topic: str, kind: str) -> dict:
    t, d = _split_topic(topic)
    return _pack(
        t,
        f"{'Scratch' if kind=='scratch' else 'Block coding'}: {d}. Events, motion, control, and testing.",
        _lectures_triple(
            f"Blocks & model — {t}",
            f"Topic detail: {d}. In block environments, scripts attach to sprites (or the stage). "
            "Hats (events) start stacks. Order of blocks is execution order. "
            "Predict-before-run: say what will happen, then click green flag.",
            f"Build technique — {t}",
            "Use broadcasts/messages to separate concerns when available. Variables for score/state. "
            "Loops for repetition; if for conditions. Keep scripts short; duplicate sprites carefully. "
            "Costume/backdrop changes are state changes — name costumes meaningfully.",
            f"Debug & polish — {t}",
            "If wrong behaviour: isolate which sprite’s script fires; check condition values; add a say/think debug. "
            "Reset positions on green flag. Credit remixes. Export/share per school rules + screenshot evidence.",
        ),
        f"when green flag clicked\n  // setup for: {t}\n  forever\n    // core behaviour related to {d}",
        [
            f"Build a playable/presentable mini feature for: {t}",
            "Green flag resets cleanly",
            "At least one variable or message if week ≥6",
            "Write 5-line script explanation mapping blocks → meaning",
        ],
        [("sprite", "Character/object"), ("event", "Trigger hat block"), ("variable", "Stored value"), ("broadcast", "Message between scripts")],
        [f"Implement {t}", "Debug with prediction", "Reset on green flag"],
        _mcq_topic(t, d),
        f"Describe your script for “{t}” as when… / then… / if… sentences.",
        f"Screenshot of Scratch/blocks project showing scripts for week {week}.",
    )


def _excel(week: int, topic: str) -> dict:
    t, d = _split_topic(topic)
    L = {
        1: (
            "Workbook = file; worksheet = tab; cell = intersection like B3. Enter text/numbers/dates. "
            "Numbers for calculation must be true numerics (not text). Headers in row 1. Column widths. Freeze optional later.",
            "Navigate: arrows, Ctrl+arrows, Ctrl+Home. Fill handle for series. Undo. "
            "Save .xlsx with class naming. One clean data rectangle — no blank rows inside the table.",
            "Data entry discipline: one fact per cell; no “500 naira” in one cell if you need to sum — put 500 and format currency.",
            "A1:Item B1:Qty C1:Price\nA2:Pen B2:10 C2:50",
        ),
        2: (
            "Formulas begin with =. References update when inputs change. =B2*C2 line total. "
            "SUM AVERAGE MIN MAX. Relative refs fill down.",
            "Order of operations; parentheses. Show formulas mode. Error tips #DIV/0! #VALUE!. "
            "Don’t type results that should be calculated.",
            "Build totals under columns; average; change an input to prove liveness.",
            "D2:=B2*C2\nD10:=SUM(D2:D9)",
        ),
        3: (
            "Sort data by key columns. AutoFilter on headers. "
            "Charts: select data+headers; column/bar/pie/line appropriateness; chart title and axis titles.",
            "Avoid charting total rows twice. Keep source table clean. "
            "Insight cell: one sentence what the chart shows.",
            "Sort, filter a condition, chart top categories.",
            "Insert → Charts → Column; title “Total by Item”",
        ),
        4: (
            "Capstone workbook either scorebook (student, T1,T2,T3, average formula, chart) "
            "or budget (planned/actual/variance). Title block name/date. Number formats.",
            "Optional conditional formatting for fails. Protect structure lightly if taught.",
            "Peer readability test: can a classmate use the sheet without you speaking?",
            "Average: =AVERAGE(B2:D2)\nVariance: =C2-B2",
        ),
    }
    l1, l2, l3, ex = L[week]
    return _pack(
        t,
        f"Excel skills: {d}.",
        _lectures_triple(f"Lecture A — {t}", l1, f"Lecture B — {t}", l2, f"Lecture C — apply — {t}", l3),
        ex,
        [f"Build the week {week} sheet for: {t}", "Include required formulas/structure", "Save YourName_Week%02d_Excel.xlsx" % week],
        [("cell reference", "Address A1"), ("formula", "Starts with ="), ("range", "A1:A10"), ("chart", "Visual of data")],
        [f"Perform {t}", "Use real formulas not typed totals", "Name files properly"],
        [
            ("Formulas start with:", ["=", "#", "@", "%"], "="),
            ("B2 means:", ["column B row 2", "row B col 2", "a macro", "a chart"], "column B row 2"),
            ("SUM(D2:D5) adds:", ["D2 through D5", "only D2", "entire sheet", "nothing"], "D2 through D5"),
        ],
        f"Explain your formulas and sheet layout for week {week}.",
        "Screenshot of the sheet showing formulas or results + filename.",
    )


def _ppt(week: int, topic: str) -> dict:
    t, d = _split_topic(topic)
    L = {
        1: (
            "A slide is a visual aid, not a document. Title slide: topic, name, class. "
            "Layouts from New Slide. Theme sets default fonts/colours — pick once.",
            "Body slides: short headline + ≤6 bullets or one diagram. One idea per slide. "
            "Avoid paragraphs. 24pt+ body when possible.",
            "Build 4-slide skeleton: title, agenda, two content.",
            "Title\n- Point one\n- Point two",
        ),
        2: (
            "Design system: consistent fonts, colours, logo placement, margins from edges. "
            "Align objects; distribute spacing. High-quality images only; crop.",
            "Contrast: light on dark only with sufficient contrast. "
            "SmartArt only if it clarifies process/relationship.",
            "Restyle week 1 deck into a consistent system; remove clutter.",
            "Home → Align → Align Left (for stacked text boxes)",
        ),
        3: (
            "Speaker notes = your script. Transitions: simple Fade. "
            "Animations: emphasise one item, not every bullet.",
            "Rehearse with timer. Presenter View if available. "
            "Backup PDF export.",
            "Add notes to 4 slides; one subtle entrance animation; rehearse out loud.",
            "Notes pane: what you will say, not text copy of bullets only",
        ),
        4: (
            "8–10 slides: Title, Hook, 4–5 teaching, Example, Summary, Q&A. "
            "School-safe specific topic. Apply design + mild motion + notes.",
            "Rubric: message clarity, visual consistency, delivery readiness.",
            "Finish and dry-run 3 minutes.",
            "Slide 1 Title | 2 Why | 3-7 Teach | 8 Example | 9 Summary | 10 Thanks",
        ),
    }
    l1, l2, l3, ex = L[week]
    return _pack(
        t, f"PowerPoint: {d}.",
        _lectures_triple(f"A — {t}", l1, f"B — {t}", l2, f"C — {t}", l3),
        ex,
        [f"Produce deck progress for: {t}", "Save .pptx class name", "Check readability from 2 metres"],
        [("layout", "Slide arrangement"), ("theme", "Shared look"), ("speaker notes", "Presenter script")],
        [f"Apply {t}", "Keep text short", "Stay consistent"],
        [
            ("Best body style:", ["short bullets", "full essays", "6pt walls", "no titles"], "short bullets"),
            ("Animations should be:", ["rare and purposeful", "on every word", "random", "mandatory 3D"], "rare and purposeful"),
            ("Title slide needs:", ["topic and name", "only path", "only clipart", "nothing"], "topic and name"),
        ],
        f"Outline your talk structure and design rules used.",
        "Screenshot of slide sorter or key slides.",
    )


def _word(week: int, topic: str) -> dict:
    t, d = _split_topic(topic)
    L = {
        1: (
            "Word window: title bar, Ribbon (Home/Insert/Layout), document area, status bar (page/word count). "
            "Insertion point. New blank document.",
            "Typing paragraphs: Enter only for new paragraph. Word wrap. Select word/paragraph. Undo/Redo. Find.",
            "Save As first time to class folder; name YourName_Week01.docx; Ctrl+S thereafter; close and reopen to verify.",
            "File → Save As → YourName_Week01_Intro.docx",
        ),
        2: (
            "Font name/size; bold italic underline; font colour sparingly. Alignment left/centre/right/justify. "
            "Line spacing; paragraph spacing before/after — prefer spacing over blank Enter spam.",
            "Bullets and numbered lists. Clear hierarchy: Title, Heading, Body styles intro if available.",
            "Format a 1-page bio with title, two headings, body, one list.",
            "Home → Font / Paragraph groups",
        ),
        3: (
            "Margins; orientation; page size. Headers/footers; page numbers; different first page option. "
            "Insert pictures with wrap text; resize from corners.",
            "Breaks: page break vs extra Enters. Keep with next for headings when taught.",
            "3/4 page report with header name, page #, one image with caption-like text under.",
            "Insert → Header / Page Number / Pictures",
        ),
        4: (
            "Formal letter OR short report 2 pages: sender/receiver or title page block, body structure, closing. "
            "Consistent fonts; 2.5cm margins-ish; saved PDF optional.",
            "Proofread: spelling, spacing, name spelling. Read aloud once.",
            "Submit final with clear file name Week04_Capstone.",
            "Block letter layout or Introduction / Body / Conclusion report",
        ),
    }
    l1, l2, l3, ex = L[week]
    return _pack(
        t, f"Microsoft Word: {d}.",
        _lectures_triple(f"A — {t}", l1, f"B — {t}", l2, f"C — {t}", l3),
        ex,
        [f"Document task for: {t}", "Correct file naming", "Print-layout check"],
        [("Ribbon", "Tool tabs"), (".docx", "Word format"), ("header", "Top margin content")],
        [f"Complete {t}", "Use formatting tools correctly", "Verify save"],
        [
            ("First save naming uses:", ["File → Save As", "View zoom", "only sleep", "Task Manager"], "File → Save As"),
            ("Enter is for:", ["new paragraph", "new page always", "bold", "save"], "new paragraph"),
            ("Page numbers usually go in:", ["header/footer", "filename only", "Ribbon colour", "Recycle Bin"], "header/footer"),
        ],
        f"Describe the formatting/layout features you applied this week.",
        "Screenshot of document in Print Layout with filename visible if possible.",
    )


def _gai(week: int, topic: str) -> dict:
    t, d = _split_topic(topic)
    L = {
        1: (
            "Generative image tools map prompts to pixels. Prompt = subject + setting + style + lighting + composition + constraints (school-safe). "
            "You remain responsible for output and policy.",
            "Iterate: change one variable per trial; keep a prompt log (date, prompt, result note). "
            "Export PNG/JPG; organise folders. No harassment/hate/sexual content; no banned impersonation.",
            "Produce 6 iterations toward one usable poster-style image; log every prompt.",
            "Prompt: subject, environment, style, lighting, camera/composition, school-safe",
        ),
        2: (
            "Composition: focal point, balance, negative space for text, contrast. "
            "Score candidates 1–5 on clarity and text-space.",
            "Lighting vocabulary steers mood (soft, hard, golden hour, studio). "
            "Avoid illegible fake text in images for final designs — add real text in an editor if needed.",
            "Create 3 composition variants; pick hero with written critique.",
            "Scorecard: clarity | relevance | text space | consistency",
        ),
        3: (
            "Brand consistency: 2–3 colours, 3 mood words, do/don’t. "
            "Formats: 1:1 feed, 9:16 story, simple mark.",
            "Export naming Brand_Asset_Size_v01. Mockups optional.",
            "Ship three matching assets + brand rules text.",
            "Rules: colours #… mood: … type vibe: …",
        ),
        4: (
            "Mini campaign: audience, promise, 3 assets, process log, rationale of choices (not only pretty).",
            "Quality and coherence beat random novelty.",
            "Package folder for submission.",
            "Audience | Message | Assets | Rationale",
        ),
    }
    l1, l2, l3, ex = L[week]
    return _pack(
        t, f"AI-assisted graphic design: {d}.",
        _lectures_triple(f"A — {t}", l1, f"B — {t}", l2, f"C — {t}", l3),
        ex,
        [f"Campaign/work for: {t}", "Prompt log required", "School-safe only"],
        [("prompt", "Text brief to model"), ("variant", "Alternative generation"), ("asset", "Final image")],
        [f"Execute {t}", "Document prompts", "Export finals"],
        _mcq_topic(t, d),
        f"Explain your prompt strategy and design decisions for “{t}”.",
        "Screenshot of final asset(s) + prompt log snippet.",
    )


def _video(week: int, topic: str) -> dict:
    t, d = _split_topic(topic)
    L = {
        1: (
            "Project settings vs media. Import footage/audio. Timeline: tracks, playhead, ripple ideas. "
            "Rough cut = order for meaning before polish. Save project + organise bins.",
            "Cut/trim tools; avoid leaving long silences unless intentional. "
            "Backup project file.",
            "Assemble 30–45s rough cut of any school-safe clips (or provided stock).",
            "Bins: video/ | audio/ | exports/",
        ),
        2: (
            "Story spine: hook, middle, payoff. B-roll covers cuts and shows detail. "
            "Audio levels: dialogue above music; avoid clipping.",
            "Captions/titles readable size/safe margins. Duration for reading speed.",
            "Add B-roll, balance audio, captions on speech.",
            "Hook 0–3s | body | end card",
        ),
        3: (
            "Colour/exposure fix before creative grade. AI helpers (captions/noise) need human check. "
            "Export presets for 16:9 and 9:16; bitrate vs size.",
            "Masters vs compressed social. Record settings used.",
            "Polish and export both aspect ratios if possible.",
            "Export MP4 H.264 classroom preset",
        ),
        4: (
            "45–90s promo/tutorial: message clear, captions, credits/music licence school-ok, end slate. "
            "Deliver MP4 + 5-line process note.",
            "Watch full once for continuity and audio only once.",
            "Final export package.",
            "Checklist: story, audio, captions, length, export",
        ),
    }
    l1, l2, l3, ex = L[week]
    return _pack(
        t, f"Video editing: {d}.",
        _lectures_triple(f"A — {t}", l1, f"B — {t}", l2, f"C — {t}", l3),
        ex,
        [f"Timeline work for: {t}", "Organise media", "Export when required"],
        [("timeline", "Time arrangement"), ("rough cut", "Order-first edit"), ("bitrate", "Quality/size trade")],
        [f"Complete {t}", "Respect audio clarity", "Correct export"],
        _mcq_topic(t, d),
        f"Describe edit decisions (cuts, audio, captions) for this week.",
        "Screenshot of timeline + export if any.",
    )


def _cloud(week: int, topic: str) -> dict:
    t, d = _split_topic(topic)
    return _pack(
        t,
        f"Cloud computing concept week: {d}.",
        _lectures_triple(
            f"Core idea — {t}",
            f"{d}. Cloud = on-demand remote compute/storage/network with APIs and billing accounts. "
            "Shared infrastructure across tenants with isolation controls. Contrast with owning a single on-prem server under your desk. "
            "Service models: IaaS (VMs), PaaS (platform/runtime), SaaS (full app). "
            "Deployment models: public/private/hybrid (definitions and school-relevant examples).",
            f"How it works — {t}",
            "Map this week’s topic to a concrete architecture sketch: users → identity → app/service → data store → logs. "
            "Regions and availability zones idea: place resources near users; multi-AZ for resilience. "
            "Identity: accounts, roles, least privilege. Secrets never in public repos. "
            "Cost: free tier limits, always-on VMs cost more than serverless for spiky loads; data egress costs.",
            f"Operations & risk — {t}",
            "Shared responsibility: provider secures cloud; you secure data/config/IAM/app. "
            "Failures: outage planning, backups, RPO/RTO vocabulary. "
            "Monitoring: logs/metrics/alerts at concept level. For the lab, produce a diagram + short ops note (what breaks, who is paged).",
        ),
        f"[User] -HTTPS-> [CDN/LB] -> [App service] -> [Database]\nIAM policies on each\nLogs -> alert on 5xx",
        [
            f"One-page architecture related to: {t}",
            "Label trust boundaries and data stores",
            "Write cost + security notes (bullet each ≥4)",
            "School/business example of the same pattern",
        ],
        [("IaaS/PaaS/SaaS", "Service depth models"), ("region", "Geographic cloud location"), ("IAM", "Identity and access"), ("shared responsibility", "Who secures what")],
        [f"Explain {t} accurately", "Draw a correct simple architecture", "State one risk + mitigation"],
        _mcq_topic(t, d),
        f"Teach back “{t}” with diagram description and a real example.",
        f"Screenshot/photo of your architecture page for week {week}.",
    )


def _system(week: int, topic: str) -> dict:
    t, d = _split_topic(topic)
    return _pack(
        t,
        f"Systems & design thinking: {d}.",
        _lectures_triple(
            f"Frame — {t}",
            f"{d}. A system is parts + relationships + purpose inside a boundary. "
            "Stocks/flows: what accumulates vs what moves. Stakeholders and goals can conflict. "
            "Design thinking modes: empathise, define, ideate, prototype, test — used with discipline, not as empty posters.",
            f"Model — {t}",
            "Tools: user stories “As a… I want… so that…”; problem statements; constraints vs requirements; "
            "flowcharts and context diagrams (system vs environment). "
            "Interfaces: what is passed (data/events) between parts. Failure modes: what if this part is down?",
            f"Decide — {t}",
            "Trade-offs: cost, speed, quality, privacy, simplicity. Write them explicitly. "
            "Feedback loops: how results change next action. "
            "Lab: diagram + 1-page rationale for a school-scale problem linked to this week.",
        ),
        "Context diagram:\n[Students] --> [Registration system] --> [Admin reports]\nAssumptions:\nRisks:",
        [
            f"Artefact for: {t} (diagram + written decisions)",
            "List ≥3 requirements and ≥2 constraints",
            "Name ≥2 failure modes and mitigations",
            "One measured success metric",
        ],
        [("stakeholder", "Who cares about outcomes"), ("constraint", "Hard limit"), ("trade-off", "Competing goals"), ("interface", "Boundary contract")],
        [f"Model {t}", "Make trade-offs explicit", "Define success metric"],
        _mcq_topic(t, d),
        f"Explain your system model for “{t}” and why you chose a trade-off.",
        f"Screenshot of diagram for week {week}.",
    )


def _ai_eng(week: int, topic: str) -> dict:
    """Handcrafted week-by-week. Week 1 fully written; later weeks filled one at a time."""
    t, d = _split_topic(topic)

    # ── Week 1: What is AI? (full substance) ─────────────────
    if week == 1:
        return _pack(
            "What is AI?",
            "Artificial Intelligence (AI) is the field of building computer systems that perform tasks "
            "people usually associate with human intelligence — recognising patterns, making predictions, "
            "understanding language, planning, or controlling devices — by using data, rules, or learned models. "
            "Almost all practical systems today are narrow AI (good at one job), not human-level general minds.",
            [
                (
                    "A clear definition (without science-fiction)",
                    """What AI means in this course

Artificial Intelligence is a branch of computer science and engineering. Its goal is to create machines
and programs that can do useful “intelligent” work: classify images, recommend a playlist, translate a
sentence, detect fraud, complete text, drive a robot arm, or answer a question from a document.

Important: AI is not “a robot with feelings.” It is also not magic. It is software (and sometimes hardware)
that produces an output from an input using either:
  (1) hand-written rules (classical / symbolic approaches), or
  (2) statistical models that were trained on examples (machine learning), or
  (3) a mix of both.

A useful working definition for engineers:
  AI system = inputs → model or decision procedure → outputs, plus a way to judge whether the output is good enough.

What “intelligence” means here
- Perception: sensing the world (pixels, sound, sensor readings).
- Reasoning / prediction: choosing labels, scores, next actions, or text.
- Adaptation (often): improving when given more data (learning).

What AI is NOT (common hype)
- Not automatically conscious or self-aware.
- Not always correct — models make mistakes and can be confident when wrong.
- Not the same as the movie idea of a machine that can do every human job (that idea is called AGI —
  Artificial General Intelligence — and it is not what your phone’s map app is).
- Not identical to “automation.” A thermostat that turns heat on at 18°C is simple automation / control,
  not modern AI — unless it uses learned models of usage or weather.

A short history in four beats (enough to orient you)
- 1950s: Turing and early ideas of machine thinking; the term “Artificial Intelligence” appears (1956 Dartmouth).
- Rules era: expert systems with if–then knowledge hand-coded by experts (strong in narrow domains, brittle).
- Statistical / ML era: systems learn patterns from large datasets (spam filters, ranking, vision).
- Deep learning + generative era: neural networks with many layers handle images, speech, and large language
  models (LLMs) that generate text, code, and images from prompts.

Narrow AI vs general AI
- Narrow (or weak) AI: one task or family of tasks (face unlock, spam filter, chat assistant). This is what
  industry deploys today.
- General (strong) AI / AGI: human-like flexibility across almost any cognitive task — research debate, not
  your capstone scope.

In class phrase to remember:
  “AI is engineered capability under uncertainty, not a person in a computer.”""",
                ),
                (
                    "AI vs classical software vs machine learning",
                    """Three ways to get answers from computers

1) Classical (deterministic) software
   Example: if mark >= 50: print("Pass") else: print("Fail")
   - Behaviour is fully specified by code you typed.
   - Same input → same output (ignoring bugs and clocks).
   - You can usually “prove” what happens by reading the rules.
   - Fails when the world is messy: what is a “cat” in a million photos cannot be listed as hand rules easily.

2) Machine Learning (a major route to AI)
   You do not list every rule. You show many examples (data) and train a model that maps inputs → outputs.
   Example: show 10,000 emails labelled spam/not-spam; the model learns features of spam.
   - Same input usually → same output for a fixed trained model, but the mapping was learned, not hand-written.
   - Errors are statistical: some spam slips through; some good mail is blocked.
   - Needs data, evaluation metrics, and monitoring when the world changes (data drift).

3) Hybrid systems (very common in products)
   Rules + ML together: e.g. a bank uses a model score + hard rules (“block if country is sanctioned”).
   Generative AI + tools: an LLM drafts text, then a policy filter blocks unsafe output.

Where people use the word “AI” in products (everyday map)
| Product idea              | Input              | Intelligent step              | Output            |
|---------------------------|--------------------|--------------------------------|-------------------|
| Photo face unlock         | Camera image       | Face match model               | Unlock / deny     |
| Map ETA                   | GPS, traffic data  | Prediction model / heuristics  | Minutes to arrival|
| Spam filter               | Email text         | Classifier                     | Spam / inbox      |
| Chat assistant            | Prompt + context   | Language model                 | Text answer       |
| Product recommendation    | Past clicks        | Ranking model                  | List of items     |

Classifying a system correctly this week
Ask:
  A) What is the input?
  B) What decision or generation is made?
  C) Were rules hand-written, or was a model trained on data, or both?
  D) How would you know if it is wrong?
If you cannot answer A–D, you do not yet understand that system — even if the brochure says “AI-powered.”

AI Engineer (this course role)
An AI engineer designs, builds, evaluates, and ships systems that use these methods safely:
data → model/tooling → product behaviour → metrics → human oversight.
You will spend later weeks on prompts, data pipelines, APIs, evaluation, and responsibility — all still
grounded in: know what the system actually does.""",
                ),
                (
                    "Capabilities, limits, and how we will talk about AI in this course",
                    """What current AI systems can do well (typical)
- Pattern recognition: images, audio, language patterns in large data.
- Ranking and recommendation when history exists.
- Speeding up drafting (text, code sketches, layouts) with a human editor.
- Narrow prediction when the future looks like the past data.

What they do poorly or riskily
- Facts they were not grounded on (hallucination in generative models: fluent, wrong answers).
- Tasks needing accountability (medical, legal, exam grading) without human review and careful design.
- Situations far outside the training data (odd accents, rare diseases, new slang, local school rules).
- True understanding of meaning the way a careful teacher understands a student — systems optimise objectives,
  they do not “care.”

Anthropomorphism trap
Saying “the AI thinks / wants / lies” is casual talk. Engineers prefer:
  “The model assigned probability…”, “The system sampled a token…”, “The classifier scored 0.92 spam.”
This week: ban empty claims like “AI will replace everything.” Prefer precise ones:
  “A classifier can label SMS as promo with X% accuracy on our test set.”

Safety and responsibility (first contact — deeper weeks later)
Even a class demo can:
- Leak private data if you paste secrets into a public tool.
- Amplify bias if training data was skewed (e.g. always scoring one group worse).
- Be misused for cheating or harassment.
Rule for this academy: school-safe data only; no real phone numbers/passwords in tools; human checks
important decisions; document limits.

What you will produce as evidence this week
Not a neural net from scratch. A clear reasoning artefact:
- Definitions in your own words (accurate, not vague).
- Classification of real systems as rule / ML / hybrid / not-AI automation.
- One system sketched as input → process → output → how you spot errors.""",
                ),
            ],
            """WORKED EXAMPLE — Is this AI?

System A: School fee portal
  if amount_paid >= fee_due: status = "Cleared"
  else: status = "Balance due"
→ Classical rules. Useful automation. Not ML. People may still loosely call it “the system,” but not AI.

System B: Email spam folder
  Model trained on labelled mail; new mail → spam score → folder.
→ Machine learning (narrow AI application). Can be wrong both ways.

System C: “If temperature < 18°C, turn heater on”
→ Control rule / automation, not modern AI.

System D: Chatbot that drafts a reply from a large language model, then a policy filter blocks hate speech
→ Hybrid generative AI + rules.

Template for every system you study:
  Name:
  Input(s):
  Output(s):
  Method: rules / ML / hybrid / unclear
  How it can fail:
  Human needed for:""",
            [
                "In your notebook (or a .txt/.md file), write a definition of AI in ≤80 words that a junior secondary student could understand — must include: tasks people associate with intelligence, and that systems use rules and/or learned models.",
                "Build a table of 6 real systems you use or know (WhatsApp spam?, Google Maps ETA, calculator app, exam grading spreadsheet with =IF, face unlock, chat AI). For each: input, output, rules vs ML vs hybrid vs not-AI, one failure mode.",
                "Pick ONE system from your table. Draw or write the pipeline: Input → Process → Output → Check (how a human notices an error).",
                "Write 5 honest sentences: two things AI systems do well, two limits, one safety rule you will follow in this course when using online AI tools.",
            ],
            [
                ("Artificial Intelligence (AI)", "Engineering field: systems that perform perception, prediction, language, or control-like tasks using rules and/or models from data"),
                ("Narrow AI", "System good at a limited task domain (today’s practical AI)"),
                ("AGI", "Hypothetical AI with broad human-like flexibility — not product reality for this course"),
                ("Machine learning (ML)", "Building models from examples/data rather than writing every rule"),
                ("Model", "The learned or configured procedure that maps inputs to outputs"),
                ("Deterministic software", "Behaviour fully fixed by explicit code/rules; same input → same logic path"),
                ("Automation", "Making a process run without manual steps — may or may not use AI"),
                ("Hallucination (preview)", "When a generative model produces fluent but false content"),
            ],
            [
                "Define AI accurately without sci-fi claims",
                "Tell classical rules, ML, hybrid, and plain automation apart with examples",
                "Describe one system as input → process → output → failure check",
            ],
            [
                (
                    "Which best matches Artificial Intelligence as used in this course?",
                    [
                        "Any app with a colourful logo",
                        "Systems that perform tasks like recognition, prediction, or language using rules and/or learned models",
                        "Only humanoid robots with emotions",
                        "Any Excel formula at all",
                    ],
                    "Systems that perform tasks like recognition, prediction, or language using rules and/or learned models",
                ),
                (
                    "A program that only does: if score >= 50 print Pass else Fail is best described as:",
                    [
                        "A trained neural network",
                        "Classical rule-based software (not ML by itself)",
                        "AGI",
                        "Unsupervised clustering",
                    ],
                    "Classical rule-based software (not ML by itself)",
                ),
                (
                    "Narrow AI means:",
                    [
                        "AI that only works at night",
                        "Systems designed for limited task domains (what we deploy today)",
                        "AI that replaces all jobs this week",
                        "Hardware without software",
                    ],
                    "Systems designed for limited task domains (what we deploy today)",
                ),
            ],
            "In 10–14 sentences: (1) define AI, (2) explain narrow vs general AI, (3) give one rule-based and one ML example, "
            "(4) name one limit of current AI, (5) state one safety habit for using AI tools in school.",
            "Screenshot or photo of your 6-row classification table AND the pipeline sketch for one system "
            "(hand-drawn is fine if readable).",
        )

    # Later weeks: temporary placeholder until we handcraft each (bit by bit)
    return _pack(
        t,
        f"AI Engineer — week {week} topic: {d}. Full lecture notes for this week are being written next; "
        f"Week 1 (What is AI?) is the model for depth.",
        _lectures_triple(
            f"Topic preview — {t}",
            f"This week’s subject is: {d}.\n\n"
            "Until the dedicated notes for this week are published, use primary study from your teacher’s class "
            "and standard references they assign. Do not treat this placeholder as complete theory.",
            f"What you should still practice — {t}",
            f"Write input → process → output for a tiny example of “{t}”. List two failure modes and one metric "
            "you would use to judge quality. Bring questions to class.",
            f"Lab focus — {t}",
            f"Produce a one-page design note for “{detail}” with: goal, example inputs, expected outputs, metric, safety note.",
        ),
        f"DESIGN NOTE — {t}\nGoal:\nExample inputs:\nProcess idea:\nOutputs:\nMetric:\nSafety:\nOpen questions:",
        [
            f"One-page design note for: {t}",
            "Two failure modes listed",
            "One quality metric named",
            "Safety constraint written",
        ],
        [
            (t if len(t) < 40 else "Week topic", d[:100]),
            ("metric", "How you measure quality"),
            ("failure mode", "How the system goes wrong"),
        ],
        [f"Outline {t}", "Name metric and failures", "Write safety constraint"],
        _mcq_topic(t, d),
        f"Summarise what you know so far about “{t}” and what you still need explained in class.",
        f"Screenshot of your design note for week {week}.",
    )


def _android(week: int, topic: str) -> dict:
    t, d = _split_topic(topic)
    return _pack(
        t,
        f"Android development topic: {d}.",
        _lectures_triple(
            f"Platform — {t}",
            f"{d}. Android apps have activities/screens (or modern Compose destinations), layouts (XML or Compose), "
            "resources (strings, colours, drawables), and a manifest declaring components. "
            "Build tools compile and package an APK/AAB. Emulator vs physical device.",
            f"UI & behaviour — {t}",
            "Views/widgets: Text, Button, Image, EditText, RecyclerView concepts. "
            "Layouts: Linear, Constraint — positioning and @string resources. "
            "Events: click listeners; navigation between screens via intents or nav graph. "
            "State: what is shown after rotation/config change (awareness).",
            f"Quality — {t}",
            "Validate input; handle empty states; readable touch targets; permissions only when needed. "
            "Logcat for crashes. Accessibility content descriptions. "
            "Lab: implement a small vertical slice for this week that runs and can be demoed in 30 seconds.",
        ),
        f"// pseudo\nButton.setOnClickListener → read input → validate → update TextView / open Activity",
        [
            f"Working UI/behaviour for: {t}",
            "Use string resources (no hard-coded user-facing mess if taught)",
            "Handle bad input without crash",
            "Screenshot emulator/device + short run note",
        ],
        [("Activity", "Screen controller"), ("Intent", "Message to start components"), ("Layout", "View hierarchy"), ("Logcat", "Device logs")],
        [f"Implement {t}", "Run without crash on happy path", "Explain navigation/state"],
        _mcq_topic(t, d),
        f"Describe UI components and logic you built for “{t}”.",
        f"Screenshot of running app week {week}.",
    )


def _generic_tech(slug: str, week: int, total: int, title: str, detail: str) -> dict:
    return _pack(
        title,
        f"{detail} (week {week}/{total}).",
        _lectures_triple(
            f"Concepts — {title}",
            f"Definition and scope: {detail}. "
            "List the moving parts, inputs, outputs, and quality criteria professionals use for this skill. "
            "Relate at least one precise term of art to a concrete example you can demo in under one minute.",
            f"Method — {title}",
            f"Step-by-step method to perform “{title}” correctly the first time: prerequisites, main operations, verification. "
            "Common error messages or failure symptoms and what they mean. "
            "Tools/settings you must not leave at random defaults.",
            f"Application — {title}",
            f"Guided build: produce an artefact that proves “{detail}”. "
            "Variation: change one requirement and re-verify. "
            "Define done: what a teacher should see in five seconds of inspection.",
        ),
        f"WORKED PATH — {title}\n1) Prepare\n2) Execute core technique for: {detail}\n3) Verify with a checklist of 4 items\n4) Save/export evidence",
        [
            f"Primary artefact for: {title}",
            "Verification checklist written and ticked",
            "One intentional variation completed",
            f"Save as YourName_Week{week:02d}_{slug[:12]}",
        ],
        [(title[:32], detail[:80]), ("artefact", "Thing you produce"), ("verify", "Check against criteria")],
        [f"Define {title}", f"Perform {detail}", "Verify and save evidence"],
        _mcq_topic(title, detail),
        f"Teach “{title}” in 8–10 sentences with concrete steps (no generic study advice).",
        f"Screenshot of finished artefact week {week}.",
    )


def week_content(slug: str, week: int, course_title: str, topic: str) -> dict:
    """Return real 3-lecture pack for this course week."""
    total = weeks_for(slug)
    topics = TOPICS.get(slug) or []
    if 1 <= week <= len(topics):
        topic = topics[week - 1]
    t, d = _split_topic(topic)

    if slug == "python-for-beginners":
        return _py_beginners(week, topic)
    if slug == "python-data-apps":
        return _py_data(week, topic)
    if slug == "python-developer":
        return _py_dev(week, topic)
    if slug == "website-development":
        return _website(week, topic)
    if slug == "graphic-coreldraw":
        return _corel(week, topic)
    if slug == "scratch":
        return _scratch_pack(week, topic, "scratch")
    if slug == "python-blocks":
        return _scratch_pack(week, topic, "blocks")
    if slug == "office-excel":
        return _excel(week, topic)
    if slug == "office-powerpoint":
        return _ppt(week, topic)
    if slug == "office-ms-word":
        return _word(week, topic)
    if slug == "graphic-ai":
        return _gai(week, topic)
    if slug == "video-editing-ai":
        return _video(week, topic)
    if slug == "cloud-computing":
        return _cloud(week, topic)
    if slug == "system-design-thinking":
        return _system(week, topic)
    if slug == "ai-engineer":
        return _ai_eng(week, topic)
    if slug == "android-app-development":
        return _android(week, topic)
    return _generic_tech(slug, week, total, t, d)
