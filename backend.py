from datetime import date

def calculate_attendance(
    weekly_schedule: dict,
    semester_start: date,
    semester_end: date,
    attendance_till: date,
    current_percentage: float,
    required_percentage: float
):
    # Total classes in one week
    classes_per_week = sum(weekly_schedule.values())

    # Total classes in the full semester
    total_days = (semester_end - semester_start).days + 1
    total_weeks = total_days // 7
    total_semester_classes = total_weeks * classes_per_week

    # Classes completed till the given date
    days_completed = (attendance_till - semester_start).days + 1
    weeks_completed = max(days_completed // 7, 0)
    classes_so_far = weeks_completed * classes_per_week

    # How many classes the student has attended till now
    attended_classes = round(
        classes_so_far * current_percentage / 100
    )

    # Remaining classes in the semester
    remaining_classes = max(
        total_semester_classes - classes_so_far, 0
    )

    # Total attendance required to reach minimum percentage
    required_total_attendance = round(
        required_percentage / 100 * total_semester_classes
    )

    # Classes the student must attend from now
    must_attend = max(
        required_total_attendance - attended_classes, 0
    )

    # Classes the student can safely bunk
    can_bunk = max(
        remaining_classes - must_attend, 0
    )

    # Simple status for UI
    status = "SAFE" if must_attend == 0 else "WARNING"

    # Send everything back to Streamlit
    return {
        "total_semester_classes": total_semester_classes,
        "classes_so_far": classes_so_far,
        "attended_classes": attended_classes,
        "remaining_classes": remaining_classes,
        "must_attend": must_attend,
        "can_bunk": can_bunk,
        "status": status
    }
