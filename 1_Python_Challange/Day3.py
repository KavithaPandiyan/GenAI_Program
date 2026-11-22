"""
DAY 3 - Conditional Statements
if, if-else, if-elif-else, nested if, ternary, match-case
Author : Kavitha Pandiyan
Course : SocialEagleAI - 10 Days Python Challenge
Run    : python Day3.py   (or click the Run button in VS Code)
"""

# =============================================================
# PART 1: SIMPLE if
# Runs the block ONLY when the condition is True.
# Indentation (4 spaces) marks what is inside the if.
# =============================================================
print("=== Part 1: Simple if ===")

temperature = 36
if temperature > 30:
    print("It's hot in Chennai today!")
    print("Drink plenty of water.")      # also inside the if
print("This line always runs.")          # outside the if
print()


# =============================================================
# PART 2: if - else  (two paths)
# =============================================================
print("=== Part 2: if-else ===")

age = 17
if age >= 18:
    print(f"Age {age}: Eligible to vote")
else:
    print(f"Age {age}: Not eligible to vote yet")

number = 7
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
print()


# =============================================================
# PART 3: if - elif - else  (many paths)
# Python checks from top to bottom and stops at the FIRST True.
# =============================================================
print("=== Part 3: if-elif-else ===")

marks = 82
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"
print(f"Marks {marks} -> Grade {grade}")

# Order matters! Wrong order example:
# if marks >= 50: "C"  <- 82 would stop here and never reach "A"

hour = 14
if hour < 12:
    greeting = "Good Morning"
elif hour < 17:
    greeting = "Good Afternoon"
elif hour < 21:
    greeting = "Good Evening"
else:
    greeting = "Good Night"
print(f"Hour {hour}: {greeting}, Kavitha!")
print()


# =============================================================
# PART 4: MULTIPLE CONDITIONS - and, or, not
# =============================================================
print("=== Part 4: Combining Conditions ===")

experience = 8
knows_python = True
knows_genai = False

if experience >= 5 and knows_python:
    print("Eligible for Senior Data Engineer role")

if knows_python or knows_genai:
    print("Eligible for AI training program")

if not knows_genai:
    print("Next goal: learn GenAI")

# Chained comparison (Python special)
score = 75
if 60 <= score <= 80:                    # same as score >= 60 and score <= 80
    print(f"Score {score} is in the 60-80 range")
print()


# =============================================================
# PART 5: NESTED if  (an if inside another if)
# =============================================================
print("=== Part 5: Nested if ===")

has_account = True
balance = 5000
withdraw = 3000
pin_correct = True

if has_account:
    print("Account found.")
    if pin_correct:
        print("PIN verified.")
        if withdraw <= balance:
            balance -= withdraw
            print(f"Withdrawn Rs {withdraw}. Remaining balance: Rs {balance}")
        else:
            print("Insufficient balance!")
    else:
        print("Wrong PIN!")
else:
    print("No account found.")

# Tip: deep nesting is hard to read. The same logic flattened:
print("-- Same logic, flattened --")
balance = 5000
if not has_account:
    print("No account found.")
elif not pin_correct:
    print("Wrong PIN!")
elif withdraw > balance:
    print("Insufficient balance!")
else:
    balance -= withdraw
    print(f"Withdrawn Rs {withdraw}. Remaining balance: Rs {balance}")
print()


# =============================================================
# PART 6: TERNARY (one-line if-else)
# Syntax:  value_if_true  if  condition  else  value_if_false
# =============================================================
print("=== Part 6: Ternary Operator ===")

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age}: {status}")

n = 15
print(f"{n} is", "Even" if n % 2 == 0 else "Odd")

a, b = 42, 27
bigger = a if a > b else b
print(f"Bigger of {a} and {b}: {bigger}")

result = "PASS" if marks >= 50 else "FAIL"
print(f"Marks {marks}: {result}")

# Chained ternary (works, but use only for very simple cases)
num = 0
sign = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(f"{num} is {sign}")

# Ternary inside an f-string and a list comprehension
items_in_cart = 1
print(f"You have {items_in_cart} item{'s' if items_in_cart != 1 else ''} in cart")
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]
print("1-5 labels :", labels)
print()


# =============================================================
# PART 7: TRUTHY / FALSY in conditions
# Empty values ("", [], {}, 0, None) count as False.
# =============================================================
print("=== Part 7: Truthy & Falsy Checks ===")

username = ""
if not username:
    print("Username is empty - please enter a name")

skills = ["Python", "SQL"]
if skills:
    print(f"You have {len(skills)} skills listed")

api_key = None
if api_key is None:
    print("API key not set - check your .env file")
print()


# =============================================================
# PART 8: MEMBERSHIP CHECKS with in
# =============================================================
print("=== Part 8: Conditions with 'in' ===")

city = "Madurai"
tamil_nadu_cities = ["Chennai", "Coimbatore", "Madurai", "Trichy", "Salem"]
if city in tamil_nadu_cities:
    print(f"{city} is in Tamil Nadu")

email = "kavitha@gmail.com"
if "@" in email and email.endswith(".com"):
    print(f"{email} looks valid")

day = "Sunday"
if day in ("Saturday", "Sunday"):
    print(f"{day}: Weekend - time to practice Python!")
print()


# =============================================================
# PART 9: match-case (Python 3.10+) - cleaner than many elifs
# =============================================================
print("=== Part 9: match-case ===")

command = "start"
match command:
    case "start":
        print("Starting the pipeline...")
    case "stop":
        print("Stopping the pipeline...")
    case "status" | "info":                 # | means OR
        print("Pipeline is running")
    case _:                                 # _ = default (like else)
        print("Unknown command")

http_code = 404
match http_code:
    case 200:
        message = "OK"
    case 401 | 403:
        message = "Access denied"
    case 404:
        message = "Not Found"
    case 500:
        message = "Server error"
    case _:
        message = "Other status"
print(f"HTTP {http_code}: {message}")
print()


# =============================================================
# PART 10: COMMON MISTAKES
# =============================================================
print("=== Part 10: Common Mistakes ===")
# 1. Using = instead of ==
#    if x = 5:      -> SyntaxError   |  correct: if x == 5:
# 2. Forgetting the colon
#    if x > 5       -> SyntaxError   |  correct: if x > 5:
# 3. Wrong indentation
#    if x > 5:
#    print("hi")    -> IndentationError (must be indented)
# 4. Comparing with None using ==
#    if value == None:   -> works, but use: if value is None:
# 5. Writing  if x == 1 or 2:  -> ALWAYS True!
x = 5
print("x == 1 or 2      ->", bool(x == 1 or 2), "(wrong! 2 is always truthy)")
print("x == 1 or x == 2 ->", x == 1 or x == 2, "(correct)")
print("x in (1, 2)      ->", x in (1, 2), "(best)")
print()


# =============================================================
# PART 11: MINI PROJECT 1 - Income Tax Calculator (New Regime)
# Slabs (simplified, for practice only - not tax advice):
#   0 - 4L: 0% | 4-8L: 5% | 8-12L: 10% | 12-16L: 15%
#   16-20L: 20% | 20-24L: 25% | above 24L: 30%
# =============================================================
print("=== Part 11: Mini Project - Tax Slab Finder ===")

def tax_slab(income):
    if income <= 400000:
        return "0%"
    elif income <= 800000:
        return "5%"
    elif income <= 1200000:
        return "10%"
    elif income <= 1600000:
        return "15%"
    elif income <= 2000000:
        return "20%"
    elif income <= 2400000:
        return "25%"
    else:
        return "30%"

for income in [350000, 750000, 1500000, 2600000]:
    print(f"Income Rs {income:>10,} -> highest slab {tax_slab(income)}")
print()


# =============================================================
# PART 12: MINI PROJECT 2 - Movie Ticket Price
# Uses: if-elif-else, nested if, ternary, and/or
# =============================================================
print("=== Part 12: Mini Project - Movie Ticket Price ===")

customers = [
    ("Kavitha", 34, "Sunday", True),
    ("Arun", 10, "Monday", False),
    ("Lakshmi", 65, "Wednesday", False),
    ("Rahul", 22, "Saturday", True),
]

for name, age, day, is_member in customers:
    # Base price by age
    if age < 12:
        price = 100
        category = "Child"
    elif age >= 60:
        price = 120
        category = "Senior"
    else:
        price = 200
        category = "Adult"

    # Weekend surcharge (nested decision)
    if day in ("Saturday", "Sunday"):
        if category == "Adult":
            price += 50
        else:
            price += 20

    # Member discount using ternary
    discount = 0.10 if is_member else 0
    final = price - price * discount

    member_tag = "Member" if is_member else "Guest"
    print(f"{name:<8} | {category:<6} | {day:<9} | {member_tag:<6} | Rs {final:.2f}")
print()


# =============================================================
# PART 13: TRY IT YOURSELF - user input (uncomment to run)
# =============================================================
# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")
# print("Even" if num % 2 == 0 else "Odd")
#
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f"{year} is a Leap Year")
# else:
#     print(f"{year} is not a Leap Year")

print("Day 3 complete!")