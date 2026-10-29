def classify(number):
    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')
    e_sum = 0
    for factor in range(1, number):
        if number % factor == 0:
            e_sum += factor

    if e_sum == number:
        return 'perfect'
    if e_sum > number:
        return 'abundant'
    else:
        return 'deficient'
