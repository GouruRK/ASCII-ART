from unidecode import unidecode
from termcolor import cprint


def load_letters(text: str, font: str):
    """The purpose of this function is to load
    all the characters that will be used to type the text, depending on the
        font. To avoid opening multiple times the same file, all letters
        are saved in a dictionary.

    :param text: text
    :type text: str
    :param font: font
    :type font: str
    :return: the dictionary containing all the letters, and the maximum 
        height of the letters
    :rtype: tuple[dict, int]
    """
    height = 0
    letters = {}
    for letter in text:
        if letter not in letters:
            if letter == " ":
                letters[" "] = {"width": 3, "letter": [" " * 3] * height}
            else:
                lst, width = load_letter(letter, font)
                letters[letter] = {"width": width, "letter": lst}
                height = max(height, len(letters[letter]["letter"]))
    return letters, height


def load_letter(letter: str, font: str):
    """Open and parse file depending on the letter

    :param letter: letter
    :type letter: str
    :param font: font
    :type font: str
    :return: the list containing the letter splited by lines and the width
        of the letter
    :rtype: tuple[list[str], int]
    """
    ascii_code = ord(letter)
    letter_array = []
    width = 0
    with open(f"./fonts/{font}/{ascii_code}.txt") as letter:
        for line in letter:
            letter_array.append(line[:-1])
            width = max(width, len(line))
    return letter_array, width


def pre_process(text: str, font: str, max_length: int):
    """The goal of this function is to load all the needed letters, and 
    split the text in lines depending on the maximum length of the line

    :param text: text
    :type text: str
    :param font: font
    :type font: str
    :param max_length: maximum length of display lines
    :type max_length: int
    :return: the text splited in lines, the letters in the text and the 
        height of each lines
    :rtype: tuple[list[list[str]], dict, int]
    """
    text = unidecode(text)
    new_text = [[]]
    current_width = 0
    letters, height = load_letters(text, font)
    for letter in text:
        letter_width = letters[letter]["width"]
        if current_width + letter_width >= max_length:
            new_text.append([])
            current_width = 0
        new_text[-1].append(letter)
        current_width += letter_width
    return new_text, letters, height


def display(text: list, letters: dict, height: int, style: dict):
    """Apply all of the style and display the text

    :param text: text to display
    :type text: list
    :param letters: dictionary containing all of the letters
    :type letters: dict
    :param height: height of each lines
    :type height: int
    :param style: dictionary containing styles options
    :type style: dict
    """
    letter_spacing = style["spacing"]
    for line in text:
        for i in range(height):
            for letter in line:
                to_print_letter = letters[letter]["letter"][i]
                if letter_spacing != 1:
                    if letter_spacing == 0:
                        to_print_letter = to_print_letter[1:]
                    else:
                        to_print_letter += " " * letter_spacing
                cprint(
                    to_print_letter,
                    color=style["color"],
                    on_color=style["on_color"],
                    attrs=style["effects"],
                    end="",
                )
            print()


def parse_args():
    """Argument parser

    :return: dictionary with inlines arguments
    :rtype: dict
    """
    import argparse
    import os

    parser = argparse.ArgumentParser(description="Ascii art")
    parser.add_argument("text", type=str, help="The text to print")
    parser.add_argument(
        "--font",
        "-f",
        required=False,
        choices={folder for folder in os.listdir("./fonts")},
        default="big",
        type=str,
    )
    parser.add_argument(
        "--spacing",
        "-s",
        required=False,
        default=1,
        type=int,
    )
    parser.add_argument(
        "--color",
        "-c",
        required=False,
        default=None,
        choices={
            "grey",
            "red",
            "green",
            "yellow",
            "blue",
            "magenta",
            "cyan",
            "white",
        },
        type=str,
    )
    parser.add_argument(
        "--on_color",
        "-oc",
        required=False,
        default=None,
        choices={
            "grey",
            "red",
            "green",
            "yellow",
            "blue",
            "magenta",
            "cyan",
            "white",
        },
        type=str,
    )
    parser.add_argument(
        "--effects",
        "-e",
        required=False,
        default=None,
        nargs="+",
        choices={
            "bold",
            "dark",
            "underline",
            "blink",
            "reverse",
            "concealed",
        },
        type=str,
    )
    parser.add_argument(
        "--length",
        "-l",
        required=False,
        default=80,
        type=int,
    )
    return vars(parser.parse_args())


def main():
    args = parse_args()
    if args["on_color"] is not None:
        args["on_color"] = "on_" + args["on_color"]
    formated_text, letters, height = pre_process(
        args["text"], args["font"], args["length"]
    )
    display(formated_text, letters, height, args)


if __name__ == "__main__":
    main()
