import unittest
import sys
import os
from PIL import Image
sys.path.append(os.path.abspath(os.path.join('../utils')))


from compose import compose_vertical_image  # Assuming compose.py is in the same directory or accessible

class TestComposeVerticalImage(unittest.TestCase):
    
    def test_compose_basic(self):
        # Define paths to sample images (replace with actual paths)
        header_image_path = 'path/to/header_image.png'
        logo_image_path = 'path/to/logo_image.png'
        thumbnail_image_path = 'path/to/thumbnail_image.png'
        
        # Temporary path for output image during testing
        output_image_path = 'output/composed_image_test.png'
        
        # Call the function to compose the image
        compose_vertical_image(header_image_path, logo_image_path, thumbnail_image_path, output_image_path)
        
        # Load the composed image for assertions
        composed_image = Image.open(output_image_path)
        
        # Perform assertions to verify correctness
        self.assertEqual(composed_image.size, (expected_width, expected_height))  # Replace with expected dimensions
        # Add more assertions based on your function's behavior
        
        # Optionally, you can also assert specific pixel values or other properties of the composed image

if __name__ == '__main__':
    unittest.main()

