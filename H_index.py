# H-INDEX PROGRAM

"""
 H-Index is the largest value such that the researcher has at least H papers
that have been cited at least H times.
    1.Sort the array in descending order.
    2.Compare each citation with its rank.
"""

citations = [3, 0, 5, 3, 0]
H_index = 1
for i in range(len(citations)):
    if citations[i] >= H_index:
        H_index += 1
print(H_index -1)
