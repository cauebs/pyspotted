import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from textwrap import fill


def import_text(filename):
    filename = filename.lower()

    if filename.endswith('xlsx') or filename.endswith('xls'):
        df = pd.read_excel(filename)
        df = df.reset_index()

    elif filename.endswith('csv'):
        df = pd.read_csv(filename)

    else:
        raise Exception("Formato de arquivo inválido")

    df = df.fillna('')
    df.columns = ('datetime', 'text', 'status', 'reason', 'editor', 'number')
    # do something


def save_image(number, text, filename):
    image = Image.open('bg.jpg').convert('RGBA')

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Merienda-Bold.ttf', 30)
    dark_gray = (51, 51, 51, 255)

    text = '"' + text.strip() + '"'
    text = fill(text, width=45)

    draw.text((50, 100), f'#{number}', dark_gray, font)
    draw.text((50, 210), text, dark_gray, font)

    image.save(filename)
