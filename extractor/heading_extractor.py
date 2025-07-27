# import fitz  # PyMuPDF

# def extract_headings(pdf_path):
#     doc = fitz.open(pdf_path)
#     outline_data = []
#     headings = []

#     for page_num in range(len(doc)):
#         page = doc[page_num]
#         blocks = page.get_text("dict")["blocks"]

#         for block in blocks:
#             if "lines" not in block:
#                 continue

#             for line in block["lines"]:
#                 line_text = ""
#                 max_font_size = 0

#                 for span in line["spans"]:
#                     line_text += span["text"].strip()
#                     max_font_size = max(max_font_size, span["size"])

#                 if not line_text.strip():
#                     continue

#                 # Define heading levels by font size thresholds
#                 if max_font_size >= 18:
#                     level = "H1"
#                 elif max_font_size >= 14:
#                     level = "H2"
#                 elif max_font_size >= 12:
#                     level = "H3"
#                 else:
#                     continue

#                 headings.append({
#                     "level": level,
#                     "page": page_num + 1,
#                     "text": line_text.strip()
#                 })

#     # Return as [Top-Level Title, [headings]]
#     if headings:
#         title = headings[0]["text"]
#     else:
#         title = "Document Title"

#     outline_data = [title, headings]
#     return outline_data
import fitz  # PyMuPDF

def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)

    headings = []
    font_stats = {}

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    if not text or len(text) < 2:
                        continue
                    font_size = span["size"]
                    is_bold = "bold" in span["font"].lower()
                    font_key = f"{font_size:.1f}-{'bold' if is_bold else 'normal'}"

                    font_stats[font_key] = font_stats.get(font_key, 0) + 1

                    headings.append({
                        "text": text,
                        "size": font_size,
                        "bold": is_bold,
                        "page": page_num
                    })

    # Find top 3 most common sizes to assign H1, H2, H3
    sorted_fonts = sorted(font_stats.items(), key=lambda x: -x[1])
    font_levels = {}
    for i, (font_key, _) in enumerate(sorted_fonts[:3]):
        font_levels[font_key] = f"H{i+1}"

    outline = []
    for h in headings:
        key = f"{h['size']:.1f}-{'bold' if h['bold'] else 'normal'}"
        level = font_levels.get(key)
        if level:
            outline.append({
                "level": level,
                "text": h["text"],
                "page": h["page"]
            })

    title = doc.metadata.get("title") or (outline[0]["text"] if outline else "Untitled Document")

    return title, outline
