"""
DAY 4 - Loops
for loop, range, while loop, break/continue/pass,
looping through dictionaries, two lists -> dictionary (zip)
Author : Kavitha Pandiyan
Course : SocialEagleAI - 10 Days Python Challenge
Run    : python Day4.py   (or click the Run button in VS Code)
"""

# =============================================================
# PART 1: WHY LOOPS? - repeat work without repeating code
# =============================================================
print("=== Part 1: Why Loops ===")

# Without a loop
print("Hello 1"); print("Hello 2"); print("Hello 3")

# With a loop - same result, works for 3 or 3000
for i in range(1, 4):
    print("Hello", i)
print()


# =============================================================
# PART 2: for LOOP with range()
#   range(stop)              -> 0 .. stop-1
#   range(start, stop)       -> start .. stop-1
#   range(start, stop, step) -> jump by step
# =============================================================
print("=== Part 2: for + range() ===")

print("range(5)        :", end=" ")
for i in range(5):
    print(i, end=" ")
print()

print("range(1, 6)     :", end=" ")
for i in range(1, 6):
    print(i, end=" ")
print()

print("range(0, 20, 5) :", end=" ")
for i in range(0, 20, 5):
    print(i, end=" ")
print()

print("range(5, 0, -1) :", end=" ")      # countdown
for i in range(5, 0, -1):
    print(i, end=" ")
print("Go!")

# Multiplication table
n = 7
print(f"\nTable of {n}:")
for i in range(1, 11):
    print(f"{n} x {i:>2} = {n * i:>3}")

# Sum of 1 to 100
total = 0
for i in range(1, 101):
    total += i
print("\nSum of 1 to 100 =", total)
print()


# =============================================================
# PART 3: for LOOP over STRING, LIST, TUPLE, SET
# =============================================================
print("=== Part 3: Looping Over Collections ===")

# String - one character at a time
word = "Python"
for ch in word:
    print(ch, end=" ")
print()

# List
tools = ["ADF", "Databricks", "Synapse", "Power BI"]
for tool in tools:
    print("Tool:", tool)

# Tuple
days = ("Mon", "Tue", "Wed")
for day in days:
    print("Day:", day)

# Set (order is not guaranteed)
skills = {"Python", "SQL", "GenAI"}
for skill in sorted(skills):            # sorted() gives a fixed order
    print("Skill:", skill)
print()


# =============================================================
# PART 4: enumerate() - get index AND value together
# =============================================================
print("=== Part 4: enumerate() ===")

for index, tool in enumerate(tools):
    print(index, tool)

print("-- start counting from 1 --")
for num, tool in enumerate(tools, start=1):
    print(f"{num}. {tool}")
print()


# =============================================================
# PART 5: LOOPING THROUGH A DICTIONARY
# =============================================================
print("=== Part 5: Dictionary in for loop ===")

student = {
    "name": "Kavitha",
    "role": "Azure Data Engineer",
    "experience": 8,
    "city": "Chennai",
}

# 5a. Keys only (default)
print("-- keys --")
for key in student:
    print(key)

# 5b. Values only
print("-- values --")
for value in student.values():
    print(value)

# 5c. Keys AND values (most common)
print("-- items() --")
for key, value in student.items():
    print(f"{key:<11}: {value}")

# 5d. Loop with a condition - only numbers
print("-- only numeric values --")
for key, value in student.items():
    if isinstance(value, int):
        print(f"{key} = {value}")

# 5e. Update values inside a loop
prices = {"apple": 100, "banana": 40, "mango": 150}
for fruit in prices:
    prices[fruit] = prices[fruit] * 1.10     # add 10%
print("-- prices after 10% hike --")
for fruit, price in prices.items():
    print(f"{fruit:<7}: Rs {price:.2f}")

# 5f. Nested dictionary
employees = {
    "E101": {"name": "Kavitha", "dept": "Data", "salary": 125000},
    "E102": {"name": "Arun", "dept": "AI", "salary": 110000},
    "E103": {"name": "Priya", "dept": "Data", "salary": 95000},
}
print("-- nested dictionary --")
for emp_id, details in employees.items():
    print(f"{emp_id}: {details['name']:<8} | {details['dept']:<4} | Rs {details['salary']:,}")

# 5g. List of dictionaries (very common with APIs / JSON)
orders = [
    {"id": 1, "item": "Laptop", "qty": 1, "price": 55000},
    {"id": 2, "item": "Mouse", "qty": 2, "price": 500},
    {"id": 3, "item": "Keyboard", "qty": 1, "price": 1500},
]
print("-- list of dictionaries --")
grand_total = 0
for order in orders:
    line_total = order["qty"] * order["price"]
    grand_total += line_total
    print(f"#{order['id']} {order['item']:<9} x{order['qty']}  = Rs {line_total:,}")
print(f"Grand total = Rs {grand_total:,}")
print()


# =============================================================
# PART 6: TWO LISTS -> ONE DICTIONARY
# =============================================================
print("=== Part 6: Two Lists as a Dictionary ===")

names = ["Kavitha", "Arun", "Priya", "Rahul"]
marks = [92, 75, 58, 88]

# 6a. Using zip() - pairs items side by side
print("-- zip() pairs --")
for name, mark in zip(names, marks):
    print(name, "->", mark)

# 6b. Method 1: dict(zip())  - shortest
result1 = dict(zip(names, marks))
print("dict(zip())        :", result1)

# 6c. Method 2: for loop with zip  - easy to understand
result2 = {}
for name, mark in zip(names, marks):
    result2[name] = mark
print("for loop + zip     :", result2)

# 6d. Method 3: for loop with index (range + len)
result3 = {}
for i in range(len(names)):
    result3[names[i]] = marks[i]
print("for loop + index   :", result3)

# 6e. Method 4: dictionary comprehension
result4 = {name: mark for name, mark in zip(names, marks)}
print("dict comprehension :", result4)

# 6f. With a condition - only those who passed
passed = {name: mark for name, mark in zip(names, marks) if mark >= 60}
print("only passed (>=60) :", passed)

# 6g. Unequal lists - zip stops at the shortest
keys = ["a", "b", "c", "d"]
values = [1, 2]
print("unequal lengths    :", dict(zip(keys, values)))

# 6h. Three lists -> dictionary of dictionaries
cities = ["Chennai", "Coimbatore", "Madurai", "Salem"]
profile = {}
for name, mark, city in zip(names, marks, cities):
    profile[name] = {"marks": mark, "city": city}
print("three lists        :")
for name, info in profile.items():
    print(f"   {name:<8} {info}")

# 6i. Reverse: dictionary -> two lists
back_names = list(result1.keys())
back_marks = list(result1.values())
print("back to lists      :", back_names, back_marks)
print()


# =============================================================
# PART 7: while LOOP - repeat WHILE a condition is True
# =============================================================
print("=== Part 7: while loop ===")

count = 1
while count <= 5:
    print("Count:", count)
    count += 1            # IMPORTANT: update, or the loop never ends!

# Savings goal
savings = 0
month = 0
while savings < 100000:
    savings += 15000
    month += 1
print(f"Saving Rs 15,000/month -> Rs 1,00,000 reached in {month} months (Rs {savings:,})")

# Digits of a number
num = 2026
digit_sum = 0
while num > 0:
    digit_sum += num % 10     # last digit
    num //= 10                # remove last digit
print("Sum of digits of 2026 =", digit_sum)
print()


# =============================================================
# PART 8: break, continue, pass, and loop-else
# =============================================================
print("=== Part 8: break / continue / pass / else ===")

# break - stop the loop completely
print("-- break: stop at first number > 50 --")
for n in [12, 45, 67, 23, 89]:
    if n > 50:
        print("Found:", n)
        break
    print("Checked:", n)

# continue - skip this round, go to the next
print("-- continue: skip odd numbers --")
for n in range(1, 11):
    if n % 2 != 0:
        continue
    print(n, end=" ")
print()

# pass - placeholder, does nothing (code to be written later)
print("-- pass: placeholder --")
for n in range(3):
    if n == 1:
        pass              # TODO: handle this later
    print("n =", n)

# for-else - else runs ONLY if the loop did NOT break
print("-- for-else: search --")
search = "Spark"
for tool in tools:
    if tool == search:
        print(f"{search} found!")
        break
else:
    print(f"{search} not found in {tools}")
print()


# =============================================================
# PART 9: NESTED LOOPS (loop inside a loop)
# =============================================================
print("=== Part 9: Nested Loops ===")

# Star pattern
rows = 5
for i in range(1, rows + 1):
    print("* " * i)

# Number pyramid
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Combinations
sizes = ["S", "M"]
colors = ["Red", "Blue"]
for size in sizes:
    for color in colors:
        print(f"T-shirt: {size}-{color}")
print()


# =============================================================
# PART 10: LIST COMPREHENSION - a loop in one line
# =============================================================
print("=== Part 10: Comprehensions ===")

squares = [x ** 2 for x in range(1, 6)]
upper_tools = [t.upper() for t in tools]
long_tools = [t for t in tools if len(t) > 5]
print("squares     :", squares)
print("upper_tools :", upper_tools)
print("long_tools  :", long_tools)
print()


# =============================================================
# PART 11: MINI PROJECT - Student Report Card
# Uses: two lists -> dict, for loop over dict, if-elif, break
# =============================================================
print("=== Part 11: Mini Project - Report Card ===")

students = ["Kavitha", "Arun", "Priya", "Rahul", "Divya"]
scores = [92, 75, 45, 88, 67]

report = dict(zip(students, scores))

print(f"{'Name':<9}{'Score':>6}  Grade")
print("-" * 22)
grade_count = {"A": 0, "B": 0, "C": 0, "F": 0}
for name, score in report.items():
    if score >= 85:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    grade_count[grade] += 1
    print(f"{name:<9}{score:>6}  {grade}")
print("-" * 22)

average = sum(report.values()) / len(report)
topper = max(report, key=report.get)
print(f"Class average : {average:.2f}")
print(f"Topper        : {topper} ({report[topper]})")
print("Grade summary :", end=" ")
for grade, count in grade_count.items():
    print(f"{grade}={count}", end="  ")
print()

# First student below average
for name, score in report.items():
    if score < average:
        print(f"First below average: {name} ({score})")
        break
print()


# =============================================================
# PART 12: TRY IT YOURSELF (uncomment to run)
# =============================================================
# 1. Simple menu with while loop
# while True:
#     choice = input("Type 'add', 'show' or 'quit': ").lower()
#     if choice == "quit":
#         print("Bye!")
#         break
#     elif choice == "add":
#         print("Adding item...")
#     elif choice == "show":
#         print("Showing items...")
#     else:
#         print("Invalid choice, try again")
#
# 2. Build a dictionary from user input
# phonebook = {}
# for i in range(3):
#     name = input("Name: ")
#     phone = input("Phone: ")
#     phonebook[name] = phone
# for name, phone in phonebook.items():
#     print(name, "->", phone)

print("Day 4 complete!")