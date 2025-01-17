import segno
from PIL import Image
import io
import json
import os
from add_text import add_legend

if not os.path.exists('qr_code_destination'):
    os.makedirs('qr_code_destination')

with open('to_generate.json', 'r') as file:
    data = json.load(file)

def create_qr_code(url: str,
                   file_name: str,
                   logo_path: str = None,
                   scale = 20):

    out = io.BytesIO()
    segno.make_qr(url, error='h').save(out, scale=scale, kind='png')

    # Important to let Pillow load the PNG
    out.seek(0)  
    img = Image.open(out)
    img = img.convert('RGB')  # Ensure colors for the output
    img_width, img_height = img.size
    logo_max_size = img_height // 3  # May use a fixed value as well
    logo_img = Image.open(logo_path)  # The logo
    # Resize the logo to logo_max_size
    logo_img.thumbnail((logo_max_size, logo_max_size), Image.Resampling.LANCZOS)
    # Calculate the center of the QR code
    box = ((img_width - logo_img.size[0]) // 2, (img_height - logo_img.size[1]) // 2)
    img.paste(logo_img, box)
    img.save(f'./qr_code_destination/{file_name}.png')

def create_simple_qr_code(url: str,
                   file_name: str,
                   scale = 10, 
                   quiet_zone = 4, 
                   background_color = "#FFFFFF",
                   black_color = "#000000"):


    qr_code = segno.make_qr(url)

    qr_code.save(
        f"qr_code_destination/{file_name}.png",
        scale = scale, 
        border = quiet_zone,
        light = background_color,
        dark = black_color
    )

if __name__ == '__main__':

    for key, value in data.items():
        create_qr_code(url=value["link"], file_name=key, logo_path=value["logo_path"])
        add_legend(image_path=f'qr_code_destination/{key}.png', text_to_add=value["account_name"])
