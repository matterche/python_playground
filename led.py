# LED display

ZERO = [" - ",
        "| |",
        "   ",
        "| |",
        " - "]

ONE = ["   ",
       "  |",
       "   ",
       "  |",
       "   "]

TWO = [" - ",
       "  |",
       " - ",
       "|  ",
       " - "]

PATTERN_LIST = [ZERO, ONE, TWO]

PATTERNS = {
    "0": ZERO,
    "1": ONE,
    "2": TWO
}


def print_pattern(pattern):
    for line in pattern:
        print line


def print_digit(digit):
    print_pattern(PATTERNS[digit])


def print_number(number):
    number_string = str(number)
    for line_index in range(5):
        for digit in number_string:
            print PATTERNS[digit][line_index],
        print


def print_number2(number):
    number_string = str(number)
    lines = ["", "", "", "", ""]
    for digit in number_string:
        for line_index in range(5):
            lines[line_index] += PATTERNS[digit][line_index] + " "
        print

print_number(102)
