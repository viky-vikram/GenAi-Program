def calculate_grade(mark):
    """
    Returns the grade based on the mark entered.
    """

    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark <= 89:
        return "B"
    elif 70 <= mark <= 79:
        return "C"
    elif 60 <= mark <= 69:
        return "D"
    else:
        return "E"


def main():
    print("=== Grade Calculator ===")

    try:
        # Get input from user
        mark = float(input("Enter mark (0-100): "))

        # Validate range
        if mark < 0 or mark > 100:
            print("Error: Mark must be between 0 and 100.")
            return

        # Calculate grade
        grade = calculate_grade(mark)

        # Display result
        print("\nResult")
        print("------")
        print(f"Mark Entered : {mark}")
        print(f"Grade        : {grade}")

    except ValueError:
        print("Error: Please enter a valid numeric value.")


# Program entry point
if __name__ == "__main__":
    main()