if __name__ == '__main__':
    N = int(input())
    L=[]
    for i in range(N):
        s=input().split()
        command=s[0]
        if command=="insert":
            L.insert(int(s[1]),int(s[2]))
        elif command=="remove":
            L.remove(int(s[1]))
        elif command=="append":
            L.append(int(s[1]))
        elif command=="sort":
            L.sort()
        elif command=="pop":
            L.pop()
        elif command=="reverse":
            L.reverse()
        elif command=="print":
            print(L)
