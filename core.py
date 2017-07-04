import pandas as pd
import textwrap
from PIL import Image, ImageDraw, ImageFont
from os import path


def generate_images(input_file, output_dir):
    input_file = input_file.lower()

    if input_file.endswith('xlsx') or input_file.endswith('xls'):
        df = pd.read_excel(input_file)
        df = df.reset_index()

    elif input_file.endswith('csv'):
        df = pd.read_csv(input_file)

    else:
        raise Exception('Formato de arquivo inválido')

    df.columns = ('datetime', 'text', 'status', 'reason', 'editor', 'number')

    starting_number = int(df.number.max() + 1)
    texts = df[df.status.isnull()].text

    for i, text in texts.iteritems():
        number = starting_number + i
        save_image(number, text, path.join(output_dir, f'{number}.png'))


def save_image(number, text, filename, background='bg.jpg', font_size=30,
               font_face='Merienda-Bold.ttf', text_color=(51, 51, 51, 255),
               column_limit=42, number_pos=(50, 100), text_y_offset=210):
    image = Image.open(background).convert('RGBA')

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_face, font_size)

    text = textwrap.fill(f'"{text.strip()}"', column_limit)

    text_width, text_height = draw.textsize(text, font)
    x_offset = (image.width - text_width) / 2

    draw.text(number_pos, f'#{number}', text_color, font)
    draw.text((x_offset, text_y_offset), text, text_color, font)

    image.save(filename)
