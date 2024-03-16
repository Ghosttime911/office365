import qrcode
from PIL import Image

def generate_qr_with_image(data, img_path, output_path):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="blue", back_color="black")

    img = Image.open(img_path)
    img = img.convert("RGBA")
    img = img.resize((100, 100))

    position = ((qr_img.size[0] - img.size[0]) // 2, (qr_img.size[1] - img.size[1]) // 2)

    qr_img.paste(img, position, img)

    qr_img.save(output_path)

data = "outlook spampage.com"
img_path = "i (1).jpg"
output_path = "qr_with_image.png"

generate_qr_with_image(data, img_path, output_path)
