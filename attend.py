classes_held = int(input("Classes Held: "))
classes_attended = int(input("Classes Attended: "))

attendance_percentage = (classes_attended / classes_held) * 100 if classes_held else 0
status = "Eligible for exams" if attendance_percentage >= 75 else "Not eligible for exams"

print(f"Classes Held: {classes_held}")
print(f"Classes Attended: {classes_attended}")
print(f"Attendance: {int(attendance_percentage) if attendance_percentage.is_integer() else round(attendance_percentage,2)}%")
print(f"Status: {status}")