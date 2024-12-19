"""Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s.
    If there is no non-repeating character, return '$'."""

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