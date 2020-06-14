import string
def print_rangoli(size):
    # your code goes here
    alpha = string.ascii_lowercase
    n =size
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append(s[::-1]+s[1:])

    width = len(L[0])

    for i in range(n-1, 0, -1):
        print(L[i].center(width, "-"))
    for i in range(n):
        print(L[i].center(width, "-"))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
