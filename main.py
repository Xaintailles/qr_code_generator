import segno
import json
import os

if not os.path.exists('qr_code_destination'):
    os.makedirs('qr_code_destination')

with open('to_generate.json', 'r') as file:
    data = json.load(file)

def create_qr_code(url: str,
                   file_name: str,
                   scale = 5, 
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

for key, value in data.items():
    create_qr_code(url=value, file_name=key)