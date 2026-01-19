import qrcode as q


url = input("enter url ").strip()
file_path = "insta.png"  # i can also add here folder path where i have to store image with //
 
qr = q.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)
 
