**QUESTION**
A. Friendly Numbers
For an integer x, we call another integer y friendly if the following condition holds:
y−d(y)=x, where d(y) is the sum of the digits of y.
For a given integer x, determine how many friendly numbers it has.

**INPUT**
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤500). The description of the test cases follows.
Each test case consists of a single line containing one integer x (1≤x≤109).

**OUTPUT**
For each test case, output one integer — the answer to the problem.

**CODE**
for t in range (int(input())):
    x=int(input())
    if x%9==0:
        c=0
        for i in range (x,x+100):
            z=str(i)
            y=0
            for j in z:
                y+=int(j)
            if i-y==x:
                c+=1
        print(c)
    else:
        print("0")

**APPROACH**
Time :- O(t)
Space :- O(1) per test case
Approach :- Math
