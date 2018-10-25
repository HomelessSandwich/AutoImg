try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    input('Could not find the pillow module!')
    print(exit)
from colours import input_colour
from fonts import input_fonts, input_font_size
from save_file import save_file
from file_to_text import get_csv_data


def input_location(img_size):
    """
    Prompt the user to input a  y location for text placement. Also deals with error handling.
    """

    while True:
        print(f'\nPlease enter a number between 0 and {img_size}')
        while True:
            try:
                y = int(input('Enter an y coordinate: '))
            except ValueError:
                print('\nThat is not a valid y coordinate!')
            else:
                break

        if 0 < y < img_size:
            break
        else:
            print('\nThat is not a valid y coordinate!')

    return y


def preview_text(base, txt):
    out = Image.alpha_composite(base, txt)
    out.show()


def draw_text(d, fnt, txt, base_width, loc, colour):
    txt_width, txt_height = d.textsize(txt, fnt)
    txt_y = loc
    txt_colour = colour
    return d.text(
        ((base_width - txt_width) / 2, txt_y), txt,
        font=fnt, fill=txt_colour
    )


def draw_confirmed_text(d, fnt, txt, base_width, loc, colour):
    txt_width, txt_height = d.textsize(txt, fnt)
    txt_y = loc
    txt_colour = colour
    return d.text(
        ((base_width - txt_width) / 2, txt_y), txt,
        font=fnt, fill=txt_colour
    )


def text_draw():
    """
    Creates a new Image object based off user inputted variables.
    """

    # get an image
    try:
        img_loc = '../img/base.png'
        base = Image.open(img_loc).convert('RGBA')
    except FileNotFoundError:
        print(f'Could not find {img_loc}!')
        print('Make sure "base.png" is included in the img folder!')
        print(exit)
    base_width, base_height = base.size
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

    file_names, texts = get_csv_data()

    colour1 = 'white'
    colour2 = 'black'
    loc1 = 900
    loc2 = 1600
    confirm = False

    for i, text in enumerate(texts, 0):
        while True:
            # get a drawing context
            d = ImageDraw.Draw(txt)

            if not confirm:
                # draw text
                print('\nPlease enter details for Text 1')
                # get a font
                fnt1 = ImageFont.truetype(input_fonts(), input_font_size())
                colour1 = input_colour()
                loc1 = input_location(base_height)
                draw_text(d, fnt1, text[0], base_width, loc1, colour1)

                # draw text 2
                print('\n\nPlease enter details for Text 2')
                fnt2 = ImageFont.truetype(input_fonts(), input_font_size())
                colour2 = input_colour()
                loc2 = input_location(base_height)
                draw_text(d, fnt2, text[1], base_width, loc2, colour2)
            else:
                draw_confirmed_text(d, fnt1, text[0], base_width, loc1, colour1)
                draw_confirmed_text(d, fnt2, text[1], base_width, loc2, colour2)

            out = Image.alpha_composite(base, txt)
            out.show()

            while True:
                user_confirm = input('\nConfirm output (y/n): ').lower()
                if user_confirm == 'y' or user_confirm == 'n':
                    break
                else:
                    print('\nThat was not a valid input!')

            if user_confirm == 'y':
                confirm = True
                out = Image.alpha_composite(base, txt)
                out.save(save_file() + f'/{file_names[i]}.png', "PNG", quality=100)
                txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
                break
            else:
                txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
                confirm = False

