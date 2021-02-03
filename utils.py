def balance_line(line_width: int, line: list) -> list:
    """
    Returns a new list with spaces added to each word
    according to the line_width desired.
    Number of spaces differ just by one between lines.
    The most spaces will be between the first lines.
    :param line_width: (int) total line width wanted
    :param line: (list) list of words that need to be justified.
    :return: a list with spaces added to each word
    according to the line_width desired.
    """
    line_length = len(''.join(line))
    equal_space = (line_width - line_length) // (len(line) - 1)
    equal_space_length = equal_space * len(line) + line_length
    extra_space = line_width - equal_space_length

    justified_line = []
    for word in line:
        justified_line.append(word + ' ' * equal_space)
    if extra_space != 0:
        i = 0
        while extra_space > 0:
            justified_line[i] += ' '
            i += 1
            extra_space -= 1
    return justified_line


def print_justified_text(justified_lines: list) -> None:
    """
    Print the justified text in the output
    :param justified_lines: list with justified lines
    :return: None
    """
    print()
    for line in justified_lines:
        print(''.join(line))


def check_line_width(words: list, line_width: int) -> bool:
    """
    Returns True if there is no word with len(word) > line_width,
    False otherwise
    :param words: (list) of words to justify
    :param line_width: (int) line width wanted
    :return: True if there is no word with len(word) > line_width,
    False otherwise
    """
    for word in words:
        if len(word) > line_width:
            return False
        else:
            pass
    return True
