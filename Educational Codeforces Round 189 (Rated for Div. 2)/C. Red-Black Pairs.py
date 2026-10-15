**QUESTION**
C. Red-Black Pairs
There is a table of 2×n cells. Each cell of the table is colored either red or black. You want to repaint some cells of this table so that there exists at least one way to partition all cells into n pairs such that the following conditions hold:
the cells in each pair have the same color;
the cells in each pair share a side.
What is the minimum number of cells that need to be repainted?

**INPUT**
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤104). The description of the test cases follows.
The first line of each test case contains one integer n (1≤n≤2⋅105).
The second and third lines of each test case describe the colors of the cells. Each line contains a string consisting of exactly n letters "R" and/or "B".
Additional constraint on the input:
the sum of n over all test cases does not exceed 2⋅105.

**OUTPUT**
For each test case, output one integer — the minimum number of cells that need to be repainted.

**CODE**
for t in range (int(input())):
    n=int(input())
    a=input()
    b=input()
    c=0
    i=0
    while i<n-1:
        if a[i]==b[i]:
            i+=1
        elif a[i]==a[i+1]:
            if b[i]!=b[i+1]:
                c+=1
            i+=2
        elif b[i]==b[i+1]:
            if a[i]!=a[i+1]:
                c+=1
            i+=2
        else:
            c+=1
            i+=1
    if i==n-1 and a[-1]!=b[-1]:
        c+=1
    print(c)

**APPROACH**
Time :- O(t*n)
Space :- O(1) per test case
Approach :- Brute Force, Array
