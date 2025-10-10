"""
ask user for password input
sets a list of special characters
sets a list of missing inputs

    checks each character of the input for lowercase
        if char.islower()
            add one to password strength
            break
            
        adds "missing lowercase" to missing inputs        
    checks each character of the input for uppercase
        if char.isupper()
            add one to password strength
            break
            
        adds "missing uppercase" to missing inputs 
    checks each character of the input for special characters
        if char in special characters
            add one to password strength
            break
            
        adds "missing special character" to missing inputs 
    checks each character of the input for numbers
        if char.isnumeric()
            add one to password strength
            break
            
        adds "missing number" to missing inputs 
    checks to see if input is long enough
        if length of input >= 8
            add one to password strength
            break
        
        adds "not long enough" to missing inputs 


    if password strength is 0, password sucks       
    if password strength is 1-2, password is weak
    if password strength is 3, password is moderate
    if password strength is 4, password is strong
    if password strength is 4, password is very strong
"""

while True:
    password = input("Input your password")
    passwordStrength = 0
    specialCharacters = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=","[","]","{","}","|",";",":",",",".","<",">","?"]
    missingInputs = []

    for char in password: # lowercase check
        if char.islower():
            passwordStrength += 1
            break
            
        missingInputs.append("missing lowercase")       
    for char in password: # uppercase check
        if char.isupper():
            passwordStrength += 1
            break
            
        missingInputs.append("missing uppercase")    
    for char in password:
        if char in specialCharacters
            passwordStrength += 1
            break
            
        missingInputs.append("missing special characters") 
    checks each character of the input for numbers
        if char.isnumeric()
            add one to password strength
            break
            
        adds "missing number" to missing inputs 
    checks to see if input is long enough
        if length of input >= 8
            add one to password strength
            break
        
        adds "not long enough" to missing inputs 
            
    if password strength is 1-2, password is weak
    if password strength is 3, password is moderate
    if password strength is 4, password is strong
    if password strength is 4, password is very strong