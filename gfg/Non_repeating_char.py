def nonRepeatingChar(s):
    char_count = {}
    for i in s:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    for i in s:
        if char_count[i] == 1:
            return i
    return '$'

print(nonRepeatingChar("aabbccddee"))