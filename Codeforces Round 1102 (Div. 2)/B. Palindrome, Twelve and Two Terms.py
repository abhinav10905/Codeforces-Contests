**QUESTION**
B. Palindrome, Twelve and Two Terms
You are given a positive integer n. A pair of non-negative integers a,b is called beautiful if the following conditions hold:
a+b=n.
The number a is a palindrome.∗
The number b is divisible by 12.
You need to find a beautiful pair or report that it does not exist.
∗A number is called a palindrome if and only if it remains the same when its digits (in decimal notation) are written in reverse order. For example, the numbers 12321, 6776, 5, 0 are palindromes, while the numbers 123 and 69 — are not.

**INPUT**
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤104). The description of the test cases follows.
The only line of each test case contains a single integer n (1≤n≤1018).

**OUTPUT**
For each test case, if such a and b exist, output a and b on a separate line, separated by a space. Otherwise, output −1 on a separate line.
If there are several beautiful pairs a,b, you may output any of them.

**CODE**
for t in range (int(input())):
    n=int(input())
    if n==10:
        print("-1")
    elif n%12==10:
        print(22,n-22)
    else:
        print(n%12,n-n%12)

**APPROACH**
Time :- O(t)
Space :- O(1) per test case
Approach :- Math
