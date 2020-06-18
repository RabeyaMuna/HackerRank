def minion_game(string):
    # your code goes here
    vowel=['A','E','I','O','U']
    k=0
    s=0
    for i in range(len(string)):
        if string[i] in vowel:
            k+=len(range(i,len(string)))
        else:
            s+=len(range(i,len(string)))
    if s>k:
        print("Stuart",s)
    elif k>s:
        print("Kevin",k)
    else:
        print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)
