
def calculate_average(scores_list):
    if not scores_list:
        return 0
    
    total_score = sum(scores_list)
    number_of_scores = len(scores_list)
    average = total_score / number_of_scores
    
    return average


def get_grade(average):
    # Use if-elif chain to classify performance
    if average >= 90:
        grade = "A"
        remark = "Excellent"
    elif average >= 80:
        grade = "B"
        remark = "Very Good"
    elif average >= 70:
        grade = "C"
        remark = "Good"
    elif average >= 60:
        grade = "D"
        remark = "Satisfactory"
    elif average >= 50:
        grade = "E"
        remark = "Pass"
    else:
        grade = "F"
        remark = "Fail"
    
    return grade, remark


def rank_students(student_data):
    # Step 1: Create records with calculated averages and grades
    student_records = []
    
    for student_name, scores in student_data:
        average_score = calculate_average(scores)
        grade_letter, grade_remark = get_grade(average_score)
        
        # Store: (name, average, grade, remark)
        student_records.append((student_name, average_score, grade_letter, grade_remark))
    
    # Step 2: Sort using nested loops (Bubble Sort)
    # This compares adjacent students and swaps if needed
    number_of_students = len(student_records)
    
    for outer_loop in range(number_of_students):
        # Inner loop compares adjacent pairs
        for inner_loop in range(0, number_of_students - outer_loop - 1):
            # Compare averages (index 1 of each record)
            if student_records[inner_loop][1] < student_records[inner_loop + 1][1]:
                # Swap if current student's average is less than next student's
                student_records[inner_loop], student_records[inner_loop + 1] = \
                    student_records[inner_loop + 1], student_records[inner_loop]
    
    # Step 3: Add rank position to each record
    ranked_list = []
    
    for position, (name, avg, grade, remark) in enumerate(student_records, start=1):
        ranked_list.append((position, name, avg, grade, remark))
    
    return ranked_list


def print_ranking_table(ranked_students):
    """
    Print a formatted ranking table with all student data.
    
    Args:
        ranked_students (list): List of ranked student tuples
                               (rank, name, average, grade, remark)
    """
    print("\n" + "=" * 85)
    print("STUDENT PERFORMANCE RANKING SYSTEM".center(85))
    print("=" * 85)
    
    # Print table header
    print(f"{'Rank':<6} {'Name':<20} {'Average':<12} {'Grade':<8} {'Remark':<20}")
    print("-" * 85)
    
    # Print each ranked student
    for rank_position, student_name, average_score, letter_grade, remark_text in ranked_students:
        print(f"{rank_position:<6} {student_name:<20} {average_score:>10.2f}    {letter_grade:<8} {remark_text:<20}")
    
    print("=" * 85 + "\n")


# Main program: Test with student data
if __name__ == "__main__":
    # Student data: (name, [exam1, exam2, exam3, exam4])
    students = [
        ("Alice Johnson", [92, 88, 95, 90]),
        ("Bob Smith", [78, 82, 75, 80]),
        ("Charlie Davis", [85, 91, 88, 86]),
        ("Diana Wilson", [95, 93, 97, 96]),
        ("Eve Martinez", [65, 70, 68, 72]),
        ("Frank Brown", [88, 85, 90, 87]),
        ("Grace Lee", [72, 78, 75, 76]),
        ("Henry Taylor", [91, 89, 92, 90]),
    ]
    
    # Calculate rankings
    ranked_students = rank_students(students)
    
    # Display the ranking table
    print_ranking_table(ranked_students)
    
    # Display detailed analysis for each student
    print("\nDETAILED STUDENT ANALYSIS:")
    print("-" * 85)
    
    for student_name, exam_scores in students:
        avg = calculate_average(exam_scores)
        grade, remark = get_grade(avg)
        scores_formatted = ", ".join(map(str, exam_scores))
        
        print(f"{student_name:20} | Scores: [{scores_formatted}] | "
              f"Avg: {avg:.2f} | Grade: {grade} ({remark})")
    
    print("-" * 85)
