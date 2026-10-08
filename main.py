import pandas as pd
from functions import (
    calculate_student_metrics,
    subject_analysis,
    get_top_students,
    get_class_statistics,
    department_analysis,
)


def main():
    print("=" * 75)
    print("             STUDENT PERFORMANCE ANALYSIS SYSTEM")
    print("=" * 75)

    # Step 2: Read CSV using Pandas
    df = pd.read_csv(r"C:\Users\Smile\OneDrive\Desktop\cousrses\PYTHON WITH AI PROJECT\student_performance_project\students.csv")

    print("\n1. DATASET INFORMATION")
    print("-" * 75)
    print(f"Number of records : {len(df)}")
    print(f"Number of columns : {len(df.columns)}")
    print(f"Columns           : {', '.join(df.columns)}")

    print("\nFirst 5 Records:")
    print(df.head().to_string(index=False))

    print("\nBasic Information:")
    print(df.info())

    # Step 3: Process data
    df = calculate_student_metrics(df)

    print("\n2. STUDENT PERFORMANCE")
    print("-" * 75)
    display_columns = [
        "Student_ID", "Name", "Department",
        "Total_Marks", "Average_Marks", "Grade",
        "Attendance", "Pass_Fail"
    ]
    print(df[display_columns].to_string(index=False, formatters={
        "Average_Marks": "{:.2f}".format
    }))

    # Step 4: Analysis
    stats = get_class_statistics(df)

    highest_student = df.loc[df["Average_Marks"].idxmax()]
    lowest_student = df.loc[df["Average_Marks"].idxmin()]

    print("\n3. OVERALL CLASS ANALYSIS")
    print("-" * 75)
    print(f"Class average marks     : {stats['class_average']:.2f}")
    print(f"Highest student average : {stats['highest_average']:.2f}")
    print(f"Lowest student average  : {stats['lowest_average']:.2f}")
    print(f"Average attendance      : {stats['attendance_average']:.2f}%")
    print(f"Students passed         : {stats['pass_count']}")
    print(f"Students failed         : {stats['fail_count']}")

    print("\nHighest Performing Student:")
    print(f"  {highest_student['Name']} ({highest_student['Student_ID']}) - "
          f"{highest_student['Average_Marks']:.2f}%")

    print("\nLowest Performing Student:")
    print(f"  {lowest_student['Name']} ({lowest_student['Student_ID']}) - "
          f"{lowest_student['Average_Marks']:.2f}%")

    print("\n4. SUBJECT-WISE ANALYSIS")
    print("-" * 75)
    sub = subject_analysis(df)
    print(sub.to_string(index=False, formatters={
        "Average": "{:.2f}".format,
        "Highest": "{:.0f}".format,
        "Lowest": "{:.0f}".format,
    }))

    best_subject = sub.loc[sub["Average"].idxmax()]
    print(f"\nBest subject by class average: {best_subject['Subject']} "
          f"({best_subject['Average']:.2f}%)")

    print("\n5. TOP 3 STUDENTS")
    print("-" * 75)
    top = get_top_students(df, 3)
    for rank, (_, student) in enumerate(top.iterrows(), start=1):
        print(f"{rank}. {student['Name']} - "
              f"{student['Average_Marks']:.2f}% - Grade {student['Grade']}")

    print("\n6. DEPARTMENT-WISE ANALYSIS")
    print("-" * 75)
    dept = department_analysis(df)
    print(dept.to_string(formatters={
        "mean": "{:.2f}".format,
        "max": "{:.2f}".format,
        "min": "{:.2f}".format,
    }))

    # Save processed output so the final results are available without
    # inspecting the source code.
    output_columns = display_columns
    df[output_columns].to_csv("student_analysis_output.csv", index=False)

    print("\n7. OUTPUT FILE")
    print("-" * 75)
    print("Processed results saved to: student_analysis_output.csv")
    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
