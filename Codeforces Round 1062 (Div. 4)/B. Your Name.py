**QUESTION**
B. Your Name
khba is writing his girlfriend's name. He has n cubes, each with one lowercase Latin letter written on it. They are arranged in a row, forming a string s. His girlfriend's name is also a string t, consisting of n lowercase Latin letters.
To prove his love, he must check whether it is possible to rearrange the letters of string s so that it becomes her name t.

**INPUT**
The first line contains an integer q (1≤q≤1000) — the number of test cases.
The first line of each test case contains an integer n (1≤n≤20).
The second line of each test case contains two distinct strings s and t, each consisting of n lowercase Latin letters.

**OUTPUT**
For each test case, output "YES" if the letters of s can be arranged to form t; otherwise, output "NO".
You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as positive responses.

**CODE**
q=int(input())
for i in range (0,q):
    n=int(input())
    s,t=map(str,input().split())
    if sorted(s)==sorted(t):
        print("YES")
    else:
        print("NO")

**APPROACH**
Time Complexity :- O(t*n)
Space Complexity :- O(n)
Approach :- Sorting
