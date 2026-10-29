def is_valid(isbn):
    cleaned_isbn = isbn.replace('-', '')

    no_digits = 10
    total = 0

    if len(cleaned_isbn) == 10:
        for item in cleaned_isbn:
            if item == 'X'and no_digits == 1:
                digital_value = 10
            elif item.isdigit():
                digital_value = int(item)
            else:
                return False
            total += digital_value*(no_digits)
            no_digits -= 1
        if total % 11 == 0:
            return True
        return False
    return False

   
