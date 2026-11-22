"""
DAY 5 - Lists in Depth
Creating lists, indexing, slicing, operations, all list methods
Author : Kavitha Pandiyan
Course : SocialEagleAI - 10 Days Python Challenge
Run    : python Day5.py   (or click the Run button in VS Code)

Note: every PART creates its own variables, so you can select
and run any single part on its own.
"""

# =============================================================
# PART 1: CREATING LISTS
# A list is ordered, changeable, allows duplicates and mixed types.
# =============================================================
print("=== Part 1: Creating Lists ===")

empty1 = []
empty2 = list()
numbers = [10, 20, 30, 40, 50]
mixed = ["Kavitha", 8, 125000.5, True, None]
nested = [[1, 2], [3, 4], [5, 6]]
from_string = list("AI")                 # ['A', 'I']
from_range = list(range(1, 6))           # [1, 2, 3, 4, 5]
repeated = [0] * 5                       # [0, 0, 0, 0, 0]

print("empty1      :", empty1, "| empty2:", empty2)
print("numbers     :", numbers)
print("mixed       :", mixed)
print("nested      :", nested)
print("from_string :", from_string)
print("from_range  :", from_range)
print("repeated    :", repeated)
print("type        :", type(numbers).__name__)
print()


# =============================================================
# PART 2: INDEXING - access one item by position
#
#   tools =  [ "ADF", "Databricks", "Synapse", "Power BI", "Python" ]
#   index  :     0         1            2          3          4
#   negative:   -5        -4           -3         -2         -1
# =============================================================
print("=== Part 2: Indexing ===")

tools = ["ADF", "Databricks", "Synapse", "Power BI", "Python"]
print("tools[0]    :", tools[0])          # first
print("tools[2]    :", tools[2])          # third
print("tools[-1]   :", tools[-1])         # last
print("tools[-2]   :", tools[-2])         # second last
print("last (len)  :", tools[len(tools) - 1])

# Change an item using its index
tools[1] = "Azure Databricks"
print("after change:", tools)

# Index of a character inside an item
print("tools[0][1] :", tools[0][1])       # 'D' from "ADF"

# Nested list indexing  [row][column]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("matrix[1]   :", matrix[1])         # [4, 5, 6]
print("matrix[1][2]:", matrix[1][2])      # 6
print("matrix[-1][0]:", matrix[-1][0])    # 7

# IndexError - accessing an index that does not exist
try:
    print(tools[10])
except IndexError as e:
    print("tools[10]   -> IndexError:", e)
print()


# =============================================================
# PART 3: SLICING - get a part of the list
# Syntax: list[start : stop : step]   (stop is NOT included)
# =============================================================
print("=== Part 3: Slicing ===")

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("nums          :", nums)
print("nums[2:5]     :", nums[2:5])       # [2, 3, 4]
print("nums[:4]      :", nums[:4])        # first 4
print("nums[6:]      :", nums[6:])        # from index 6 to end
print("nums[-3:]     :", nums[-3:])       # last 3
print("nums[:-3]     :", nums[:-3])       # all except last 3
print("nums[::2]     :", nums[::2])       # every 2nd item (even index)
print("nums[1::2]    :", nums[1::2])      # odd index items
print("nums[::-1]    :", nums[::-1])      # reversed
print("nums[7:2:-1]  :", nums[7:2:-1])    # backwards slice
print("nums[:]       :", nums[:])         # full copy

# Slicing never gives IndexError
print("nums[5:100]   :", nums[5:100])

# Replace / insert / delete using slices
letters = ["a", "b", "c", "d", "e"]
letters[1:3] = ["B", "C"]                # replace 2 items
print("replace slice :", letters)
letters[1:1] = ["x", "y"]                # insert without removing
print("insert slice  :", letters)
letters[1:3] = []                        # delete items
print("delete slice  :", letters)
print()


# =============================================================
# PART 4: LIST OPERATIONS
# =============================================================
print("=== Part 4: List Operations ===")

a = [1, 2, 3]
b = [4, 5]

print("a + b        :", a + b)            # concatenation (joins)
print("a * 3        :", a * 3)            # repetition
print("3 in a       :", 3 in a)           # membership
print("9 not in a   :", 9 not in a)
print("len(a)       :", len(a))
print("a == [1,2,3] :", a == [1, 2, 3])   # compare values
print("[1,2] < [1,3]:", [1, 2] < [1, 3])  # compares item by item

# Unpacking
first, second, third = a
print("unpacked     :", first, second, third)
head, *rest = [10, 20, 30, 40]
print("head, *rest  :", head, rest)
*start, last = [10, 20, 30, 40]
print("*start, last :", start, last)

# del keyword
items = ["pen", "book", "bag", "box"]
del items[0]
print("del items[0] :", items)
del items[-2:]
print("del items[-2:]:", items)
print()


# =============================================================
# PART 5: ADDING ITEMS - append, insert, extend
# =============================================================
print("=== Part 5: Adding Items ===")

skills = ["Python", "SQL"]

skills.append("Spark")                   # add ONE item at the end
print("append('Spark')     :", skills)

skills.insert(1, "Azure")                # add at a position
print("insert(1, 'Azure')  :", skills)

skills.extend(["GenAI", "LangChain"])    # add MANY items at the end
print("extend([...])       :", skills)

# Common mistake: append vs extend with a list
x = [1, 2]
y = [1, 2]
x.append([3, 4])                         # adds the list as ONE item
y.extend([3, 4])                         # adds each item
print("append([3,4])       :", x)        # [1, 2, [3, 4]]
print("extend([3,4])       :", y)        # [1, 2, 3, 4]
print()


# =============================================================
# PART 6: REMOVING ITEMS - remove, pop, clear
# =============================================================
print("=== Part 6: Removing Items ===")

fruits = ["apple", "banana", "mango", "banana", "grapes"]
print("start               :", fruits)

fruits.remove("banana")                  # removes FIRST match by value
print("remove('banana')    :", fruits)

last_item = fruits.pop()                 # removes & returns LAST item
print("pop()               :", last_item, "->", fruits)

second = fruits.pop(1)                   # removes & returns by index
print("pop(1)              :", second, "->", fruits)

# remove() gives an error if the value is missing - check first
if "kiwi" in fruits:
    fruits.remove("kiwi")
else:
    print("kiwi not in list - nothing removed")

fruits.clear()                           # remove everything
print("clear()             :", fruits)
print()


# =============================================================
# PART 7: SEARCHING & COUNTING - index, count
# =============================================================
print("=== Part 7: index() & count() ===")

marks = [78, 92, 65, 92, 88, 92]
print("marks               :", marks)
print("count(92)           :", marks.count(92))     # how many times
print("index(92)           :", marks.index(92))     # first position
print("index(92, 2)        :", marks.index(92, 2))  # search from index 2

# All positions of a value
positions = [i for i, m in enumerate(marks) if m == 92]
print("all positions of 92 :", positions)
print()


# =============================================================
# PART 8: SORTING & REVERSING - sort, reverse
# =============================================================
print("=== Part 8: sort() & reverse() ===")

scores = [45, 12, 89, 33, 67]
scores.sort()                             # changes the list itself
print("sort()              :", scores)
scores.sort(reverse=True)
print("sort(reverse=True)  :", scores)
scores.reverse()                          # just flips the order
print("reverse()           :", scores)

names = ["priya", "Arun", "kavitha", "Divya"]
names.sort()
print("sort strings        :", names)     # capitals come first!
names.sort(key=str.lower)
print("sort(key=str.lower) :", names)     # case-insensitive
names.sort(key=len)
print("sort(key=len)       :", names)     # by length

# sort() vs sorted()
original = [3, 1, 2]
new_list = sorted(original)               # returns a NEW list
print("sorted() new list   :", new_list, "| original:", original)
result = original.sort()                  # changes original, returns None
print("sort() returns      :", result, "| original:", original)

# Sort a list of tuples / dictionaries
employees = [("Kavitha", 125000), ("Arun", 110000), ("Priya", 95000)]
employees.sort(key=lambda emp: emp[1], reverse=True)
print("by salary (desc)    :", employees)
print()


# =============================================================
# PART 9: COPYING - copy() vs = (very important!)
# =============================================================
print("=== Part 9: Copying Lists ===")

original = ["a", "b", "c"]
same = original                # NOT a copy - both names point to ONE list
copied = original.copy()       # a real copy (also: original[:] or list(original))

original.append("d")
print("original            :", original)
print("same (= assignment) :", same, "<- changed too!")
print("copied (.copy())    :", copied, "<- safe")

# Nested lists need deepcopy
import copy
team = [["Kavitha", "Arun"], ["Priya"]]
shallow = team.copy()
deep = copy.deepcopy(team)
team[0].append("Rahul")
print("shallow copy        :", shallow, "<- inner list changed!")
print("deep copy           :", deep, "<- fully safe")
print()


# =============================================================
# PART 10: BUILT-IN FUNCTIONS for lists
# =============================================================
print("=== Part 10: Built-in Functions ===")

data = [23, 7, 45, 12, 38]
print("data                :", data)
print("len()               :", len(data))
print("sum()               :", sum(data))
print("min() / max()       :", min(data), "/", max(data))
print("average             :", sum(data) / len(data))
print("sorted()            :", sorted(data))
print("list(reversed())    :", list(reversed(data)))
print("any(x > 40)         :", any(x > 40 for x in data))
print("all(x > 5)          :", all(x > 5 for x in data))
print("list(enumerate())   :", list(enumerate(data)))
print("list(zip())         :", list(zip(["a", "b", "c"], [1, 2, 3])))
print("list(map(str))      :", list(map(str, data)))
print("list(filter(even))  :", list(filter(lambda x: x % 2 == 0, data)))
print()


# =============================================================
# PART 11: LIST COMPREHENSIONS
# Syntax: [expression for item in list if condition]
# =============================================================
print("=== Part 11: List Comprehensions ===")

prices = [100, 250, 80, 400, 150]
print("prices              :", prices)
print("with 18% GST        :", [round(p * 1.18, 2) for p in prices])
print("only above 120      :", [p for p in prices if p > 120])
print("label cheap/costly  :", ["costly" if p > 200 else "cheap" for p in prices])

words = ["  python ", "SQL", " GenAI  "]
print("cleaned words       :", [w.strip().lower() for w in words])

flat = [n for row in [[1, 2], [3, 4], [5, 6]] for n in row]
print("flatten nested      :", flat)
print()


# =============================================================
# PART 12: METHODS CHEAT SHEET
# =============================================================
print("=== Part 12: List Methods Cheat Sheet ===")
cheat_sheet = [
    ("append(x)",      "Add x at the end"),
    ("extend(list)",   "Add all items of another list"),
    ("insert(i, x)",   "Add x at position i"),
    ("remove(x)",      "Remove first x (error if missing)"),
    ("pop(i)",         "Remove & return item at i (default last)"),
    ("clear()",        "Remove all items"),
    ("index(x)",       "Position of first x"),
    ("count(x)",       "How many times x appears"),
    ("sort()",         "Sort in place (key=, reverse=)"),
    ("reverse()",      "Reverse in place"),
    ("copy()",         "Shallow copy of the list"),
]
for method, meaning in cheat_sheet:
    print(f"  {method:<15} -> {meaning}")
print()


# =============================================================
# PART 13: MINI PROJECT - To-Do List Manager
# Uses: append, insert, remove, pop, index, count, sort, slicing
# =============================================================
print("=== Part 13: Mini Project - To-Do Manager ===")

todo = []
done = []

def show():
    print("  To-Do:", todo if todo else "(empty)")
    print("  Done :", done if done else "(empty)")

# Add tasks
todo.append("Finish Day 5 Python")
todo.append("Push code to GitHub")
todo.append("Watch Day 6 video")
todo.insert(0, "Revise Day 4 loops")       # urgent task goes first
print("After adding tasks:")
show()

# Complete the first task
finished = todo.pop(0)
done.append(finished)
print(f"\nCompleted: {finished}")
show()

# Complete a task by name
task = "Push code to GitHub"
if task in todo:
    todo.remove(task)
    done.append(task)
    print(f"\nCompleted: {task}")
show()

# Summary
total = len(todo) + len(done)
percent = len(done) / total * 100
print(f"\nProgress: {len(done)}/{total} tasks ({percent:.0f}%)")
print("Next task:", todo[0] if todo else "All done!")
print("Tasks sorted A-Z:", sorted(todo + done))
print()


# =============================================================
# PART 14: TRY IT YOURSELF (uncomment to run)
# =============================================================
# shopping = []
# while True:
#     item = input("Add item (or 'done'): ").strip()
#     if item.lower() == "done":
#         break
#     if item in shopping:
#         print(f"{item} already in list")
#     else:
#         shopping.append(item)
# shopping.sort()
# print("Your shopping list:")
# for i, item in enumerate(shopping, start=1):
#     print(f"{i}. {item}")

print("Day 5 complete!")