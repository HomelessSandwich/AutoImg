import json


def print_colours(colours):
    """
    Prints all available colour names
    """
    colours_dic = colours
    print_num = 0

    # for every 5 colours printed, the next colour will go to a new line.
    print('\nAvailable colours:')
    for key in colours_dic:
        print_num += 1
        if print_num != 5:
            print(key + ', ', end='')
        else:
            print_num = 0
            print(key + ', ')


def load_colours():
    """
    Loads all colours from json file to dict.
    """

    try:
        # locates the colours file
        colours_loc = '../colours/colours.json'
        colours_file = open(colours_loc)
        colours_str = colours_file.read()
        # loads the json file into a dictionary
        colours_dict = json.loads(colours_str)
    except FileNotFoundError:
        print(f'Could not find {colours_loc}!')
        print('Make sure "colours.json" is included in the colours folder!')
        print(exit)
    else:
        return colours_dict


def input_colour():
    """
    Prompts the user to input a colour. Also deals with error handling.
    """
    colours = load_colours()
    while True:
        print('\nIf you would like to list available colours enter "help"')
        user_input = input('Enter a colour: ')

        if user_input == 'help':
            print_colours(colours)
            continue

        try:
            return tuple(colours[user_input])
        except KeyError:
            print('\nThat was not a valid colour!')
