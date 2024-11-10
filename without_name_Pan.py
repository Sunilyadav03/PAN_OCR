import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = 'path of your Pytesseract' 
def extract_pan_details(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Extract text from the image using Tesseract OCR
    ocr_text = pytesseract.image_to_string(gray)
    print("OCR Text:", ocr_text)
    
    # Initialize variables for storing extracted information
    details = {  
        "pan_number": None,
        "dob": None,
        "Candidate Name": None
        
    }

    # Find PAN number (10-character alphanumeric pattern)
    pan_match = re.search(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b', ocr_text)
    if pan_match:
        details["pan_number"] = pan_match.group()
    
    # Find Date of Birth (DOB) in multiple formats
    dob_match = re.search(r'\b(\d{2}[-/ ]\d{2}[-/ ]\d{4}|\d{2} [a-zA-Z]{3} \d{4})\b', ocr_text)
    if dob_match:
        details["dob"] = dob_match.group()
    
    # Split text into lines for line-by-line processing
    lines = ocr_text.splitlines()
    name_lines = [line.strip() for line in lines if line.strip()]
    
    # Patterns for common non-name phrases
    non_name_phrases = ["INCOME TAX DEPARTMENT", "GOVT. OF INDIA"]

    # Heuristic to identify Candidate Name and Father's Name
    for i, line in enumerate(name_lines):
        if re.search(r'^[A-Z\s]+$', line) and not re.search(r'\bPermanent Account Number\b', line):
            # If the line is a common non-name phrase, skip it
            if line in non_name_phrases and i + 2 < len(name_lines):
                # Set the candidate name to the next line and father's name to the line after
                details['Candidate Name'] = name_lines[i + 1]
                details["Father's Name"] = name_lines[i + 2]
            else:
                # Otherwise, assume this is the Candidate Name
                details['Candidate Name'] = line
                # The following line should be the Father's Name
                if i + 1 < len(name_lines):
                    details["Father's Name"] = name_lines[i + 1]
            break  # Stop after finding the names

    return details

# Test the function with image paths

image_path = 'put_your_image_path'  # Replace with the actual image path


print("Image Details:", extract_pan_details(image_path))
