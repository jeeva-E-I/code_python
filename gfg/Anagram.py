s1 = "allergy"
s2 ="allergic"
def anagram(s1,s2):
    flag ='false'
    new_s1 = s1.lower()
    new_s2 = s2.lower()
    if len(new_s1) == len(new_s2):
        for i in new_s1:
            if i in new_s2:
                flag = 'true'
            else:
                return 'false'
        return flag
    else:
        return flag

print(anagram(s1,s2))

