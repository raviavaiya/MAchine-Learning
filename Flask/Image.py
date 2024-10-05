# Let's extract the text from the uploaded image to retrieve the code shown in it.
from PIL import Image
import pytesseract

# Load the image from the uploaded file
image_path = 'C:/Users/ravia/OneDrive/Pictures/Screenshots/Screenshot 2024-10-05 151110.png'
image = Image.open(image_path)

# Use pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(image)

extracted_text
