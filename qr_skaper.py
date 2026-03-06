import qrcode
from PIL import Image
data = 'https://vincentkleis.github.io/Bring-linksamlinger/'

logo = Image.open('5f44a660-27d2-4221-b0fa-0479e3a0ae8f (1).png')

save_path = 'qr_code.png'

qr = qrcode.QRCode(
    error_correction= qrcode.ERROR_CORRECT_H
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", bakc_color="white").convert('RGB')

qr_w, qr_h = img.size

logo_w, logo_h = logo.width//5, logo.height//5

logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)

position = ((qr_w - logo_w) // 2, (qr_h - logo_h) // 2)

img.paste(logo, position, logo)

img.save(save_path)