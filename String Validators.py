#str.isalnum():This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
#str.isalpha():This method checks if all the characters of a string are alphabetical (a-z and A-Z).
#str.isdigit():This method checks if all the characters of a string are digits (0-9).
#str.islower():This method checks if all the characters of a string are lowercase characters (a-z).
#str.isupper():This method checks if all the characters of a string are uppercase characters (A-Z).
if __name__ == '__main__':
    str = input()
    print (any (c.isalnum()  for c in str))
    print (any(c.isalpha() for c in str))
    print (any(c.isdigit() for c in str))
    print (any(c.islower() for c in str))
    print (any(c.isupper() for c in str))
