#A set is an unordered collection of elements without duplicate entries.
#When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

def average(array):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
