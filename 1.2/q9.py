marks = [80, 75, 90, 65, 70]

total = 0

for mark in marks:
    total += mark

percentage = total / (len(marks) * 100) * 100

if percentage >= 35:
    result = "PASS"
else:
    result = "FAIL"

print("Total:", total)
print("Percentage:", percentage)
print("Result:", result)
