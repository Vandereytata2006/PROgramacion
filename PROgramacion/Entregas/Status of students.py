exam_score = float(input('Enter the exam score (out of 100): '))
total_classes = int(input('Enter the total number of classes: '))
attended_classes = int(input('Enter the number of classes attended: '))

attendance_percentage = (attended_classes / total_classes) * 100

if exam_score >= 70 and attendance_percentage >= 80:
    result = "Pass"
else:
    result = "Fail"

print(f"The student has an exam score of {exam_score} and attended {attendance_percentage}% of the classes.")
print(f"Result: {result}")
