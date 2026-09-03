**QUESTION**
B. Nikita and Books
As is well known, Nikita loves reading. Today, he made a mess in his room and arranged his books into n stacks in a row, numbered from 1 to n from left to right. The i-th stack contains ai books. This arrangement is called neat if, in every stack except the rightmost one, the number of books is strictly less than in the stack to its right; that is, the array a is strictly increasing.
Yura wants to make the arrangement neat by performing the following operation any number of times:
Choose a stack i such that 1≤i<n and ai>1.
Take 1 book from the top of stack i, so ai decreases by 1.
Put this book on top of stack i+1, so ai+1 increases by 1.
Determine whether Yura can make the arrangement neat.

**INPUT**
The first line contains a single integer t (1≤t≤104) — the number of test cases.
The first line of each test case contains a single integer n (1≤n≤2⋅105) — the number of stacks.
The second line of each test case contains n integers ai (1≤ai≤109) — the initial number of books in each stack.
It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.

**OUTPUT**
For each test case, output "YES" if Yura can make the arrangement neat, and "NO" otherwise.
You may output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted.

**CODE**
for t in range (int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m="true"
    c=0
    i=0
    while i<n:
        c+=a[i]
        if c<(i+1)*(i+2)//2:
            m="false"
            break
        i+=1
    if m=="false":
        print("NO")
    else:
        print("YES")

**APPROACH**
Time :- O(t*n)
Space :- O(1) per test case
Approach :- Array, Math, Boolean
