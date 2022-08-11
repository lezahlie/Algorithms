"""
Leslie Horace
kthElement.py: Uses Divide and Conquer to find the kth element in a combined sorted array
Input: A = [1, 2, 2, 3, 5, 6, 6], B = [3, 3, 4, 5, 6, 7, 8], k = 5 (k must be in range 1 to |A+B|)
Output: 3, value of k in C, where C=A+B sorted
"""


def find_k(A, B, m, n, k):
    if m == 0:  # A is empty, k is in B
        return B[k-1]
    elif n == 0:  # B is empty, k is in A
        return A[k-1]
    elif k == 1:  # base case: k=1 or recurse until k=1
        return min(A[k - 1], B[k - 1])
    else:
        x = min(m, k//2)  # x divides A, unless m < k//2
        y = min(n, k//2)  # y divides B, unless n < k//2
        if A[x-1] < B[y-1]:  # x = lower bound for k, reduce A by x elements
            return kth_element(A[x:m], B, (k-x))
        else:  # y=lower bound for k, reduce B by y elements
            return kth_element(A, B[y:n], (k-y))


def kth_element(A, B, k):
    m, n = len(A), len(B)
    if 0 < k < (m+n)+1:
        return find_k(A, B, m, n, k)
    return None  # here if k is out of bounds
