import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("AWS DevOps refers to the practices and tools.")
qr.make(fit=True)
img = qr.make_image()
img.save("AwsCu.png")

