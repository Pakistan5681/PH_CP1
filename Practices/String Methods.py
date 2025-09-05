name = input("Whats your name: ").strip().lower().title()

while not name.isalpha():
    print("That name is invalid")
    name = input("Whats your name: ").strip().lower().title()

phoneNumber = input("Whats your phone number: ").strip().replace(" ", "").replace("-","")


while len(phoneNumber) != 10 or not phoneNumber.isdigit():
    print("Thats not a phone number")
    phoneNumber = input("Whats your phone number: ").strip().replace(" ", "").replace("-","")

phoneList = list(phoneNumber)
phoneList.insert(3, " ")
phoneList.insert(7, " ")

phoneNumber = "".join(phoneList)

gpa = input("Whats your GPA?").strip().replace(" ", "")

if gpa.isnumeric():
    gpa = float(gpa)

while not gpa.isnumeric() and not gpa.isdecimal() or gpa > 4 or gpa < 0:
    print("This GPA is invalid")
    gpa = input("Whats your GPA?").strip().replace(" ", "")

    if gpa.isnumeric():
        gpa = float(gpa)

round(gpa, 2)

print(name)
print(phoneNumber)
print(gpa)