def is_armstrong_number(number):
    
    #this is to convert the number to a string
    str_num = str(number)

    #to get the number of the digits for the power of each digit
    p = len(str_num)

    #to store the total sum of the digits
    total = 0

    #For loop to iterate through all the numbers inputed for the sum
    for i in str_num:
        total += int(i) ** p
        
    #conditional statement to check if the sum is an armstrong number
    if(total == number):
        return True
    else:
        return False
    
