A=set(map(int, input().split()))
for i in range(int(input())):
    if not A.issuperset(set(map(int, input().split()))):
        print(False)
        break
else:
    print(True)
