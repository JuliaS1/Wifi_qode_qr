import qrcode

# Replace with your formatted Wi-Fi information
wifi_info = "WIFI:S:your_network_name;T:WPA2;P:your_password;;"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(wifi_info)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("wifi_qr.png")
