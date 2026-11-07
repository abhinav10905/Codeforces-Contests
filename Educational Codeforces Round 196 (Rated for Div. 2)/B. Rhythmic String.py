**QUESTION**
B. Rhythmic String
We call a binary string s of length m periodic if there exists an integer  (1≤k<m) such that si=si+k for every i from 1 to m−k inclusive. The characters of the string are numbered starting from 1. The smallest such k is called the period of the string.
We call a string s rhythmic if it is periodic and among the first p characters of the string (where p is the period of the string), there is exactly one 1.
For example, the string 0010010 is periodic with period p=3 and rhythmic: among the first three characters there is exactly one 1. The string 0110110 is also periodic with period p=3, but it is not rhythmic: among the first three characters there are two 1s.
You are given an array a of n integers and a string s, initially consisting of 1018 zeros. For each element ai, all characters of the string whose indices are divisible by ai are replaced by ones. In other words, the characters at positions ai,2ai,3ai,…, not exceeding the length of the string, become ones. Replacing a character with one again does nothing.
For example, if a=[3,7,5,3], then the string s will begin with 001011101101011...
Before performing these changes, you may remove any elements from array a. Find the minimum number of elements that need to be removed so that the resulting string s is rhythmic.

**INPUT**
The first line contains an integer t (1≤t≤5000) — the number of test cases.
The following descriptions of the test cases follow.
The first line of each test case contains an integer n (1≤n≤5000) — the length of array a.
The second line of each test case contains n integers a1,a2,…,an (1≤ai≤109) — the elements of the array.
Additional constraints on the input:the sum of n over all test cases does not exceed 5000.

**OUTPUT**
For each test case, output one integer — the minimum number of elements that need to be removed from the array so that string s is rhythmic.
