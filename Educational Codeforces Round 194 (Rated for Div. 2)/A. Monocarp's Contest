**QUESTION**
A. Monocarp's Contest
Monocarp is preparing a team programming contest. The contest has n problems, each of which is either easy or hard. The problems are numbered from 1 to n.
Monocarp wants the first and the last problems of the contest to be easy. In one operation, he can choose any two problems and swap them.
Determine the minimum number of operations required to make the first and the last problems easy, or report that it is impossible.

**INPUT**
The first line contains an integer t (1≤t≤103) — the number of test cases.
Each test case consists of two lines
the first line contains one integer n (2≤n≤50) — the number of problems in the contest;
the second line contains n integers a1,a2,…,an (0≤ai≤1). If ai=0, then the problem with number i is easy; if ai=1, then it is hard.

**OUTPUT**
For each test case, print the minimum number of operations required to make the first and the last problems easy. If it is impossible to satisfy the requirement, print −1.

**CODE**
for t in range (int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in l:
        if i==0:
            c+=1
    if c<2:
        print("-1")
    elif l[0]==0 and l[-1]==0:
        print("0")
    elif l[0]==0:
        print("1")
    elif l[-1]==0:
        print("1")
    else:
        print("2")

**APPROACH**
Time :- O(t*n)
Space :- O(n) per test case
Approach :- Counting, Array
