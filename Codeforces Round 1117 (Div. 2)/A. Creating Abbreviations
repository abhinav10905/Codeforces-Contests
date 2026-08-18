**QUESTION**
A. Creating Abbreviations
The Beaver was given a set of words S, which initially contained n words. Then he performed the following operation m times:
The Beaver forms a sequence of one or more words from the set S. The same word may appear in the sequence several times. An abbreviation∗ is formed from the resulting phrase.
Then the Beaver adds the resulting abbreviation to S and can now use it in subsequent operations as an ordinary word.
You are given the n initial words that were in the set S, and the set of abbreviations that the Beaver formed. Determine whether the Beaver made a mistake and whether all these abbreviations could have appeared as a result of the operation described above. Note that the abbreviations did not necessarily appear in the same order in which they are given to you.
∗The abbreviation of a sequence is the word produced by the first letters of the words in the sequence. For example, the sequence birch OAK birch redwood produces the abbreviation BOBR.


**INPUT**
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤500). The description of the test cases follows.
The first line of each test case contains two integers n and m — the number of ordinary words and the number of abbreviations, respectively (1≤n,m≤100).
Each of the next n lines contains one string wi — an ordinary word (1≤|wi|≤20).
Each of the next m lines contains one string ai — an abbreviation formed by Bobr (1≤|ai|≤20).
All ordinary words consist of lowercase English letters, and all abbreviations consist of uppercase English letters. In each test case, all strings w1,w2,…,wn,a1,a2,…,am are pairwise distinct.
The total length of all strings over all test cases does not exceed 50000.

**OUTPUT**
For each test case, print "YES" if there exists a suitable order in which the given abbreviations could have appeared, and "NO" otherwise.
You may print each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.

**CODE**
for t in range (int(input())):
    n,m=map(int,input().split())
    a=[]
    b=[]
    o="true"
    for i in range (n):
        z=input()
        a.append(z)
    for j in range (m):
        z=input()
        b.append(z)
    hash={}
    for i in b:
        for j in i:
            j=j.lower()
            if j not in hash:
                hash[j]=1
    for i in a:
        if i[0] not in hash:
            pass
        else:
            hash[i[0]]=10
    for i in hash:
        if hash[i]==1:
            o="false"
    if o=="true":
        print("YES")
    else:
        print("NO")
    
**APPROACH**
Time :- O(t(n+m))
Space :- O(1)
Approach :- Hash Map
