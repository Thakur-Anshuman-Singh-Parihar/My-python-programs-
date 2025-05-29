import qrcode as qr
img = qr.make(input("Enter your subject to make qr ..."))
img.save("qr.png")
