import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = 'Path_of_Pytesseract'
def preprocess_dob(text):
    -- Replace 'o' and 'O' with '0' to handle OCR misreadings specifically in DOB
    return text.replace('o', '0').replace('O', '0')

def extract_pan_details(image_path):
    -- Read the image
    image = cv2.imread(image_path)
    
    -- Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    -- Use OCR to extract text from the image
    text = pytesseract.image_to_string(gray)
    print("Raw OCR Text:", text)
    
    -- Initialize an empty dictionary to store extracted information
    pan_details = {
        "PAN Number": None,
        "Date of Birth": None,
        "Candidate Name": None,
        "Father's Name": None
    }
    
    -- Extract PAN number using regex
    pan_match = re.search(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b', text)
    if pan_match:
        pan_details["PAN Number"] = pan_match.group()
    
    -- Extract DOB using regex with preprocessed DOB text
    dob_text = preprocess_dob(text)  -- Preprocess only for DOB
    dob_match = re.search(r'\b(\d{2}[-/ ]\d{2}[-/ ]\d{4})\b', dob_text)
    if dob_match:
        pan_details["Date of Birth"] = dob_match.group()
    
    -- Split text into lines for line-by-line processing
    lines = text.splitlines()
    
    -- Variables to track the first and second occurrence of "Name" variations
    name_found = 0

    -- Define a pattern that includes "Name" and common variations
    name_pattern = re.compile(r'\b(Name|Neme|name|neme|Nome|nome)\b', re.IGNORECASE)

    -- Iterate through lines to find candidate and father's names
    for i, line in enumerate(lines):
        -- Find occurrences of "Name" variations
        if name_pattern.search(line):
            name_found += 1
            if name_found == 1 and i + 1 < len(lines):  -- First "Name" is candidate's name
                pan_details["Candidate Name"] = re.sub(r'\d', '', lines[i + 1].strip())  -- Remove digits if any
            elif name_found == 2 and i + 1 < len(lines):  -- Second "Name" is father's name
                pan_details["Father's Name"] = re.sub(r'\d', '', lines[i + 1].strip())  -- Remove digits if any
                break  -- Stop after finding the father's name

    return pan_details

-- Test with an image path
image_path = "Image Path"  -- Replace with actual image path
pan_details = extract_pan_details(image_path)
print(pan_details)
