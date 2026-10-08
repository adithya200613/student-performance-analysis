import numpy as np
import pandas as pd


SUBJECTS = [
    "Python",
    "Data_Structures",
    "Database",
    "Computer_Networks",
    "Operating_Systems",
]


def calculate_student_metrics(df):
    """Calculate total, average, grade and pass/fail for each student."""
    df = df.copy()

    # NumPy is used for efficient numerical calculations.
    marks = df[SUBJECTS].to_numpy(dtype=float)
    df["Total_Marks"] = np.sum(marks, axis=1)
    df["Average_Marks"] = np.mean(marks, axis=1)

    def assign_grade(avg):
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    df["Grade"] = [assign_grade(avg) for avg in df["Average_Marks"]]

    # Pass condition:
    # 1. At least 40 marks in every subject
    # 2. Average marks >= 50
    # 3. Attendance >= 75%
    df["Pass_Fail"] = np.where(
        (df[SUBJECTS].min(axis=1) >= 40)
        & (df["Average_Marks"] >= 50)
        & (df["Attendance"] >= 75),
        "Pass",
        "Fail",
    )
    return df


def subject_analysis(df):
    """Return subject-wise average, highest and lowest marks."""
    analysis = []
    for subject in SUBJECTS:
        values = df[subject].to_numpy(dtype=float)
        analysis.append({
            "Subject": subject,
            "Average": np.mean(values),
            "Highest": np.max(values),
            "Lowest": np.min(values),
        })
    return pd.DataFrame(analysis)


def get_top_students(df, n=3):
    """Return the top n students by average marks."""
    return df.sort_values("Average_Marks", ascending=False).head(n)


def get_class_statistics(df):
    """Return overall class statistics."""
    return {
        "class_average": np.mean(df["Average_Marks"].to_numpy()),
        "highest_average": np.max(df["Average_Marks"].to_numpy()),
        "lowest_average": np.min(df["Average_Marks"].to_numpy()),
        "pass_count": int((df["Pass_Fail"] == "Pass").sum()),
        "fail_count": int((df["Pass_Fail"] == "Fail").sum()),
        "attendance_average": np.mean(df["Attendance"].to_numpy()),
    }


def department_analysis(df):
    """Calculate average performance department-wise."""
    return (
        df.groupby("Department")["Average_Marks"]
        .agg(["mean", "max", "min", "count"])
        .round(2)
        .sort_values("mean", ascending=False)
    )
