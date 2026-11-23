# =====================================================================
#  WEEK 1 - DAY 2: STUDENT GRADE MANAGER
#  Built with : Python only (runs in the terminal, nothing to install)
#  How to run : python grade_manager.py
# =====================================================================
#
#  DESIGN DECISIONS
#  1. Storage: a LIST of DICTIONARIES, e.g. {"name": "Priya", "mark": 92}
#     - A list keeps every entry, so two students called "Priya" are both
#       saved. A dictionary like {"Priya": 92} would overwrite the first one.
#     - A list also keeps the order in which students were added.
#  2. Invalid input never crashes the program:
#     - empty name           -> ask again
#     - "abc" as a mark      -> int() fails -> caught with try/except
#     - 105 or -5            -> "Mark must be between 0 and 100"
#     - "show" before adding -> "No students added yet"
#     - wrong menu choice    -> "Please choose 1, 2 or 3"
#     - Ctrl+C               -> exits politely instead of a red error
# =====================================================================


# ---------------------------------------------------------------------
#  SECTION 1: DATA STORAGE
# ---------------------------------------------------------------------
students = []       # every student is a dictionary: {"name": ..., "mark": ...}


# ---------------------------------------------------------------------
#  SECTION 2: GRADE CALCULATION
# ---------------------------------------------------------------------
# Checks from the top down. A mark of 92 returns "A" at the first check,
# so later checks never need an upper limit (boundaries are inclusive).
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# ---------------------------------------------------------------------
#  SECTION 3: INPUT HELPERS (validation lives here)
# ---------------------------------------------------------------------
def ask_name():
    """Keep asking until the user types a name that is not empty."""
    while True:
        name = input("Student name: ").strip()     # strip() removes extra spaces
        if name:                                   # empty string counts as False
            return name
        print("  Name cannot be empty. Please try again.")


def ask_mark():
    """Keep asking until the user types a whole number from 0 to 100."""
    while True:
        text = input("Mark (0-100): ").strip()
        try:
            mark = int(text)                       # "abc", "" or "92.5" raise ValueError
        except ValueError:
            print("  Please enter a whole number, e.g. 85.")
            continue                               # go back to the top of the loop
        if 0 <= mark <= 100:
            return mark
        print("  Mark must be between 0 and 100.")


# ---------------------------------------------------------------------
#  SECTION 4: ADD A STUDENT
# ---------------------------------------------------------------------
def add_student():
    name = ask_name()

    # Same name already stored? Warn, but still allow it (two different Priyas)
    for s in students:
        if s["name"].lower() == name.lower():
            print(f"  Note: '{name}' already exists. Adding as a separate student.")
            break

    mark = ask_mark()
    students.append({"name": name, "mark": mark})
    print(f"  Added {name}: {mark} ({get_grade(mark)})")


# ---------------------------------------------------------------------
#  SECTION 5: SHOW RESULTS (aligned table + average, highest, lowest)
# ---------------------------------------------------------------------
def show_results():
    if not students:                               # empty list counts as False
        print("  No students added yet. Choose 1 to add a student first.")
        return

    # Make the Name column as wide as the longest name (at least 10)
    width = max(10, max(len(s["name"]) for s in students) + 2)

    # :<width = left-align, :>4 = right-align in 4 spaces, :^5 = centre in 5
    print()
    print(f"{'Name':<{width}}{'Mark':>4}   {'Grade':^5}")
    print("-" * (width + 12))
    for s in students:
        print(f"{s['name']:<{width}}{s['mark']:>4}   {get_grade(s['mark']):^5}")
    print("-" * (width + 12))

    marks = [s["mark"] for s in students]          # list of just the marks
    average = sum(marks) / len(marks)
    print(f"Average: {average:.1f}    Highest: {max(marks)}    Lowest: {min(marks)}")
    print()


# ---------------------------------------------------------------------
#  SECTION 6: MENU LOOP
# ---------------------------------------------------------------------
def main():
    print("=== Student Grade Manager ===")
    while True:
        print("1. Add student")
        print("2. Show results")
        print("3. Quit")
        choice = input("Choose 1, 2 or 3: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_results()
        elif choice == "3":
            print("Goodbye!")
            break                                  # leave the while loop
        else:
            print("  Please choose 1, 2 or 3.")


# Run main() only when this file is run directly (not when imported).
# Ctrl+C or a closed input ends the program politely instead of crashing.
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")