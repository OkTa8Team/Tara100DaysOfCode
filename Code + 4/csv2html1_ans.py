import sys
import xml.sax.saxutils

"""csv2html1_ans.py

    Transform the CSV file into HTML file.

"""

__author__ = "maydee"


def main():
    maxwidth, format = process_options()
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"
            print_line(line, color, maxwidth, format)
            count += 1
        except EOFError:
            break
    print_end()


def print_start():
    print("<table border='1'>")


def print_line(line, color, maxwidth, format):
    print("<tr bgcolor='{0}'>".format(color))
    format_number = "<td align='right'>{{0:{0}}}</td>".format(format)
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print(format_number.format(round(x)))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = xml.sax.saxutils.escape(field)
                else:
                    field = "{0} ...".format(
                        xml.sax.saxutils.escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c    # other quote inside quoted string
            continue
        if quote is None and c == ",": # end of a field
            fields.append(field)
            field = ""
        else:
            field += c        # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields


def process_options():
    maxwidth_str = 'maxwidth='
    format_str = 'format='
    maxwidth = 100
    format = '.0f'

    for arg in sys.argv:
        if arg in ['-h', '-help']:
            print("""\
            usage:
            csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html
    
            maxwidth is an optional integer; if specified, it sets the maximum
            number of characters that can be output for string fields,
            otherwise a default of {0} characters is used.
    
            format is the format to use for numbers; if not specified it
            defaults to "{1}".""".format(maxwidth, format))
            return None, None
        elif arg.startswith(maxwidth_str):
            maxwidth = int(arg[len(maxwidth_str):])
        elif arg.startswith(format_str):
            format = arg[len(format_str):]
    return maxwidth, format


def print_end():
    print("</table>")


main()
