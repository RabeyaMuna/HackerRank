def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    temp=[]
    c=0
    for i in string:
       c+=1
       if i not in temp:
          temp.append(i)
       if c==k:
           print(''.join(temp))
           c=0
           temp=[]

           
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
