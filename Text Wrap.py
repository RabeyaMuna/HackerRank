#textwrap.shorten(text, width, **kwargs): This function truncates the input string so that the length of the string becomes equal to the given width. At first, all the whitespaces are collapsed in the string by removing the whitespaces with a single space. If the modified string fits in the given string, then it is returned otherwise, the characters from the end are dropped so that the remaining words plus the placeholder fit within width.
#textwrap.indent(text, prefix, predicate=None): This function is used to add the given prefix to the beginning of the selected lines of the text. The predicate argument can be used to control which lines are indented.
#textwrap.fill(text, width=70, **kwargs): The fill() convenience function works similar to textwrap.wrap except it returns the data joined into a single, newline-separated string. This function wraps the input single paragraph in text, and returns a single string containing the wrapped paragraph.
#textwrap.wrap(text, width=70, **kwargs): This function wraps the input paragraph such that each line in the paragraph is at most width characters long. The wrap method returns a list of output lines. The returned list is empty if the wrapped output has no content. Default width is taken as 70.
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
