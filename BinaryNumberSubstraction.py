def binary_subtraction(bin1, bin2):
    len1, len2 = len(bin1), len(bin2)
    max_len = max(len1, len2)

    bin1 = '0' * (max_len - len1) + bin1
    bin2 = '0' * (max_len - len2) + bin2

    result = ''
    borrow = 0

    for i in range(max_len - 1, -1, -1):
        digit1 = int(bin1[i])
        digit2 = int(bin2[i])

        if digit1 - borrow >= digit2:
            result = str(digit1 - digit2 - borrow) + result
            borrow = 0
        else:
            result = str(2 + digit1 - digit2 - borrow) + result
            borrow = 1

    return result.lstrip('0') or '0'
