def average(array):

    x = sum(set(array))/len(set(array))
    return x

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)