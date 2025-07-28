import fitz  # PyMuPDF
import json
import os

def is_heading(text, size, fontname):
    fontname = fontname.lower()
    if size >= 15:
        return "H1"
    elif "bold" in fontname and size >= 14:
        return "H1"
    elif "bold" in fontname and size >= 13:
        return "H2"
    return None

def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    title = os.path.basename(pdf_path).replace(".pdf", "")
    outline = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    size = span["size"]
                    font = span["font"]

                    heading_level = is_heading(text, size, font)
                    if heading_level and len(text) > 3 and not text.isnumeric():
                        outline.append({
                            "level": heading_level,
                            "text": text,
                            "page": page_num
                        })

    return {
        "title": title,
        "outline": outline
    }

# Run on the uploaded saq.pdf
pdf_path = "/mnt/data/saq.pdf"
output = extract_outline_from_pdf(pdf_path)
output_path = "/mnt/data/saq_output.json"

# Save the output JSON
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

output_path  # return path to download JSON file
