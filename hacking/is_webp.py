from pathlib import Path
import unittest


def is_webp(file_as_bytes):
    file_as_hex = file_as_bytes.hex()

    RIFF = int(file_as_hex[0:8])
    WEBP = int(file_as_hex[16:24])

    return RIFF == 52494646 and WEBP == 57454250
class Test(unittest.TestCase):
    WEBP_FILE_NAME= ''
    def test_webp(self):
        
        file_1 = Path(f'./{self.WEBP_FILE_NAME}').read_bytes()
        result = is_webp(file_1)
        self.assertTrue(result)

if __name__ == "__main__":
    Test.WEBP_FILE_NAME = 'file'
    unittest.main()
