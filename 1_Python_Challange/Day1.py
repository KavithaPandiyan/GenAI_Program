"""
DAY 1 - Python Basics: Fundamentals, Variables & Operators
Author : Kavitha Pandiyan
Course : SocialEagleAI - 10 Days Python Challenge
Run    : python Day1.py   (or click the Run button in VS Code)
"""

# =============================================================
# PART 1: FUNDAMENTALS - print, comments, escape characters
# =============================================================
print("=== Part 1: Fundamentals ===")

# This is a single-line comment. Python ignores it.
print("Hello, World!")
print("Name:", "Kavitha", "| Role:", "Azure Data Engineer")
print("Line 1\nLine 2")             # \n = new line
print("Col1\tCol2\tCol3")           # \t = tab
print("A", "B", "C", sep="-")       # sep = separator between values
print("No new line here...", end=" ")
print("continued on same line")     # end = what to print at the end
print()


# =============================================================
# PART 2: VARIABLES & DATA TYPES
# =============================================================
print("=== Part 2: Variables & Data Types ===")

name = "Kavitha"          # str   - text
experience = 8            # int   - whole number
salary = 1500000.50       # float - decimal number
is_learning_ai = True     # bool  - True / False
skills = None             # NoneType - "no value yet"

print(name, "->", type(name))
print(experience, "->", type(experience))
print(salary, "->", type(salary))
print(is_learning_ai, "->", type(is_learning_ai))
print(skills, "->", type(skills))

# Multiple assignment in one line
city, state, country = "Chennai", "Tamil Nadu", "India"
print("Location:", city, state, country)

# Same value to many variables
a = b = c = 0
print("a, b, c =", a, b, c)

# Swap two variables (Python style - no temp variable needed)
x, y = 10, 20
x, y = y, x
print("After swap -> x:", x, "y:", y)

# Variable naming rules:
#   OK   : my_name, name1, _total, firstName
#   ERROR: 1name, my-name, class (reserved keyword)
print()


# =============================================================
# PART 3: STRINGS & F-STRINGS
# =============================================================
print("=== Part 3: Strings & f-strings ===")

course = "SocialEagleAI"
name = "Kavitha"          # str   - text
experience = 8            # int   - whole number
salary = 1500000.50       # float - decimal number
is_learning_ai = True     # bool  - True / False
skills = None             # NoneType - "no value yet"
print(f"I am {name}, learning AI at {course}.")      # f-string
print(f"Experience: {experience} years")
print(f"Salary formatted: {salary:,.2f}")             # 1,500,000.50
print("Length of course name:", len(course))
print("Upper:", course.upper())
print("Lower:", course.lower())
print("First letter:", course[0], "| Last letter:", course[-1])
print("Slice [0:6]:", course[0:6])                    # Social
print("Repeat:", "Hi! " * 3)
print()


# =============================================================
# PART 4: TYPE CONVERSION (CASTING)
# =============================================================
print("=== Part 4: Type Conversion ===")

num_text = "25"
num = int(num_text)              # str -> int
print(num + 5, type(num))

price = float("99.99")           # str -> float
print(price, type(price))

age_text = str(30)               # int -> str
print("Age: " + age_text)        # can join strings with +

print(int(7.9))                  # float -> int (cuts decimal, gives 7)
print(bool(0), bool(1), bool(""), bool("hi"))   # False True False True
print()


# =============================================================
# PART 5: ARITHMETIC OPERATORS
# =============================================================
print("=== Part 5: Arithmetic Operators ===")

p, q = 17, 5
print(f"{p} + {q}  = {p + q}")     # Addition       -> 22
print(f"{p} - {q}  = {p - q}")     # Subtraction    -> 12
print(f"{p} * {q}  = {p * q}")     # Multiplication -> 85
print(f"{p} / {q}  = {p / q}")     # Division       -> 3.4 (always float)
print(f"{p} // {q} = {p // q}")    # Floor division -> 3
print(f"{p} % {q}  = {p % q}")     # Modulus (remainder) -> 2
print(f"{p} ** 2 = {p ** 2}")      # Power          -> 289
print()


# =============================================================
# PART 6: ASSIGNMENT OPERATORS
# =============================================================
print("=== Part 6: Assignment Operators ===")

score = 10
score += 5;  print("score += 5  ->", score)   # 15
score -= 3;  print("score -= 3  ->", score)   # 12
score *= 2;  print("score *= 2  ->", score)   # 24
score /= 4;  print("score /= 4  ->", score)   # 6.0
score //= 4; print("score //= 4 ->", score)   # 1.0
score **= 3; print("score **= 3 ->", score)   # 1.0
print()


# =============================================================
# PART 7: COMPARISON OPERATORS (result is True / False)
# =============================================================
print("=== Part 7: Comparison Operators ===")

m, n = 10, 20
print(f"{m} == {n} : {m == n}")    # equal
print(f"{m} != {n} : {m != n}")    # not equal
print(f"{m} >  {n} : {m > n}")
print(f"{m} <  {n} : {m < n}")
print(f"{m} >= {n} : {m >= n}")
print(f"{m} <= {n} : {m <= n}")
print()


# =============================================================
# PART 8: LOGICAL OPERATORS - and, or, not
# =============================================================
print("=== Part 8: Logical Operators ===")

has_laptop = True
has_internet = False
print("Can join online class (and):", has_laptop and has_internet)  # False
print("Can study something (or)   :", has_laptop or has_internet)   # True
print("No internet (not)          :", not has_internet)             # True

age = 28
print("Age between 18 and 60      :", age >= 18 and age <= 60)      # True
print()


# =============================================================
# PART 9: MEMBERSHIP & IDENTITY OPERATORS
# =============================================================
print("=== Part 9: Membership & Identity ===")

tools = ["ADF", "Databricks", "Synapse"]
print("'ADF' in tools        :", "ADF" in tools)          # True
print("'Snowflake' not in    :", "Snowflake" not in tools)  # True
print("'Eagle' in course     :", "Eagle" in course)       # True

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("list1 == list2 (same values) :", list1 == list2)   # True
print("list1 is list2 (same object) :", list1 is list2)   # False
print("list1 is list3 (same object) :", list1 is list3)   # True
print("skills is None               :", skills is None)   # True
print()


# =============================================================
# PART 10: OPERATOR PRECEDENCE (order of calculation)
# =============================================================
print("=== Part 10: Operator Precedence ===")
# Order: ()  ->  **  ->  * / // %  ->  + -  ->  comparisons  ->  not -> and -> or
print("2 + 3 * 4     =", 2 + 3 * 4)       # 14  (multiply first)
print("(2 + 3) * 4   =", (2 + 3) * 4)     # 20  (brackets first)
print("2 ** 3 ** 2   =", 2 ** 3 ** 2)     # 512 (power goes right to left)
print()


# =============================================================
# PART 11: MINI PROJECT - Simple Salary Calculator
# =============================================================
print("=== Part 11: Mini Project - Salary Calculator ===")

monthly_salary = 125000
bonus_percent = 10
tax_percent = 20

yearly_salary = monthly_salary * 12
bonus = yearly_salary * bonus_percent / 100
gross = yearly_salary + bonus
tax = gross * tax_percent / 100
net = gross - tax

print(f"Yearly salary : Rs {yearly_salary:,.2f}")
print(f"Bonus ({bonus_percent}%)   : Rs {bonus:,.2f}")
print(f"Gross income  : Rs {gross:,.2f}")
print(f"Tax ({tax_percent}%)     : Rs {tax:,.2f}")
print(f"Net income    : Rs {net:,.2f}")
print(f"Monthly in-hand (approx): Rs {net / 12:,.2f}")
print()


# =============================================================
# PART 12: USER INPUT (uncomment to try)
# input() always returns a str - convert it with int() / float()
# =============================================================
# user_name = input("Enter your name: ")
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# print(f"Hi {user_name}! {n1} + {n2} = {n1 + n2}")
# print(f"{n1} is even? {n1 % 2 == 0}")

print("Day 1 complete!")