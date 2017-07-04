import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from textwrap import fill
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


def save_image(number, text, filename):
    image = Image.open('bg.jpg').convert('RGBA')

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Merienda-Bold.ttf', 30)
    dark_gray = (51, 51, 51, 255)

    text = '"' + text.strip() + '"'
    text = fill(text, width=42)

    text_width, text_height = draw.textsize(text, font)
    x_offset = (image.width - text_width) / 2

    draw.text((50, 100), f'#{number}', dark_gray, font)
    draw.text((x_offset, 210), text, dark_gray, font)

    image.save(filename)
