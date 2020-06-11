#The format() function returns a formatted representation of a given value specified by the format specifier
# rjust(): will right align the string, using a specified character (space is default) as the fill character.string.rjust(length, character)
# binary format: format(i, 'b')
# hex format:format(i, 'x')
#binary formate:format(number, 'b')
#octal format:format(i, 'o')
def print_formatted(number):
    # your code goes here
   w = len(format(number, 'b'))
   for i in range(1, number+1):
        d = str(i).rjust(w)
        o = format(i, 'o').rjust(w)
        h = format(i, 'x').rjust(w).upper()
        b = format(i, 'b').rjust(w)
        print(d, o, h, b)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
