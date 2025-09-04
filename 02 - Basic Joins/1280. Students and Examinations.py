import pandas as pd


def students_and_examinations(
    students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame
) -> pd.DataFrame:
    cross = students.merge(subjects, how="cross")
    attended_exams = examinations.groupby(["student_id", "subject_name"]).size().reset_index(name="attended_exams")
    result = cross.merge(attended_exams, how="left", on=["student_id", "subject_name"])
    result["attended_exams"] = result["attended_exams"].fillna(0)
    return result.sort_values(by=["student_id", "subject_name"])
