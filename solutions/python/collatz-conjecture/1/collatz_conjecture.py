def steps(number):
    # Error handling must happen BEFORE the loop
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    step_count = 0
    
    while number > 1:
        if number % 2 == 0:
            number = number // 2  # Update number for even
        else:
            number = 3 * number + 1  # Update number for odd
        
        step_count += 1 # Count this step
        
    return step_count