percentage = input("GIVE ME YOUR GRADE NOW (make it percentage) ").strip().replace("%", "")
override = False

while not percentage.isdigit():
    if "." in percentage or "-" in percentage:
        placeholder = percentage.replace(".", "", 1).replace("-", "", 1)

        if placeholder.isdigit():
            override = True
            break

    print(" ")
    print("Broski thats invalid.")
    percentage = input("GIVE ME YOUR GRADE NOW (make it percentage) ").strip().replace("%", "")

percentage = round(float(percentage), 3)
grade = ""

if percentage >= 95:
    grade = "A"
elif percentage >= 90:
    grade = "A-"
elif percentage >= 85:
    grade = "B+"
elif percentage >= 80:
    grade = "B"
elif percentage >= 75:
    grade = "B-"
elif percentage >= 70:
    grade = "C+"
elif percentage >= 65:
    grade = "C"
elif percentage >= 60:
    grade = "C-"
else:
    grade = "F" 

print(f"You have a {percentage}%, which is a(n) {grade}")