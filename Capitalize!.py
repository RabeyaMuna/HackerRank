def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
# the capitalize() method converts the first character of a string to capital (uppercase) letter. If the string has its first character as capital, then it returns the original string.
