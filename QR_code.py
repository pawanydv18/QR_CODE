import qrcode

# Data to encode
data = "Hello! Yeh mera QR Code h"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("02_qr.png")

print("QR Code generated and saved as 'example_qr.png'")