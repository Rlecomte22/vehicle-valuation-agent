from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report(vin):
    file_path = f"/tmp/{vin}_valuation_report.pdf"
    c = canvas.Canvas(file_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, f"Vehicle Valuation Report for VIN: {vin}")
    c.drawString(100, 720, "Estimated Value: $25,000")
    c.drawString(100, 700, "Confidence: 85%")
    c.drawString(100, 680, "Source Summary: Placeholder for MMR/KBB/Retail comps")
    c.save()
    return file_path
