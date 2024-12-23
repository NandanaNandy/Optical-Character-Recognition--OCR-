import easyocr

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

# Path to the image containing Tamil text
image_path = "C:/Users/nares/Documents/OCR/1.jpg" #replace your own image path

# Perform text extraction
results = reader.readtext(image_path)

# Display the extracted text
print("Extracted Text:")
for result in results:
    print(result[1])  # Print only the detected text part