**QUESTION**
B. Impost or Sus
A string w consisting of lowercase Latin letters is called suspicious if and only if all of the following conditions hold:
The letter s appears at least twice, and
For every occurrence of the letter u, the two nearest occurrences of s are the same number of characters away from the u.
After watching you finish a string task, your friend Aka has gifted you a string r consisting only of letters s and u. You can perform the following operation on r:
Choose an index i (1≤i≤|r|), and set ri to s.
Determine the minimum number of operations needed to make r suspicious. It can be shown that, under the given constraints, it is always possible to transform r into a suspicious string.

**INPUT**
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤104). The description of the test cases follows.
The only line of each test case contains the string r (3≤|r|≤2⋅105). It is guaranteed that ri=s or u.
It is guaranteed that the sum of |r| over all test cases does not exceed 2⋅105.

**OUTPUT**
For each test case, output a single integer — the minimum number of operations needed to make r suspicious.

**CODE**
t=int(input())
for i in range (0,t):
    s=input()
    r=list(s)
    count=0
    for j in range (0,len(r)):
        if r[j]=='u':
            for k in range (0,len(r)):
                if (j-k)>=0 and (j+k)<len(r):
                    if r[j-k]=='s' and r[j+k]=='u':
                        r[j+k]='s'
                        count+=1
                        break
                    elif r[j+k]=='s' and r[j-k]=='u':
                        r[j-k]='s'
                        count+=1
                        break
                    elif r[j-k]=='s' and r[j+k]=='s':
                        break
                    else:
                        pass
                    
                else:
                    r[j]='s'
                    count+=1
                    break
    print(count)

**APPROACH**
Time :- O(t(n**2))
Space :- O(n) per test case
Approach :- Counting
