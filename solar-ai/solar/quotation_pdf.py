from fpdf import FPDF

def generate_pdf(lead_id, user, quote):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "SOLAR QUOTATION", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 8, f"Lead ID: {lead_id}", ln=True)
    pdf.cell(200, 8, f"Customer: {user}", ln=True)
    pdf.ln(5)

    for k, v in quote.items():
        pdf.cell(200, 8, f"{k.replace('_',' ').title()}: {v}", ln=True)

    path = f"data/{lead_id}.pdf"
    pdf.output(path)
    return path
