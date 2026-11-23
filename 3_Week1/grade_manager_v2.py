# =====================================================================
#  WEEK 1 - DAY 2: STUDENT GRADE MANAGER  (VERSION 2 - IMPROVED)
#  Built with : Python only (standard library, nothing to install)
#  How to run : python grade_manager_v2.py
#  Run tests  : python grade_manager_v2.py --test
# =====================================================================
#
#  WHAT'S NEW COMPARED WITH VERSION 1
#  1. Data is SAVED to students.json, so it survives closing the program
#  2. Every student gets a unique ROLL NUMBER (101, 102, ...), so two
#     students called "Priya" are easy to tell apart
#  3. Edit a mark and delete a student (full CRUD)
#  4. Sort results by roll number, mark (with rank) or name
#  5. Grade summary (A: 1, B: 0 ...) and pass / fail count
#  6. Search students by name
#  7. Grade scale kept as DATA (GRADE_SCALE), not a long if/elif chain
#  8. Built-in automatic tests:  python grade_manager_v2.py --test
#  9. Decimal marks allowed, e.g. 92.5
# 10. Type hints on every function
# =====================================================================


# ---------------------------------------------------------------------
#  SECTION 1: IMPORTS AND SETTINGS
# ---------------------------------------------------------------------
import json                     # save / load data as JSON text
import sys                      # read command-line words like --test
from pathlib import Path        # build file paths that work on any computer

# students.json is saved in the SAME folder as this script
DATA_FILE = Path(__file__).parent / "students.json"

# Grade scale as data: (lowest mark for the grade, grade).
# Checked from the top, so the first match wins. Change the scale here only.
GRADE_SCALE = [(90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "E")]
PASS_MARK = 60                  # below 60 = grade E = fail
FIRST_ROLL = 101                # roll numbers start here


# ---------------------------------------------------------------------
#  SECTION 2: DATA
# ---------------------------------------------------------------------
# A list of dictionaries: {"roll": 101, "name": "Priya", "mark": 92}
students: list[dict] = []


# ---------------------------------------------------------------------
#  SECTION 3: CORE LOGIC (no input / print here, so it is easy to test)
# ---------------------------------------------------------------------
def get_grade(mark: float) -> str:
    """Return 'A' to 'E' for a mark from 0 to 100."""
    for lowest, grade in GRADE_SCALE:
        if mark >= lowest:
            return grade
    return "E"                  # safety net; 0 already matches above


def next_roll() -> int:
    """Next free roll number: one more than the biggest used so far."""
    if not students:
        return FIRST_ROLL
    return max(s["roll"] for s in students) + 1


def find_by_roll(roll: int) -> dict | None:
    """Return the student with this roll number, or None if not found."""
    for s in students:
        if s["roll"] == roll:
            return s
    return None


def format_mark(mark: float) -> str:
    """Show 92.0 as '92' and 92.5 as '92.5'."""
    return f"{mark:g}"


# ---------------------------------------------------------------------
#  SECTION 4: SAVE AND LOAD (file handling)
# ---------------------------------------------------------------------
def save_students() -> None:
    """Write the whole list to students.json."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=2)


def load_students() -> None:
    """Read students.json at start-up, if it exists."""
    if not DATA_FILE.exists():
        return                                  # first run: nothing saved yet
    try:
        with open(DATA_FILE, encoding="utf-8") as f:
            students.extend(json.load(f))
        print(f"Loaded {len(students)} student(s) from {DATA_FILE.name}")
    except (json.JSONDecodeError, OSError):
        # File is damaged: keep a copy and start fresh instead of crashing
        backup = DATA_FILE.with_suffix(".bak")
        DATA_FILE.replace(backup)
        print(f"Warning: {DATA_FILE.name} was damaged. Saved a copy as {backup.name}.")


# ---------------------------------------------------------------------
#  SECTION 5: INPUT HELPERS (all validation lives here)
# ---------------------------------------------------------------------
def ask_name(prompt: str = "Student name: ") -> str:
    """Keep asking until the name is not empty."""
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("  Name cannot be empty. Please try again.")


def ask_mark(prompt: str = "Mark (0-100): ") -> float:
    """Keep asking until the mark is a number from 0 to 100 (decimals allowed)."""
    while True:
        text = input(prompt).strip()
        try:
            mark = float(text)                  # "abc" or "" -> ValueError
        except ValueError:
            print("  Please enter a number, e.g. 85 or 85.5.")
            continue
        if 0 <= mark <= 100:
            return mark
        print("  Mark must be between 0 and 100.")


def ask_roll() -> dict | None:
    """Ask for a roll number and return that student, or None."""
    text = input("Roll number: ").strip()
    try:
        roll = int(text)
    except ValueError:
        print("  Roll number must be a whole number, e.g. 101.")
        return None
    student = find_by_roll(roll)
    if student is None:
        print(f"  No student with roll number {roll}.")
    return student


def has_students() -> bool:
    """Print a message and return False when the list is empty."""
    if not students:
        print("  No students yet. Choose 1 to add a student first.")
        return False
    return True


# ---------------------------------------------------------------------
#  SECTION 6: MENU ACTIONS
# ---------------------------------------------------------------------
def add_student() -> None:
    name = ask_name()
    same = [s for s in students if s["name"].lower() == name.lower()]
    if same:
        rolls = ", ".join(str(s["roll"]) for s in same)
        print(f"  Note: '{name}' already exists (roll {rolls}). Adding as a new student.")
    mark = ask_mark()
    student = {"roll": next_roll(), "name": name, "mark": mark}
    students.append(student)
    save_students()
    print(f"  Added roll {student['roll']}: {name}, {format_mark(mark)} ({get_grade(mark)})")


def print_table(rows: list[dict], show_rank: bool = False) -> None:
    """Print students as an aligned table."""
    width = max(10, max(len(s["name"]) for s in rows) + 2)
    rank_head = "Rank  " if show_rank else ""
    header = f"{rank_head}{'Roll':<6}{'Name':<{width}}{'Mark':>6}   {'Grade':^5}"
    print()
    print(header)
    print("-" * len(header))
    for i, s in enumerate(rows, start=1):
        rank = f"{i:<6}" if show_rank else ""
        print(f"{rank}{s['roll']:<6}{s['name']:<{width}}"
              f"{format_mark(s['mark']):>6}   {get_grade(s['mark']):^5}")
    print("-" * len(header))


def show_results() -> None:
    if not has_students():
        return

    print("Sort by:  1. Roll number   2. Mark (high to low)   3. Name")
    choice = input("Choose 1, 2 or 3 (Enter = 1): ").strip() or "1"
    if choice == "2":
        rows = sorted(students, key=lambda s: s["mark"], reverse=True)
    elif choice == "3":
        rows = sorted(students, key=lambda s: s["name"].lower())
    else:
        rows = sorted(students, key=lambda s: s["roll"])
    print_table(rows, show_rank=(choice == "2"))

    # Class statistics
    marks = [s["mark"] for s in students]
    average = sum(marks) / len(marks)
    print(f"Average: {average:.1f}    Highest: {format_mark(max(marks))}"
          f"    Lowest: {format_mark(min(marks))}")

    # Grade summary, built from GRADE_SCALE so it always matches
    counts = {grade: 0 for _, grade in GRADE_SCALE}
    for m in marks:
        counts[get_grade(m)] += 1
    print("Grades:  " + "  ".join(f"{g}: {n}" for g, n in counts.items()))

    passed = sum(1 for m in marks if m >= PASS_MARK)
    print(f"Passed: {passed}    Failed: {len(marks) - passed}    (pass mark {PASS_MARK})")
    print()


def search_student() -> None:
    if not has_students():
        return
    text = ask_name("Search name (part is fine): ").lower()
    matches = [s for s in students if text in s["name"].lower()]
    if matches:
        print_table(sorted(matches, key=lambda s: s["roll"]))
    else:
        print(f"  No student name contains '{text}'.")


def edit_mark() -> None:
    if not has_students():
        return
    student = ask_roll()
    if student is None:
        return
    old = student["mark"]
    print(f"  {student['name']} currently has {format_mark(old)} ({get_grade(old)}).")
    student["mark"] = ask_mark("New mark (0-100): ")
    save_students()
    print(f"  Updated: {format_mark(old)} -> {format_mark(student['mark'])}"
          f" ({get_grade(student['mark'])})")


def delete_student() -> None:
    if not has_students():
        return
    student = ask_roll()
    if student is None:
        return
    sure = input(f"  Delete {student['name']} (roll {student['roll']})? (y/n): ").strip().lower()
    if sure == "y":
        students.remove(student)
        save_students()
        print("  Deleted.")
    else:
        print("  Cancelled.")


# ---------------------------------------------------------------------
#  SECTION 7: MENU LOOP
# ---------------------------------------------------------------------
MENU = {
    "1": ("Add student", add_student),
    "2": ("Show results", show_results),
    "3": ("Search student", search_student),
    "4": ("Edit a mark", edit_mark),
    "5": ("Delete a student", delete_student),
}


def main() -> None:
    print("=== Student Grade Manager v2 ===")
    load_students()
    while True:
        for key, (label, _) in MENU.items():
            print(f"{key}. {label}")
        print("6. Quit")
        choice = input("Choose 1-6: ").strip()

        if choice == "6":
            print("Saved. Goodbye!")
            break
        if choice in MENU:
            MENU[choice][1]()           # call the function stored in the menu
        else:
            print("  Please choose a number from 1 to 6.")


# ---------------------------------------------------------------------
#  SECTION 8: AUTOMATIC TESTS
# ---------------------------------------------------------------------
def run_tests() -> None:
    """Check every grade boundary. Prints OK or stops at the first failure."""
    cases = {100: "A", 90: "A", 89.9: "B", 89: "B", 80: "B", 79: "C", 70: "C",
             69: "D", 60: "D", 59.9: "E", 59: "E", 0: "E"}
    for mark, expected in cases.items():
        assert get_grade(mark) == expected, f"get_grade({mark}) should be {expected}"
    assert format_mark(92.0) == "92" and format_mark(92.5) == "92.5"
    print(f"All {len(cases) + 1} tests passed.")


# ---------------------------------------------------------------------
#  SECTION 9: START HERE
# ---------------------------------------------------------------------
if __name__ == "__main__":
    if "--test" in sys.argv:
        run_tests()
    else:
        try:
            main()
        except (KeyboardInterrupt, EOFError):
            print("\nSaved. Goodbye!")