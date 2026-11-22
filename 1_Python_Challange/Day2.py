"""
DAY 2 - Python Data Types
Numbers, Strings, Lists, Tuples, Sets, Dictionaries, Booleans
Author : Kavitha Pandiyan
Course : SocialEagleAI - 10 Days Python Challenge
Run    : python Day2.py   (or click the Run button in VS Code)
"""

# =============================================================
# PART 1: OVERVIEW - Python's built-in data types
# =============================================================
print("=== Part 1: Data Types Overview ===")

examples = [
    42,                         # int
    3.14,                       # float
    2 + 3j,                     # complex
    "Hello",                    # str
    [1, 2, 3],                  # list
    (1, 2, 3),                  # tuple
    {1, 2, 3},                  # set
    {"name": "Kavitha"},        # dict
    True,                       # bool
    None,                       # NoneType
]
for value in examples:
    print(f"{str(value):<20} -> {type(value).__name__}")

# Mutable   (can change after creation): list, set, dict
# Immutable (cannot change)            : int, float, str, tuple, bool
print()


# =============================================================
# PART 2: NUMBERS - int, float, complex
# =============================================================
print("=== Part 2: Numbers ===")

count = 100                 # int - no size limit in Python
big = 10 ** 30
pi = 3.14159                # float
z = 4 + 5j                  # complex (real + imaginary)

print("int    :", count, "| big int:", big)
print("float  :", pi)
print("complex:", z, "| real:", z.real, "| imag:", z.imag)
print("1_000_000 is readable:", 1_000_000)   # underscores for readability

# Useful number functions
print("abs(-7)        =", abs(-7))
print("round(3.4567,2)=", round(3.4567, 2))
print("max(4, 9, 2)   =", max(4, 9, 2))
print("min(4, 9, 2)   =", min(4, 9, 2))
print("pow(2, 5)      =", pow(2, 5))
print("divmod(17, 5)  =", divmod(17, 5))     # (quotient, remainder)

import math
print("math.sqrt(49)  =", math.sqrt(49))
print("math.ceil(4.2) =", math.ceil(4.2))    # round up
print("math.floor(4.8)=", math.floor(4.8))   # round down

# Float precision gotcha
print("0.1 + 0.2      =", 0.1 + 0.2)         # 0.30000000000000004
print("rounded        =", round(0.1 + 0.2, 2))
print()


# =============================================================
# PART 3: STRINGS - text (immutable)
# =============================================================
print("=== Part 3: Strings ===")

s = "  Social Eagle AI  "
text = "python is fun"
multi = """This is
a multi-line string"""

print(multi)
print("Original   :", repr(s))
print("strip()    :", repr(s.strip()))        # remove spaces at both ends
print("upper()    :", text.upper())
print("title()    :", text.title())
print("capitalize:", text.capitalize())
print("replace()  :", text.replace("fun", "powerful"))
print("split()    :", text.split())           # -> list of words
print("join()     :", "-".join(["a", "b", "c"]))
print("find('is') :", text.find("is"))        # index of first match
print("count('n') :", text.count("n"))
print("startswith :", text.startswith("py"))
print("isdigit    :", "2026".isdigit())

# Indexing & slicing   p  y  t  h  o  n
#                      0  1  2  3  4  5
#                     -6 -5 -4 -3 -2 -1
word = "python"
print("word[0]    :", word[0])
print("word[-1]   :", word[-1])
print("word[1:4]  :", word[1:4])     # yth (end index not included)
print("word[:3]   :", word[:3])      # pyt
print("word[::-1] :", word[::-1])    # reverse -> nohtyp

# Strings are immutable: word[0] = "P" would give an error
word = "P" + word[1:]                # create a new string instead
print("New word   :", word)
print()


# =============================================================
# PART 4: LISTS - ordered, changeable, allows duplicates  [ ]
# =============================================================
print("=== Part 4: Lists ===")

tools = ["ADF", "Databricks", "Synapse"]
print("List       :", tools)
print("First item :", tools[0], "| Last:", tools[-1])
print("Length     :", len(tools))

tools.append("Power BI")           # add at end
print("append     :", tools)
tools.insert(1, "SQL")             # add at position
print("insert     :", tools)
tools.extend(["Python", "Spark"])  # add many
print("extend     :", tools)
tools.remove("SQL")                # remove by value
print("remove     :", tools)
last = tools.pop()                 # remove last & return it
print("pop        :", last, "->", tools)
tools[0] = "Azure Data Factory"    # change an item
print("update     :", tools)

  

# List comprehension - build a list in one line
squares = [n ** 2 for n in range(1, 6)]
evens = [n for n in range(1, 11) if n % 2 == 0]
print("squares    :", squares)
print("evens      :", evens)

# Nested list (like a table)
matrix = [[1, 2, 3], [4, 5, 6]]
print("matrix[1][2]:", matrix[1][2])          # 6
print()


# =============================================================
# PART 5: TUPLES - ordered, NOT changeable  ( )
# =============================================================
print("=== Part 5: Tuples ===")

location = (13.0827, 80.2707)      # Chennai lat, long - should not change
days = ("Mon", "Tue", "Wed", "Mon")
single = ("only",)                 # one-item tuple needs a comma!

print("location   :", location)
print("days[1]    :", days[1])
print("count Mon  :", days.count("Mon"))
print("index Wed  :", days.index("Wed"))
print("single     :", single, type(single).__name__)

# Tuple unpacking
lat, lon = location
print(f"Latitude {lat}, Longitude {lon}")

# Tuples are immutable: location[0] = 0 would give an error
# Convert if you really need to change it
temp = list(days)
temp.append("Thu")
days = tuple(temp)
print("new tuple  :", days)
print()


# =============================================================
# PART 6: SETS - unordered, unique items only  { }
# =============================================================
print("=== Part 6: Sets ===")

skills = {"Python", "SQL", "Spark", "Python"}   # duplicate removed
print("skills     :", skills)
skills.add("GenAI")
skills.discard("Spark")            # no error if missing (remove() would error)
print("add/discard:", skills)

# Remove duplicates from a list
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com"]
print("unique     :", sorted(set(emails)))

# Set operations
my_skills = {"Python", "SQL", "Azure"}
job_needs = {"Python", "GenAI", "Azure", "LangChain"}
print("Have & need (intersection):", my_skills & job_needs)
print("All skills  (union)       :", my_skills | job_needs)
print("To learn    (difference)  :", job_needs - my_skills)
print("Not common  (sym diff)    :", my_skills ^ job_needs)

empty_set = set()                  # {} creates an empty DICT, not a set
print("empty set  :", type(empty_set).__name__, "| {} is", type({}).__name__)
print()


# =============================================================
# PART 7: DICTIONARIES - key : value pairs  { }
# =============================================================
print("=== Part 7: Dictionaries ===")

student = {
    "name": "Kavitha",
    "course": "SocialEagleAI",
    "day": 2,
    "skills": ["Python", "Azure"],
}
print("dict       :", student)
print("name       :", student["name"])
print("get()      :", student.get("city", "Not set"))   # safe - no error

student["day"] = 3                     # update
student["city"] = "Chennai"            # add new key
print("updated    :", student)
student.pop("city")                    # remove key
print("after pop  :", student)

print("keys()     :", list(student.keys()))
print("values()   :", list(student.values()))
print("'name' in  :", "name" in student)

# Loop through a dictionary
for key, value in student.items():
    print(f"  {key:<8}: {value}")

student.update({"level": "Beginner", "day": 2})
print("update()   :", student)

# Nested dictionary
team = {
    "emp1": {"name": "Kavitha", "role": "Data Engineer"},
    "emp2": {"name": "Arun", "role": "ML Engineer"},
}
print("emp2 role  :", team["emp2"]["role"])

# Dictionary comprehension
square_map = {n: n ** 2 for n in range(1, 6)}
print("square_map :", square_map)
print()


# =============================================================
# PART 8: BOOLEANS - True / False
# =============================================================
print("=== Part 8: Booleans ===")

is_active = True
print("is_active  :", is_active, type(is_active).__name__)
print("5 > 3      :", 5 > 3)
print("True + True:", True + True)      # True = 1, False = 0

# "Falsy" values - all become False
falsy = [0, 0.0, "", [], (), {}, set(), None, False]
print("Falsy      :", [bool(v) for v in falsy])

# "Truthy" values - everything else
truthy = [1, -5, "hi", [0], (1,), {"a": 1}, True]
print("Truthy     :", [bool(v) for v in truthy])

cart = []
if not cart:                           # Pythonic empty check
    print("Cart is empty")

print("any([0,0,1]):", any([0, 0, 1]))  # True if at least one is True
print("all([1,1,0]):", all([1, 1, 0]))  # True only if all are True
print()


# =============================================================
# PART 9: TYPE CONVERSION BETWEEN COLLECTIONS
# =============================================================
print("=== Part 9: Converting Between Types ===")

print("list('abc')        :", list("abc"))
print("tuple([1, 2])      :", tuple([1, 2]))
print("set([1, 1, 2])     :", set([1, 1, 2]))
print("dict(zip(k, v))    :", dict(zip(["a", "b"], [1, 2])))
print("list(dict.items()) :", list({"x": 1, "y": 2}.items()))
print("str(123) + '4'     :", str(123) + "4")
print("int('123') + 4     :", int("123") + 4)
print()


# =============================================================
# PART 10: QUICK COMPARISON TABLE
# =============================================================
print("=== Part 10: Collections Cheat Sheet ===")
print(f"{'Type':<7}{'Symbol':<9}{'Ordered':<9}{'Changeable':<12}{'Duplicates'}")
print(f"{'list':<7}{'[ ]':<9}{'Yes':<9}{'Yes':<12}{'Yes'}")
print(f"{'tuple':<7}{'( )':<9}{'Yes':<9}{'No':<12}{'Yes'}")
print(f"{'set':<7}{'{ }':<9}{'No':<9}{'Yes':<12}{'No'}")
print(f"{'dict':<7}{'{k:v}':<9}{'Yes':<9}{'Yes':<12}{'Keys: No'}")
print()


# =============================================================
# PART 11: MINI PROJECT - Student Marks Report
# Uses: dict, list, tuple, set, numbers, strings, booleans
# =============================================================
print("=== Part 11: Mini Project - Student Marks Report ===")

marks = {
    "Kavitha": [92, 88, 95],
    "Arun": [75, 64, 80],
    "Priya": [55, 42, 60],
    "Rahul": [88, 91, 79],
}
subjects = ("Python", "SQL", "AI")      # fixed -> tuple
pass_mark = 50

passed = set()
print(f"{'Name':<10}{'Total':>6}{'Avg':>8}  {'Grade':<6}{'Result'}")
print("-" * 40)
for name, scores in marks.items():
    total = sum(scores)
    avg = total / len(scores)
    all_passed = all(score >= pass_mark for score in scores)   # boolean
    if avg >= 90:
        grade = "A+"
    elif avg >= 75:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    else:
        grade = "C"
    if all_passed:
        passed.add(name)
    result = "PASS" if all_passed else "FAIL"
    print(f"{name:<10}{total:>6}{avg:>8.2f}  {grade:<6}{result}")

print("-" * 40)
topper = max(marks, key=lambda n: sum(marks[n]))
print("Topper     :", topper)
print("Passed     :", sorted(passed))
print("Failed     :", sorted(set(marks) - passed))

# Subject-wise highest score
for i, subject in enumerate(subjects):
    best = max(marks, key=lambda n: marks[n][i])
    print(f"Best in {subject:<7}: {best} ({marks[best][i]})")
print()

print("Day 2 complete!")