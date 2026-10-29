def classify(number):
    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')
    e_sum = 0
    for i in range(1, number):
        if number % i == 0:
            e_sum += i

    if e_sum == number:
        return 'perfect'
    elif e_sum > number:
        return 'abundant'
    else:
        return 'deficient'
