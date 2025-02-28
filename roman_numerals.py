def roman_numeral(num):
    if num < 1 or num > 3999:
        return "Input must be between 1 and 3999." # Do not forget these types of conditional statements.
    result = ""
    values = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    for value, numeral in values:
        while num >= value:
            result = result + numeral
            # result += numeral
            num = num - value  
            # num += value       
    return result

#print(roman_numeral(12))
