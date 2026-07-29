"""
10 BASIC LOOP PATTERNS IN PYTHON
=================================
Run this file top to bottom, or copy one function at a time into a
Python shell and play with the numbers. The goal isn't to memorize
these — it's to notice the SHAPE of the logic each pattern uses,
because that shape shows up again and again in real code.

Tip: try changing the input numbers and predicting the output
BEFORE you run it. That's how you actually learn loops.
"""


# ─────────────────────────────────────────────────────────────
# PATTERN 1: Basic counting loop (for + range)
# ─────────────────────────────────────────────────────────────
def pattern_1_basic_count():
    # range(start, stop) generates numbers from start up to (not including) stop.
    # This is the most common loop shape: "do something N times."
    for i in range(1, 6):
        print(i)
    # Output: 1 2 3 4 5

for i in range(0,5,1):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(1, 5, 1):
    for j in range(1, 5, 1):
        if j <= 5 - i:
            print(" ", end = "")
        else:
            print("*", end = "")


# ─────────────────────────────────────────────────────────────
# PATTERN 2: Loop with a step (skip counting)
# ─────────────────────────────────────────────────────────────
def pattern_2_step_counting():
    # range(start, stop, step) lets you skip values.
    # Great for things like "every other item" or "every 5th minute."
    for i in range(0, 20, 5):
        print(i)
    # Output: 0 5 10 15

    # Negative step counts DOWN instead of up.
    print("Counting down:")
    for i in range(10, 0, -2):
        print(i)
    # Output: 10 8 6 4 2


# ─────────────────────────────────────────────────────────────
# PATTERN 3: Looping over a list directly (no index needed)
# ─────────────────────────────────────────────────────────────
def pattern_3_loop_over_list():
    fruits = ["apple", "banana", "cherry"]

    # When you don't need the position/index, loop over the items directly.
    # This is more "Pythonic" than using range(len(fruits)).
    for fruit in fruits:
        print(f"I like {fruit}")


# ─────────────────────────────────────────────────────────────
# PATTERN 4: Looping with BOTH index and value (enumerate)
# ─────────────────────────────────────────────────────────────
def pattern_4_enumerate():
    fruits = ["apple", "banana", "cherry"]

    # enumerate() gives you (index, value) pairs automatically.
    # Use this instead of manually tracking a counter variable.
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")
    # Output:
    # 0: apple
    # 1: banana
    # 2: cherry

    # You can also tell enumerate to start counting from a different number.
    for index, fruit in enumerate(fruits, start=1):
        print(f"Item #{index} is {fruit}")


# ─────────────────────────────────────────────────────────────
# PATTERN 5: Accumulator pattern (build up a result as you go)
# ─────────────────────────────────────────────────────────────
def pattern_5_accumulator():
    numbers = [4, 8, 15, 16, 23, 42]

    # An "accumulator" is a variable that collects a result across iterations.
    # Almost every "sum", "count", or "combine" problem uses this shape:
    # 1. Start with an initial value
    # 2. Loop through the data
    # 3. Update the accumulator each time
    total = 0
    for num in numbers:
        total = total + num  # same as: total += num
    print(f"Sum: {total}")

    # The accumulator doesn't have to be a number — it can be a list, string, etc.
    doubled = []
    for num in numbers:
        doubled.append(num * 2)
    print(f"Doubled: {doubled}")


# ─────────────────────────────────────────────────────────────
# PATTERN 6: while loop (loop until a condition becomes False)
# ─────────────────────────────────────────────────────────────
def pattern_6_while_loop():
    # Use "while" when you don't know in advance how many times you'll loop —
    # you just know the CONDITION that should keep it going.
    count = 0
    while count < 5:
        print(f"count is {count}")
        count += 1  # IMPORTANT: forgetting this line = infinite loop!

    # Real-world use case: keep asking until valid input is given,
    # keep retrying until a connection succeeds, etc.


# ─────────────────────────────────────────────────────────────
# PATTERN 7: break and continue (controlling loop flow)
# ─────────────────────────────────────────────────────────────
def pattern_7_break_and_continue():
    # 'break' immediately exits the loop entirely.
    print("Using break — stop at first number > 5:")
    for num in [2, 4, 6, 8, 10]:
        if num > 5:
            break  # loop ends here, 8 and 10 are never checked
        print(num)
    # Output: 2 4

    # 'continue' skips the rest of THIS iteration and moves to the next one.
    print("Using continue — skip even numbers:")
    for num in [1, 2, 3, 4, 5, 6]:
        if num % 2 == 0:
            continue  # jump straight to the next number
        print(num)
    # Output: 1 3 5


# ─────────────────────────────────────────────────────────────
# PATTERN 8: Nested loops (a loop inside another loop)
# ─────────────────────────────────────────────────────────────
def pattern_8_nested_loops():
    # The inner loop runs COMPLETELY (all its iterations) for every
    # single iteration of the outer loop. Think: "rows and columns."
    for row in range(1, 4):        # outer loop = 3 rows
        for col in range(1, 4):    # inner loop = 3 columns per row
            print(f"({row},{col})", end=" ")
        print()  # move to a new line after each row finishes
    # Output:
    # (1,1) (1,2) (1,3)
    # (2,1) (2,2) (2,3)
    # (3,1) (3,2) (3,3)

    # Classic use case: multiplication table
    print("\nMultiplication table (1-3):")
    for i in range(1, 4):
        for j in range(1, 4):
            print(i * j, end="\t")
        print()


# ─────────────────────────────────────────────────────────────
# PATTERN 9: Looping over a dictionary (keys, values, both)
# ─────────────────────────────────────────────────────────────
def pattern_9_loop_over_dict():
    student_grades = {"Alice": 90, "Bob": 85, "Charlie": 78}

    # Looping directly gives you the KEYS by default.
    print("Just keys:")
    for name in student_grades:
        print(name)

    # .values() gives you just the values.
    print("Just values:")
    for grade in student_grades.values():
        print(grade)

    # .items() gives you (key, value) pairs — the most common way
    # to loop over a dictionary when you need both pieces of info.
    print("Keys and values together:")
    for name, grade in student_grades.items():
        print(f"{name} scored {grade}")


# ─────────────────────────────────────────────────────────────
# PATTERN 10: List comprehension (a compact loop that builds a list)
# ─────────────────────────────────────────────────────────────
def pattern_10_list_comprehension():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # This list comprehension:
    #   squares = [n * n for n in numbers]
    # is a shorthand for this normal loop:
    squares = []
    for n in numbers:
        squares.append(n * n)
    print(f"Squares (regular loop): {squares}")

    # Same result, written as a comprehension — read it as:
    # "n*n, for each n in numbers"
    squares_short = [n * n for n in numbers]
    print(f"Squares (comprehension): {squares_short}")

    # Comprehensions can also filter, using an 'if' at the end.
    # Read it as: "n, for each n in numbers, but only if n is even"
    evens_only = [n for n in numbers if n % 2 == 0]
    print(f"Evens only: {evens_only}")


# ─────────────────────────────────────────────────────────────
# Run every pattern in order so you can see them all in action.
# Comment out the ones you've already learned to focus on new ones.
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    patterns = [
        pattern_1_basic_count,
        pattern_2_step_counting,
        pattern_3_loop_over_list,
        pattern_4_enumerate,
        pattern_5_accumulator,
        pattern_6_while_loop,
        pattern_7_break_and_continue,
        pattern_8_nested_loops,
        pattern_9_loop_over_dict,
        pattern_10_list_comprehension,
    ]

    for i, pattern_func in enumerate(patterns, start=1):
        print(f"\n{'=' * 50}")
        print(f"PATTERN {i}: {pattern_func.__name__}")
        print("=" * 50)
        pattern_func()
