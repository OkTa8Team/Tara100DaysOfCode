import sys
import unicodedata

"""print_unicode_ans.py

    Takes users input and prints into file the Unicode symbols which contain in description the inputted words.

"""

__author__ = "maydee"


def print_unicode_table(words):
    filename = "unicode-table.txt"
    with open(filename, "w", encoding="utf8") as file:
        file.write("decimal   hex   chr  {0:^40}\n".format("name"))
        file.write("-------  -----  ---  {0:-<40}\n".format(""))

        code = ord(" ")
        end = min(0xD800, sys.maxunicode) # Stop at surrogate pairs

        while code < end:
            c = chr(code)
            name = unicodedata.name(c, "*** unknown ***")
            is_print = True
            if words:
                for word in words:
                    is_print = is_print and (word in name.lower())
            if is_print:
                file.write("{0:7}  {0:5X}  {0:^3c}  {1}\n".format(
                            code, name.title()))
            code += 1
    print("wrote results to", filename)


words = []
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string]".format(sys.argv[0]))
        words = 0
    else:
        for word in sys.argv[1:]:
            words.append(word)
        print("word:", words)
if words != 0:
    print_unicode_table(words)