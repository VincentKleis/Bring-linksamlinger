import qrcode
from PIL import Image

logo = Image.open('5f44a660-27d2-4221-b0fa-0479e3a0ae8f (1).png')

logo_w, logo_h = logo.width//5, logo.height//5

logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)

destinations = ["Index", "Drammen", "StokkeSkienLarvik"]


for dest in destinations:
    if dest == "Index":
        save_path = "Index_qr_code.png"
        data = "https://vincentkleis.github.io/Bring-linksamlinger/"
    else:
        save_path = dest + "_qr_code.png"
        data = "https://vincentkleis.github.io/Bring-linksamlinger/Avdelinger/" + dest
    
    qr = qrcode.QRCode(
        error_correction= qrcode.ERROR_CORRECT_H
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", bakc_color="white").convert('RGB')

    qr_w, qr_h = img.size

    position = ((qr_w - logo_w) // 2, (qr_h - logo_h) // 2)

    img.paste(logo, position, logo)

    img.save("QR_coder/"+save_path)