marks = {
    "Arun": 90,
    "Bala": 85,
    "Kavin": 78,
    "Divya": 92,
    "Riya": 88
}
name = input("Enter student name: ")
if name in marks:
    print("Marks of", name, "=", marks[name])
else:
    print("Student not found.")
