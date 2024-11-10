# PAN_OCR

## Overview
PAN_OCR is a Python-based project for Optical Character Recognition (OCR) on PAN cards. The repository has scripts to carry out OCR data, about PAN card images, based on whether the texts contain the word "Name."

## Repository Structure


To run these scripts, you will need to have the following Python packages installed:

pytesseract: Python wrapper for Google's Tesseract-OCR engine
opencv-python: For image processing



## Additional Prerequisites
Tesseract-OCR: Install Tesseract-OCR so it is available from the command line. You can download it from the Tesseract official GitHub repository.

https://github.com/madmaze/pytesseract.git

##### without_name_Pan.py
This code has been developed for PAN cards where "Name" is not present in the OCR text. It is logics based on parsing and extraction of required fields from OCR data without relying on the keyword "Name".
For its use case, You can the file "

##### Name_Pan.py
This script is specifically oriented toward PAN cards. By making use of the fact that the word "Name" occurs in the OCR text as some reference point to help locate the fields with precision in OCR results.
For its use case, You can the file "

## Participation
Feel free to fork this repository and make pull requests to add your contributions to the project. All of your contributions are welcome. 

## License
This project is open-source and licensed under the MIT License. See LICENSE for more information.
