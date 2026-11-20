"""
DAY 1 CHALLENGE - Python Fundamentals, Variables & Operators
Run:  python day1_python_basics.py   (or click the Run button in VS Code)
"""

# ------------------------------------------------------------
# PROGRAM 1: Hello World + print basics
# ------------------------------------------------------------
print("=== Program 1: Hello World ===")
print("Hello, World!")
print("Name:", "Kavitha", "| Role:", "Azure Data Engineer")
print("Line 1\nLine 2")          # \n = new line
print("A", "B", "C", sep="-")    # sep changes the separator
print()

# ------------------------------------------------------------
# PROGRAM 2: Variables & data types
# ------------------------------------------------------------
print("=== Program 2: Variables & Data Types ===")
name = "Kavitha"          # str
experience = 8            # int
salary = 1500000.50       # float
is_learning_ai = True     # bool
skills = None             # NoneType

print(name, type(name))
print(experience, type(experience))
print(salary, type(salary))
print(is_learning_ai, type(is_learning_ai))
print(skills, type(skills))
print()

# ------------------------------------------------------------
# PROGRAM 3: Multiple assignment & swapping
# ------------------------------------------------------------
print("=== Program 3: Multiple Assignment & Swap ===")
a, b, c = 10, 20, 30
print("a, b, c =", a, b, c)

x = y = z = 0
print("x, y, z =", x, y, z)

a, b = b, a               # Pythonic swap (no temp variable)
print("After swap -> a =", a, ", b =", b)
print()

# ------------------------------------------------------------
# PROGRAM 4: Type conversion (casting)
# ------------------------------------------------------------
print("=== Program 4: Type Conversion ===")
num_str = "100"
num_int = int(num_str)
num_float = float(num_str)
back_to_str = str(num_int)

print(num_int + 50)           # 150 (math works now)
print(num_float)              # 100.0
print(back_to_str + "50")     # "10050" (string join)
print(int(9.99))              # 9 (decimal part dropped)
print(bool(0), bool(5), bool(""), bool("hi"))
print()

# ------------------------------------------------------------
# PROGRAM 5: Arithmetic operators
# ------------------------------------------------------------
print("=== Program 5: Arithmetic Operators ===")
a, b = 17, 5
print(f"{a} + {b}  = {a + b}")
print(f"{a} - {b}  = {a - b}")
print(f"{a} * {b}  = {a * b}")
print(f"{a} / {b}  = {a / b}")     # true division -> float
print(f"{a} // {b} = {a // b}")    # floor division
print(f"{a} % {b}  = {a % b}")     # remainder
print(f"{a} ** {b} = {a ** b}")    # power
print()

# ------------------------------------------------------------
# PROGRAM 6: Comparison operators
# ------------------------------------------------------------
print("=== Program 6: Comparison Operators ===")
x, y = 10, 20
print("x == y :", x == y)
print("x != y :", x != y)
print("x >  y :", x > y)
print("x <  y :", x < y)
print("x >= 10:", x >= 10)
print("y <= 15:", y <= 15)
print()

# ------------------------------------------------------------
# PROGRAM 7: Logical operators
# ------------------------------------------------------------
print("=== Program 7: Logical Operators ===")
age = 30
has_degree = True
print("age > 18 and has_degree :", age > 18 and has_degree)
print("age < 18 or has_degree  :", age < 18 or has_degree)
print("not has_degree          :", not has_degree)
print()

# ------------------------------------------------------------
# PROGRAM 8: Assignment operators
# ------------------------------------------------------------
print("=== Program 8: Assignment Operators ===")
n = 10
n += 5;  print("n += 5  ->", n)
n -= 3;  print("n -= 3  ->", n)
n *= 2;  print("n *= 2  ->", n)
n /= 4;  print("n /= 4  ->", n)
n //= 2; print("n //= 2 ->", n)
n **= 2; print("n **= 2 ->", n)
n %= 3;  print("n %= 3  ->", n)
print()

# ------------------------------------------------------------
# PROGRAM 9: Identity & membership operators
# ------------------------------------------------------------
print("=== Program 9: Identity & Membership ===")
tools = ["ADF", "Databricks", "Synapse"]
print("'ADF' in tools        :", "ADF" in tools)
print("'Snowflake' not in    :", "Snowflake" not in tools)
print("'Data' in 'Databricks':", "Data" in "Databricks")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("list1 == list2 :", list1 == list2)   # same values -> True
print("list1 is list2 :", list1 is list2)   # different objects -> False
print("list1 is list3 :", list1 is list3)   # same object -> True
print()

# ------------------------------------------------------------
# PROGRAM 10: Bitwise operators
# ------------------------------------------------------------
print("=== Program 10: Bitwise Operators ===")
p, q = 6, 3   # 6 = 110, 3 = 011
print(f"{p} & {q}  = {p & q}")     # AND  -> 010 = 2
print(f"{p} | {q}  = {p | q}")     # OR   -> 111 = 7
print(f"{p} ^ {q}  = {p ^ q}")     # XOR  -> 101 = 5
print(f"~{p}     = {~p}")          # NOT  -> -7
print(f"{p} << 1 = {p << 1}")      # left shift  -> 12
print(f"{p} >> 1 = {p >> 1}")      # right shift -> 3
print()

# ------------------------------------------------------------
# PROGRAM 11: Simple interest calculator
# ------------------------------------------------------------
print("=== Program 11: Simple Interest ===")
principal = 100000
rate = 7.5
years = 3
simple_interest = (principal * rate * years) / 100
print(f"Principal: Rs.{principal}, Rate: {rate}%, Years: {years}")
print(f"Simple Interest = Rs.{simple_interest:.2f}")
print(f"Total Amount    = Rs.{principal + simple_interest:.2f}")
print()

# ------------------------------------------------------------
# PROGRAM 12: Temperature converter
# ------------------------------------------------------------
print("=== Program 12: Temperature Converter ===")
celsius = 37
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
f_temp = 98.6
c_temp = (f_temp - 32) * 5 / 9
print(f"{f_temp}°F = {c_temp:.1f}°C")
print()

# ------------------------------------------------------------
# PROGRAM 13: Area & perimeter of a rectangle and circle
# ------------------------------------------------------------
print("=== Program 13: Area & Perimeter ===")
length, width = 12, 5
print(f"Rectangle -> Area: {length * width}, Perimeter: {2 * (length + width)}")
PI = 3.14159
radius = 7
print(f"Circle    -> Area: {PI * radius ** 2:.2f}, Circumference: {2 * PI * radius:.2f}")
print()

# ------------------------------------------------------------
# PROGRAM 14: Even or odd (using % and a conditional expression)
# ------------------------------------------------------------
print("=== Program 14: Even or Odd ===")
for number in [7, 12, 0, -3]:
    result = "Even" if number % 2 == 0 else "Odd"
    print(f"{number} is {result}")
print()

# ------------------------------------------------------------
# PROGRAM 15: Seconds -> hours, minutes, seconds (// and %)
# ------------------------------------------------------------
print("=== Program 15: Time Converter ===")
total_seconds = 10000
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{total_seconds} seconds = {hours}h {minutes}m {seconds}s")
print()

# ------------------------------------------------------------
# PROGRAM 16: Sum of digits of a 3-digit number
# ------------------------------------------------------------
print("=== Program 16: Sum of Digits ===")
num = 482
d1 = num // 100
d2 = (num // 10) % 10
d3 = num % 10
print(f"Digits of {num}: {d1}, {d2}, {d3} -> Sum = {d1 + d2 + d3}")
print()

# ------------------------------------------------------------
# PROGRAM 17: Operator precedence
# ------------------------------------------------------------
print("=== Program 17: Operator Precedence ===")
print("2 + 3 * 4        =", 2 + 3 * 4)        # 14 (* before +)
print("(2 + 3) * 4      =", (2 + 3) * 4)      # 20
print("2 ** 3 ** 2      =", 2 ** 3 ** 2)      # 512 (right to left)
print("10 - 4 - 3       =", 10 - 4 - 3)       # 3 (left to right)
print("not True or True =", not True or True) # True
print()

# ------------------------------------------------------------
# PROGRAM 18: User input (uncomment to try - it waits for typing)
# ------------------------------------------------------------
# print("=== Program 18: User Input ===")
# user_name = input("Enter your name: ")
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# print(f"Hi {user_name}! {n1} + {n2} = {n1 + n2}")

print("Day 1 complete!")


