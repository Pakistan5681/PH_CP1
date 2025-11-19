
def calc(equation, firstNum, *numbers, ):
    output = 0

    if equation =='+':
        for i in numbers:
            output += i
    elif equation =='-':
        output = firstNum
        
        for i in numbers:
            output -= i
    elif equation =='*':
        output = firstNum
        
        for i in numbers:
            output *= i
    elif equation =='/':
        output = firstNum
        
        for i in numbers:
            output /= i    
    elif equation =='//':
        output = firstNum
        numbers.remove(output)
        
        for i in numbers:
            output //= i 
    elif equation =='**':
        output = firstNum
        
        for i in numbers:
            output **= i   
    elif equation =='%':
        output = firstNum
        for i in numbers:
            output **= i 

    return output

print(calc("/", 1, 4, 5, 2, 4, 2, 4, 5, 4))
