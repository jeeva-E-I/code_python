s1 = "enag"
s2 ="gane"
def anagram(s1,s2):
    return sorted(s1) == sorted(s2)

print(anagram(s1,s2))

