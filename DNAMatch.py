"""
Leslie Horace
DNAMatch.py: Uses Dynamic programming to finds the length of the longest DNA Sequence
            dna_match_bottomup(): Uses a matrix for tabulation
            dna_match_topdown(): Uses a matrix for recursive memoization
For bottom up and top down functions:
Input: A = "ATAGTTCCGTCAAA", B = "GTGTTCCCGTCAAA"
Output: Length(A,B) = 12 (TGTTCCGTCAAA)
"""


def dna_match_iterative(A, B, m, n, C):
    if m == 0 or n == 0:    # Base Case, DNA lcs length is 0
        return 0
    for x in range(1, m+1):     # loop each row in C[x][y]
        for y in range(1, n+1):     # loop each col in C[x][y]
            if A[x-1] == B[y-1]:     # match found, store DNA lcs length + 1
                C[x][y] = C[x-1][y-1] + 1
            else:   # no match, dec. to last max value in C[x][y]
                C[x][y] = max(C[x-1][y], C[x][y-1])
    return C[x][y]   # return final DNA lcs length


def dna_match_bottomup(DNA1, DNA2):
    # initialize matrix to hold count values for DNA lcs length
    matrix = [[0 for y in range(len(DNA2)+1)] for x in range(len(DNA1)+1)]
    return dna_match_iterative(DNA1, DNA2, len(DNA1), len(DNA2), matrix)


def dna_match_recursive(A, B, m, n, C):
    if m == 0 or n == 0:    # Base Case, DNA lcs length is 0
        return 0
    if C[m-1][n-1] != 1:    # if current C[x][y] is > 1
        if A[m-1] == B[n-1]:  # match found, store DNA lcs length + 1
            C[m-1][n-1] = dna_match_recursive(A, B, m-1, n-1, C) + 1
        else:  # no match, recurse to last max value in C[x][y]
            C[m-1][n-1] = max(dna_match_recursive(A, B, m-1, n, C), dna_match_recursive(A, B, m, n-1, C))
    return C[m-1][n-1]   # return final DNA lcs length


def dna_match_topdown(DNA1, DNA2):
    # initialize matrix to hold count values for DNA lcs length
    matrix = [[0 for y in range(len(DNA2)+1)] for x in range(len(DNA1)+1)]
    return dna_match_recursive(DNA1, DNA2, len(DNA1), len(DNA2), matrix)
