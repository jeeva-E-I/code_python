#ATOI CONVERSION
""" 1. Skip any leading whitespaces.
    2. Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
    3. Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached.
       If no digits are present, return 0.
    4.If the integer is greater than 231 – 1, then return 231 – 1 and 
     if the integer is smaller than -231, then return -231."""

def myatio():
    txt = "123"
    txt = txt.lstrip()
    sign = 1
    result = 0
    index = 0
    if txt[index] == '-':
        sign = -1
        index += 1
    elif txt[index]=='+':
        sign = +1
        index += 1
    
    for i in range(index,len(txt)):
        if txt[i].isdigit():
            result = result * 10 + (int(txt[i]))        
            if result * sign > (2**31 - 1)/10:
                return (2**31 -1)
            elif result * sign < (-2**31)/10:
                return -2**31
        else:
            return result*sign
    return result*sign



print(myatio())

#Sample inputs:
# Input: s = "-999999999999"
# Input: s = " 1231231231311133"
# Input: s = "  -0012gfg4"
# Input: s = "  -"