from PIL import Image, ImageDraw, ImageFont

def add_legend(image_path, text_to_add):

    # Load the image
    image = Image.open(image_path)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Define the text properties
    text = "GT Feminisme"
    font = ImageFont.truetype("./fonts/sans_serif.ttf", 60)
    text_color = (0, 0, 0)

    # Calculate the position to center the text
    text_length = draw.textlength(text_to_add, font=font)
    x = image.width / 2
    y = image.height - 40 # 40 pixels from the bottom

    # Add text to the image
    draw.text((x, y), text_to_add, fill=text_color, font=font, align="center", anchor="mm")

    # Save or display the modified image
    image.save(image_path)

if __name__ == '__main__':
    add_legend(image_path="qr_code_destination/Bellevue Chantenay.png", text_to_add="GT Feminisme")