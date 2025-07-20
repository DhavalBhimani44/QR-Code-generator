import qrcode

def generate_qr_code(link, filename):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the instance
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image to a file
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

if __name__ == "__main__":
    link = input("Enter the link to convert to QR code: ")
    filename = input("Enter the filename to save the QR code (e.g., 'qrcode.png'): ")
    generate_qr_code(link, filename)
