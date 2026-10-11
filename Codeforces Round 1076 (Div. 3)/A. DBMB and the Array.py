**QUESTION**
A. DBMB and the Array
DBMB had a birthday yesterday. He was gifted an array a of n elements and a number x. But there is one problem: he only likes arrays where the sum of the elements equals s. To make the array appealing to him, you can perform the following operation any number of times:
Choose an index i (1≤i≤n) and add x to the number ai.
For example, if he was given the array [1,2,3,5] and x=2, you can choose index 3 and get the array [1,2,5,5]. Your task is to determine whether the array can appeal to DBMB after any number of operations.

**INPUT**
Each test consists of several test cases. The first line contains a single integer t (1≤t≤1000) — the number of test cases. The following describes the test cases.
The first line of each test case contains three integers n, s, x (1≤n,x≤10, 1≤s≤100).
The second line of each test case contains n integers a1,a2,…an (1≤ai≤10) — the elements of the array gifted to DBMB.

**OUTPUT**
For each test case, output "YES" if the array can appeal to DBMB. Otherwise, output "NO".
You can output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.

**CODE**
for t in range (int(input())):
    n,s,x=map(int,input().split())
    arr=list(map(int,input().split()))
 
    if sum(arr)==s:
        print("YES")
    elif sum(arr)>s:
        print("NO")
    elif (s-sum(arr))%x==0:
        print("YES")
    else:
        print("NO")

**APPROACH**
Time :- O(t*n)
Space :- O(n) per test case
Approach :- Array, Sum
