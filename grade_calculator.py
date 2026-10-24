# Simple Student Grade Calculator for PyCharm

def calculate_grade(score):
    """Determines letter grade based on test score."""
    if score >= 80:
        return "A (Excellent)"
    elif score >= 70:
        return "B (Good)"
    elif score >= 50:
        return "C (Pass)"
    else:
        return "F (Fail)"


def main():
    print("=== Student Performance Calculator ===")

    # Take student name and scores as input
    student_name = input("Enter student name: ")

    try:
        score1 = float(input("Enter Score 1 (0-100): "))
        score2 = float(input("Enter Score 2 (0-100): "))
        score3 = float(input("Enter Score 3 (0-100): "))

        # Calculate average
        average_score = (score1 + score2 + score3) / 3
        grade = calculate_grade(average_score)

        # Display results
        print("\n--- Final Results ---")
        print(f"Student: {student_name}")
        print(f"Average Score: {average_score:.2f}")
        print(f"Final Grade: {grade}")

    except ValueError:
        print("\nError: Please enter valid numbers for test scores!")


# Run the program
if __name__ == "__main__":
    main()
