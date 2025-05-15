import qrcode
from PIL import Image

data = "https://github.com/DevaharshaM"

qr = qrcode.QRCode(
    version=2,  
    error_correction=qrcode.constants.ERROR_CORRECT_H,  
    box_size=10,
    border=4
)
qr.add_data(data)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="darkblue", back_color="white").convert('RGB')

logo = Image.open("gitLogo.png")  
logo = logo.resize((60, 60), Image.LANCZOS)

qr_width, qr_height = qr_img.size
logo_pos = ((qr_width - logo.size[0]) // 2, (qr_height - logo.size[1]) // 2)

qr_img.paste(logo, logo_pos, mask=logo if logo.mode == 'RGBA' else None)

qr_img.save("QR_portfolio.png")

print("Saved as image.png")
