import os


def print_fonts():
    """
    Prints all available font names
    """

    fonts = load_fonts()
    print_num = 0

    # for every 5 colours printed, the next colour will go to a new line.
    print('\nAvailable fonts:')
    for font in fonts:
        font = font.split('/')[2][:-4]
        print_num += 1
        if print_num != 5:
            print(font + ', ', end='')
        else:
            print_num = 0
            print(font + ', ')


def load_fonts():
    """
    Loads all colours from json file to dict.
    """
    fonts = []
    try:
        # locates the fonts in the font folder
        for root, dirs, files in os.walk('../fonts'):
            for file in files:
                if file.endswith(".ttf"):
                    fonts.append('../fonts/' + file)
    except FileNotFoundError:
        print(f'Could not find the fonts folder!')
        print(exit)
    else:
        return fonts


def input_fonts():
    """
    Prompts the user to input a font. Also deals with error handling.
    """
    fonts = load_fonts()
    fonts = [font.split('/')[2][:-4] for font in fonts]
    while True:
        try:
            print('\nIf you would like to list available fonts enter "help"')
            user_input = input(f'Enter a font: ')

            if user_input == 'help':
                print_fonts()
                continue
            if user_input not in fonts:
                raise KeyError
        except KeyError:
            print('\nThat was not a valid font!')
        else:
            return '../fonts/' + user_input + '.ttf'


def input_font_size():
    """
    Prompts the user to input a font size. Also deals with error handling.
    """
    while True:
        try:
            user_input = input('\nPlease enter a font size: ')
            a = float(user_input)
            b = int(user_input)
            if a != b:
                raise ValueError
        except ValueError:
            print('\nThat was not a valid size!')
        else:
            return int(user_input)
