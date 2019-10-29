# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input()) 
set1 = set(map(int,input().split()))
n = int(input()) 
set2 = set(map(int,input().split()))


result = set1.difference(set2)
result.update(set2.difference(set1))

for i in sorted(result):
    print(i)

