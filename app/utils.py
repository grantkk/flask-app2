from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def format_option(text):
    import re
    text = re.sub(r'[ＡＢＣＤ]', lambda m: chr(ord(m.group(0)) - 0xFEE0), text)
    text = re.sub(r'[（）]', lambda m: '(' if m.group(0) == '（' else ')', text)
    text = re.sub(r'\(?([A-D])\)?', r'(\1)', text)
    text = re.sub(r'\(\w\)\s*', lambda m: f"{m.group(0).strip()} ", text)
    return text

def set_font_to_mingti(paragraph):
    for run in paragraph.runs:
        run.font.name = "新細明體"
        r = run._element
        rFonts = OxmlElement("w:rFonts")
        rFonts.set(qn("w:eastAsia"), "新細明體")
        r.insert(0, rFonts)

def process_word_file(input_file, output_file):
    doc = Document(input_file)
    for paragraph in doc.paragraphs:
        if any(option in paragraph.text for option in ["A", "B", "C", "D", "Ａ", "Ｂ", "Ｃ", "Ｄ"]):
            paragraph.text = format_option(paragraph.text)
            set_font_to_mingti(paragraph)
    doc.save(output_file)
