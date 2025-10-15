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
 
 
password = input("Input your password ").replace(" ", "") 
passwordStrength = 0 
specialCharacters = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=","[","]","{","}","|",";",":",",",".","<",">","?"] 
missingInputs = [] 
 
if any(i.islower() for i in password):
    passwordStrength += 1
else:
    missingInputs.append("missing lowercase")  
           
if any(i.isupper() for i in password):
    passwordStrength += 1
else:
    missingInputs.append("missing uppercase")

if any(i in specialCharacters for i in password):
    passwordStrength += 1
else:
    missingInputs.append("missing special characters (!,@,#,$,%,^,&,*,(,),_,+,-,=,[,],{,},|,;,:,,,.,<,>,?)") 
 
if any(i.isnumeric() for i in password):
    passwordStrength += 1
else:
    missingInputs.append("missing number") 
          
if len(password) >= 8: 
    passwordStrength += 1 
else: 
    missingInputs.append("not long enough (should be eight characters or more)")  
 
for i in missingInputs: 
    print(f"password is {i}") 
         
if passwordStrength == 2: 
    print("Password is weak") 
elif passwordStrength == 3: 
    print("Password is moderate") 
elif passwordStrength == 4: 
    print("Password is strong") 
elif passwordStrength == 5: 
    print("Password is very strong") 
else: 
    print("How did you make such a terrible password? The password 'eE' would've been better than this") 