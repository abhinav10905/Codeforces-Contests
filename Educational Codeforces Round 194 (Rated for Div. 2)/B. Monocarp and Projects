**QUESTION**
B. Monocarp and Projects
Monocarp runs a company. Consider the work of his company over the next k months. In the first month, the company has x employees, not counting Monocarp himself, and y projects need to be completed. In each next month, both the number of employees and the number of projects increase by 1.
In other words, in month i (0≤i<k), the company has x+i employees and needs to complete y+i projects.
In each month, Monocarp distributes the projects among the employees. Each employee must receive the same number of projects, and each project can be assigned to at most one employee. Monocarp completes all unassigned projects himself. He always chooses a distribution that makes him complete as few projects as possible.
In particular, if in some month there are a employees and b projects, then Monocarp assigns exactly ⌊ba⌋ projects to each employee, and he completes bmoda projects himself.
Find the total number of projects that Monocarp will complete himself over the next k months.

**INPUT**
The first line contains an integer t — the number of test cases (1≤t≤104).
Each test case consists of one line containing three integers x, y, and k (1≤x≤y≤106; 1≤k≤1012).
Additional constraint on the input:
the sum of y over all test cases does not exceed 106.

**OUTPUT**
For each test case, output one integer — the total number of projects that Monocarp will complete himself over k months.

**CODE**
for t in range (int(input())):
    x,y,k=map(int,input().split())
    c=0
    i=0
    while i<k:
        if (y+i)//(x+i)==1:
            break
        else:
            c+=(y+i)%(x+i)
        i+=1
    c+=(y+i)%(x+i)*(k-i)
    print(c)

**APPROACH**
Time :- O(t*k)
Space :- O(1) per test case
Approach :- Math
