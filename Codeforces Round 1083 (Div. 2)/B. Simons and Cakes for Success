**QUOTE**

When I succeed, we'll share the cakes together!
— SHUN

**QUESTION**
B. Simons and Cakes for Success
Simons has n friends and a huge amount of cakes. To divide the cakes fairly, you are asked to help him solve the following problem:
Find the minimum positive integer k such that n is a divisor of kn.
It can be proved that the answer always exists under the given constraints.

**INPUT**
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤100). The description of the test cases follows.
The only line of each test case contains a single integer n (2≤n≤109) — the number of friends Simons has.

**OUTPUT**
For each test case, output a single integer — the minimum k you found.

**CODE**
for t in range (int(input())):
    n=int(input())
    c=2
    a=1
    while c*c<=n:
        if n%c==0:
            a*=c
            n//=c
            while n%c==0:
                n//=c
        c+=1
    if n>1:
        a*=n
    print(a)

**APPROACH**
Time :- O(t(√n))
Space :- O(1) per test case
Approach :- Math
