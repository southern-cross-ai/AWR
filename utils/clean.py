import pdfplumber
import json
import re
import os
from pdfminer.pdfparser import PDFSyntaxError

# Common Latin placeholder words often used in sample text
LATIN_START_WORDS = [
    "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", 
    "elit", "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", 
    "et", "dolore", "magna", "aliqua", "ut", "enim", "ad", "minim", "veniam",
    "quis", "nostrud", "exercitation", "ullamco", "laboris", "nisi", "ut", 
    "aliquip", "ex", "ea", "commodo", "consequat", "duis", "aute", "irure", 
    "dolor", "in", "reprehenderit", "in", "voluptate", "velit", "esse", 
    "cillum", "dolore", "eu", "fugiat", "nulla", "pariatur", "excepteur", 
    "sint", "occaecat", "cupidatat", "non", "proident", "sunt", "in", 
    "culpa", "qui", "officia", "deserunt", "mollit", "anim", "id", "est", "laborum"
]

# Step 1: Function to extract Summary and Details from a single PDF
def extract_summary_and_details_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            all_text = "\n".join([page.extract_text() for page in pdf.pages])

        # Regex to match the "Summary" and "Details" sections
        summary_match = re.search(r'Summary\n(.+?)\nDetails', all_text, re.DOTALL)
        details_match = re.search(r'Details\n(.+)', all_text, re.DOTALL)

        summary = summary_match.group(1).strip() if summary_match else ""
        details = details_match.group(1).strip() if details_match else ""

        return summary, details

    except (PDFSyntaxError, Exception) as e:
        print(f"Error processing {pdf_path}: {e}")
        return None, None

# Step 2: Check if the "Details" section starts with Latin text and decide whether to include it
def should_include_details(details):
    # Check if the first word in the "Details" section is a common Latin placeholder word
    first_word = details.split()[0].lower() if details else ""
    return first_word not in LATIN_START_WORDS

# Step 3: Process all PDFs in a directory and combine their content into one JSON object
def process_pdfs_in_directory(directory_path, output_path):
    combined_data = []  # List to hold all the extracted text content

    # Loop through all PDF files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory_path, filename)
            summary, details = extract_summary_and_details_from_pdf(pdf_path)

            if summary is None and details is None:
                continue  # Skip files that couldn't be processed

            # Decide whether to include the "Details" section based on its content
            if should_include_details(details):
                combined_text = f"{summary} {details}"
            else:
                combined_text = summary

            # Clean up the text content
            combined_text = combined_text.replace("\n", " ").strip()
            combined_text = re.sub(r'\s+', ' ', combined_text)  # Replace multiple spaces with a single space

            # Only add non-empty text content with at least 20 words
            if combined_text and len(combined_text.split()) >= 20:
                combined_data.append({"text": combined_text.strip()})

    # Save the combined_data as a JSON file
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(combined_data, json_file, ensure_ascii=False, indent=4)
    print(f"Combined text saved to {output_path}")

# Define the path to the directory containing the PDF files and the output JSON file
directory_path = "AWR"  # Replace with your PDF folder path
output_path = "AWR_dataset.json"  # Final output JSON file path

# Process all PDFs in the directory and save the results to a JSON file
process_pdfs_in_directory(directory_path, output_path)