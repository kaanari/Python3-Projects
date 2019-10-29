# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m = tuple(map(int,input().split()))
arr = list(map(int,input().split()))
likes = set(map(int,input().split()))
dislikes = set(map(int,input().split()))

posPoint = likes.intersection(arr)
negPoint = dislikes.intersection(arr)

finalPoint = 0

for i in arr:
    if i in posPoint:
        finalPoint += 1
    elif i in negPoint:
        finalPoint -= 1

print(finalPoint)