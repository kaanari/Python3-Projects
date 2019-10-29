def operations(N):
    list1 = []
    for i in range(N):
        inp = input()
        if " " in inp:
            instruction = inp.split()
            instruction[1:] = list(map(int,instruction[1:]))

            if instruction[0] == "insert":
                list1.insert(instruction[1],instruction[2])
            elif instruction[0] == "append":
                list1.append(instruction[1])
            elif instruction[0] == "remove":
                list1.remove(instruction[1])
        else:
            if inp == "pop":
                list1.pop()
            elif inp == "sort":
                list1.sort()
            elif inp == "reverse":
                list1.reverse()
            elif inp == "print":
                print(list1)

if __name__ == '__main__':
    N = int(input())

    operations(N)

