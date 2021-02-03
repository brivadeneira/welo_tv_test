import argparse

from utils import balance_line, print_justified_text, check_line_width


def justify_text(text: str, line_width: int) -> list:
    """
    Justify a text with a line_width wanted
    :param text: (str) to justify
    :param line_width: (int) line_width wanted
    :return: (list) with justified lines
    """
    words = text.replace(' ', '* ').split('*')
    if not check_line_width(words, line_width):
        raise ValueError(f"A word length exceeds the long {line_width} width.")

    char_sum = 0
    line = []
    lines = []

    for word in words:
        if not line:
            # remove the space at the beginning of the line
            word = word.replace(' ', '')
        char_sum += len(word)
        line.append(word)
        if char_sum >= line_width:
            if char_sum > line_width:
                lines.append(line[:-1])
                last_word = line[-1].replace(' ', '')
                # extra word will be the beginning of next line
                line = [last_word]
                char_sum = len(last_word)
            else:
                lines.append(line)
                line, char_sum = [], 0
        else:
            pass

    # check if there is more words in the text
    if lines[-1][-1] != words[-1]:
        word = words[-1].replace(' ', '')
        lines.append([word])

    justified_lines = []
    for line in lines[:-1]:
        justified_line = balance_line(line_width, line)
        justified_lines.append(justified_line)
    justified_lines.append(lines[-1])

    return justified_lines


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str,
                        help='a text to justify')
    parser.add_argument('width', type=int,
                        help='the line width wanted')
    args = parser.parse_args()

    text = args.text
    line_width = args.width

    justified_lines = justify_text(text, line_width)
    print_justified_text(justified_lines)


if __name__ == '__main__':
    main()
