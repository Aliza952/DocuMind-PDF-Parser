import matplotlib.pyplot as plt
from pathlib import Path
from zipfile import ZipFile

out_dir = Path("sample_pdfs")
out_dir.mkdir(exist_ok=True)

def make_pdf(bank, lines, filename):
    fig = plt.figure(figsize=(8.27, 11.69))  # A4 portrait
    plt.axis("off")
    y = 0.95
    plt.text(0.08, y, f"{bank} Credit Card Statement", fontsize=16)
    y -= 0.05
    for line in lines:
        plt.text(0.08, y, line, fontsize=12)
        y -= 0.04
    fig.savefig(out_dir / filename, format="pdf", bbox_inches="tight")
    plt.close(fig)

samples = {
    "HDFC Bank": [
        "Card No: XXXX 1234",
        "Statement Period: 01 Sep 2025 – 30 Sep 2025",
        "Payment Due Date: 15 Oct 2025",
        "Total Amount Due: ₹ 14,789.32",
    ],
    "SBI Card": [
        "Card ending with 5678",
        "Statement Period: 01 Aug 2025 – 31 Aug 2025",
        "Payment Due Date: 15 Sep 2025",
        "Total Amount Due: ₹ 8,901.00",
    ],
    "ICICI Bank": [
        "Card No. XXXX-9012",
        "Statement Period: 01/07/2025 – 31/07/2025",
        "Payment Due Date: 15/08/2025",
        "Total Payment Due: ₹ 23,456.78",
    ],
    "Axis Bank": [
        "Card No XXXX 3456",
        "Statement Period : 01.06.2025 – 30.06.2025",
        "Payment Due Date : 15.07.2025",
        "Total Amount Due : ₹ 5,432.10",
    ],
    "American Express": [
        "Card ending with 7890",
        "Statement Period: 01 Aug 2025 – 31 Aug 2025",
        "Due Date: 14 Sep 2025",
        "New Balance: $456.78",
    ],
}

# Generate PDFs
pdf_paths = []
for bank, lines in samples.items():
    fname = bank.lower().replace(" ", "_") + "_sample.pdf"
    make_pdf(bank, lines, fname)
    pdf_paths.append(out_dir / fname)

# Zip them up
zip_path = out_dir / "DocuMind_Sample_PDFs.zip"
with ZipFile(zip_path, "w") as zf:
    for p in pdf_paths:
        zf.write(p, p.name)

print("✅ PDFs created in:", out_dir.resolve())
