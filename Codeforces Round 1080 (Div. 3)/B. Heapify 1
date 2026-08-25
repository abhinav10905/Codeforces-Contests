**QUESTION**
B. Heapify 1
You are given a permutation a of length n∗.
You can perform the following operation any number of times (possibly zero):
Select an index i (1≤i≤n2), and swap ai and a2i.
For example, when a=[1,4,2,3,5], you can swap a2 and a4 to make it [1,3,2,4,5], but you cannot swap a2 and a3.
Please determine if the sequence a can be sorted in increasing order.
∗A permutation of length n is an array consisting of n distinct integers from 1 to n in arbitrary order. For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array), and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

**INPUT**
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤104). The description of the test cases follows.
The first line of each test case contains a single integer n (1≤n≤2⋅105).
The second line of each test case contains n distinct integers a1,a2,…,an (1≤ai≤n).
It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.

**OUTPUT**
If a can be sorted in increasing order, output "YES" on a separate line. Otherwise, output "NO" on a separate line.
You can output the answer in any case. For example, the strings "yEs", "yes", and "Yes" will also be recognized as positive responses.

**CODE**
for t in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    p = True
    for i in range(1, n + 1, 2):
        indices = []
        values = []
        curr = i
        while curr <= n:
            indices.append(curr)
            values.append(a[curr])
            curr *= 2
        if sorted(indices) != sorted(values):
            p = False
            break
            
    if p:
        print("YES")
    else:
        print("NO")

**APPROACH**
Time :- O(t*nlogn)
Space :- O(n) per test case
Approach :- Array, Sorting
