# VARIABLES AND DATA TYPES
student_count = 28                     # int
average_grade = 87.65                  # float
course_name = "Introduction to Python"  # string
is_passing = average_grade >= 60       # boolean
grades = [92, 78.5, 85, 91.25, 67]     # list

student = {                            # dictionary
    "name": "Jordan Lee",
    "id": 10423,
    "grades": grades
}

# FUNCTIONS


def calculate_average(numbers):
    """Function 1: returns the average of a list of numbers."""
    if len(numbers) == 0:
        raise ValueError("Can't average an empty list")
    return sum(numbers) / len(numbers)


def letter_grade(score):
    """Function 2: converts a numeric score into a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def print_report_card(student):
    """Function 3: prints a report card using the two functions above."""
    avg = calculate_average(student["grades"])
    print(f"Name: {student['name']}")
    print(f"Average: {avg:.2f}")
    print(f"Final Grade: {letter_grade(avg)}")

    # loop through each grade and show its letter grade
    for g in student["grades"]:
        print(f"  Score {g} -> {letter_grade(g)}")


# ERROR HANDLING


def safe_divide(a, b):
    """Divides two numbers safely, handling errors."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")
        return None
    except TypeError:
        print("Error: both values must be numbers.")
        return None
    else:
        print(f"{a} / {b} = {result}")
        return result

# MAIN PROGRAM


def main():
    print("--- Data Types ---")
    print(student_count, type(student_count))
    print(average_grade, type(average_grade))
    print(course_name, type(course_name))
    print(is_passing, type(is_passing))
    print(grades, type(grades))
    print(student, type(student))

    print("\n--- Report Card ---")
    print_report_card(student)

    print("\n--- Safe Division ---")
    safe_divide(10, 2)
    safe_divide(10, 0)
    safe_divide(10, "two")

    print("\n--- Handling a Raised Error ---")
    try:
        calculate_average([])
    except ValueError as e:
        print("Caught error:", e)

    print("\n--- While Loop Example ---")
    count = 0
    while count < 3:
        print("Loop number:", count)
        count += 1


if __name__ == "__main__":
    main()
