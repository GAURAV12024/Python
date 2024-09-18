map={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
map2={"0":10,"1":11,"2":12,"3":13,"4":14,"5":15,"6":16,"7":17,"8":18,"9":19}

def text_to_int(string):
    if string == "":
        return 0
    elif len(string) == 1:
        return map[string]
    else:
        i = len(string) - 1
        number = 0
        j = 0
        while i >= 0:
            number = number + (map[string[i]] * pow(10, j))
            j += 1
            i -= 1
        return number

def decimal_subtraction(str1, str2):
    ans = 0
    p = 0
    i = len(str1) - 1
    j = len(str2) - 1
    carry = 0
    
    while i >= 0 or j >= 0:

        a = text_to_int(str1[i]) if i >= 0 else 0
        b = text_to_int(str2[j]) if j >= 0 else 0

        if a >= b + carry:
            ans = ans + (a - (b + carry)) * pow(10, p)
            carry = 0
        else:
            ans = ans + (map2[str(a)] - (b + carry)) * pow(10, p)
            carry = 1
        
        p += 1
        i -= 1
        j -= 1
    
    return str(ans)

print(decimal_subtraction("121", "120"))  
print(decimal_subtraction("139", "120"))
print(text_to_int("1245"))               
