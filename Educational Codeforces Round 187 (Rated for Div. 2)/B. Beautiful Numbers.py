**QUESTION**
B. Beautiful Numbers
Let's define F(x) as the sum of the digits of x. An integer x is considered beautiful if F(F(x))=F(x).
You are given an integer x. In one move, you can choose any digit in the number and replace it with another. The resulting number cannot have leading zeros.
Your task is to calculate the minimum number of moves (possibly zero) required to make the given number beautiful.

**INPUT**
The first line contains a single integer t (1≤t≤104) — the number of test cases.
The only line of each test case contains a single integer x (1≤x≤1018).

**OUTPUT**
For each test case, print a single integer — the minimum number of moves (possibly zero) required to make the given number beautiful.

**CODE**
for t in range (int(input())):
    x=list(input())
    a=0
    c=0
    for i in x:
        a+=int(i)
    x[0]=str(int(x[0])-1)
    while a>9:
        a-=int(max(x))
        c+=1
        x.remove(max(x))
    print(c)

**APPROACH**
Time :- O(t(n**2))
Space :- O(n) per test case
Approach :- Math, DP
