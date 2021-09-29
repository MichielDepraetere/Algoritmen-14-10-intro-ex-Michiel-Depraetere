number1 = 2
number2 = 1
outcome = 0
total = 0

while(outcome < 4000000):
    

    outcome = number1 + number2
    if(number1 == 2):
        if(number1 % 2 == 0):
            total += number1
        number1 = outcome
    
    else:
        if(number1 < number2):
            if(number1 % 2 == 0):
                total += number1
            number1 = outcome
        
        else:
            if(number2 % 2 == 0):
                total += number2
            number2 = outcome

print("The sum of al odd numbers int the row of Lucas smaller than 4 000 000 = " + str(total))
