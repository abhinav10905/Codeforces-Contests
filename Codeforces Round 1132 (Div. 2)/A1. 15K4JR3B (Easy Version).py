**QUESTION**
A1. 15K4JR3B (Easy Version)
Unemployed ∗ Angel places three points A, B, and C at the origin.
You must perform exactly n operations of the following type: choose one of these points and increase or decrease one of its coordinates by 1. In other words, if the chosen point has coordinates (x,y), in one operation you may move it to (x+1,y), (x−1,y), (x,y+1), or (x,y−1).
Unemployed ∗ Angel asks you to find the maximum doubled area of triangle ABC after all operations are performed. As she is your idol, you cannot refuse her.
Since Unemployed ∗ Angel is very smart, she can show that the value of interest is always an integer.

**INPUT**
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤1000). The description of the test cases follows.
The only line of each test case contains one integer n (2≤n≤1000) — the number of operations.

**OUTPUT**
For each test case, output one integer — the maximum doubled area of triangle ABC.

**CODE**
for t in range (int(input())):
    n=int(input())
    i=0
    a=0
    b=0
    while i<n:
        if i%2==0:
            a+=1
        else:
            b+=1
        i+=1
    print(a*b)
