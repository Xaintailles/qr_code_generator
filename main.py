import segno

def create_qr_code(url: str, 
                   scale = 5, 
                   quiet_zone = 4, 
                   background_color = "#FFFFFF",
                   black_color = "#000000"):


    qr_code = segno.make_qr(url)

    qr_code.save(
        "qr_code.png",
        scale = scale, 
        border = quiet_zone,
        light = background_color,
        dark = black_color
    )

url = "https://pays-de-la-loire.lesecologistes.fr/posts/27hdWEwgpKIsLn67yb3AeE/le-29-septembre-on-fete-l-ecologie-a-nantes"

create_qr_code(url)