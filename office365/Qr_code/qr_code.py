import qrcode

data = ""

qr = qrcode.make(data)

qr.save("qr_code.png")

qr.show()
