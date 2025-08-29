#2nd PH Average Grade

print("Type each grade from 0-100")
gradeA = float(input("What is your grade in Scondary Math III Honors: "))
gradeB = float(input("What is your grade in AP History: "))
gradeC = float(input("What is your grade in Game Design III: ")) # sigh. (Apparently game design doesnt count as a programming class)
gradeD = float(input("What is your grade in Drawing II: "))
gradeE = float(input("What is your grade in AP Chem: "))
gradeF = float(input("What is your grade in Lunch: "))
gradeG = float(input("What is your grade in Interpersonal Relationships: "))

grade = gradeA + gradeB + gradeC + gradeD + gradeE + gradeF + gradeG
grade = grade / 7
grade = round(grade, 2)

print(" ")
print("Your grade average is " + str(grade) + "%")