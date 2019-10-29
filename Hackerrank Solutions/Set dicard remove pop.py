n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    inp = input()
    if inp == "pop" and len(s) != 0:
        s.pop()
    else:
        instruction = inp.split()
        if instruction[0] == "remove" and (int(instruction[1]) in s):
            s.remove(int(instruction[1]))
        elif instruction[0] == "discard":
            s.discard(int(instruction[1]))

print(sum(s))