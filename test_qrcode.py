import os
from qrcode_generator import generate_qr_code

def test_qr_code_generation():
    test_link = "https://example.com"
    test_file = "test_qr.png"
    
    generate_qr_code(test_link, test_file)
    
    assert os.path.exists(test_file), "QR code file was not generated"
    os.remove(test_file)

if __name__ == "__main__":
    test_qr_code_generation()
    print("Test passed.")