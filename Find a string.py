def count_substring(string, sub_string):
    results = 0
    for i in range(0,len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            results += 1
    return results
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
