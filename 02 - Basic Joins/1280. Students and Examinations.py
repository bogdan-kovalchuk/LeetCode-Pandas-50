import pandas as pd


def students_and_examinations(
    students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame
) -> pd.DataFrame:
    cross = pd.merge(students, subjects, how="cross")
    exam_table = (
        examinations.groupby("student_id")["subject_name"].value_counts().reset_index()
    )
    result_table = pd.merge(
        cross, exam_table, on=["student_id", "subject_name"], how="left"
    )
    result_table = result_table.rename(columns={"count": "attended_exams"})
    result_table["attended_exams"] = result_table["attended_exams"].fillna(0)
    return result_table.sort_values(by=["student_id", "subject_name"])
