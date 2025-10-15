Perfect! Since this is for a **GitHub README.md**, I’ve reformatted your exact content so it renders cleanly — no jumbling, proper spacing, correct markdown hierarchy, and bullet alignment.

Just **copy-paste directly into your `README.md`** ✅

---

````markdown
# 🧠 DocuMind – PDF Parser  
**An intelligent PDF statement extractor with a beautiful UI**

DocuMind is a Streamlit-based PDF parser that extracts five essential fields from Indian credit card statements across multiple banks. It features automatic bank detection, elegant UI, and CSV/JSON exports, making it perfect for demos, hackathons, and evaluations.

---

## ✅ Key Features

### 🔹 Multi-bank Support  
Currently supports 5 major issuers:
- HDFC Bank  
- SBI Card  
- ICICI Bank  
- Axis Bank  
- American Express  

### 🔹 Extracts 5 Structured Fields

| Field               | Example                     |
|----------------------|-----------------------------|
| Bank Name            | HDFC Bank                  |
| Card Last 4 Digits   | 1234                       |
| Statement Period     | 01 Jun 2025 – 30 Jun 2025  |
| Payment Due Date     | 15 Jul 2025                |
| Total Amount Due     | ₹5,432.10                  |

### 🔹 Beautiful Streamlit UI
- Animated gradient background  
- 3D glassmorphism cards  
- Two-page layout (Parse Statements | About)  
- Fully responsive design  

### 🔹 Export Options
- Download extracted data as:
  - ✅ CSV
  - ✅ JSON  
- Auto serial numbering (starting at 1)

### 🔹 Offline & Demo-ready
Runs 100% locally — no API or internet required.

---

## 🧩 Tech Stack

| Layer       | Technology                         |
|-------------|-------------------------------------|
| Frontend    | Streamlit                           |
| PDF Parsing | pdfplumber                          |
| Data Handling | pandas                            |
| Extraction Logic | Regex                         |
| Styling     | Custom CSS (glassmorphism + gradients) |

---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/Aliza952/DocuMind-PDF-Parser.git
cd DocuMind-PDF-Parser

# 2. (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run parser.py
````

---

## 🧠 How It Works

1️⃣ Upload up to 5 PDF credit card statements
2️⃣ DocuMind automatically:

* Detects the bank
* Extracts the 5 key fields
* Displays results in a table

3️⃣ Download outputs as:

* ✅ `DocuMind_Extracted_Data.csv`
* ✅ `DocuMind_Extracted_Data.json`

---

## 🪩 Example Output

| S.No | Filename             | Bank      | Card Last 4 Digits | Statement Period          | Payment Due Date | Total Amount Due |
| ---- | -------------------- | --------- | ------------------ | ------------------------- | ---------------- | ---------------- |
| 1    | hdfc_bank_sample.pdf | HDFC Bank | 1234               | 01 Sep 2025 – 30 Sep 2025 | 15 Oct 2025      | ₹14,789.32       |
| 2    | axis_bank_sample.pdf | Axis Bank | 3456               | 01 Jun 2025 – 30 Jun 2025 | 15 Jul 2025      | ₹5,432.10        |

---

## 🖼️ UI Screenshots

### 🌈 Parse Page

<img width="1918" height="905" alt="image" src="https://github.com/user-attachments/assets/d879a4bd-5a8e-470b-8e94-13f3c868d65e" />

### 📘 About Page

<img width="1917" height="897" alt="image" src="https://github.com/user-attachments/assets/d88b3be2-4ead-4480-ae0d-7aa7f0fc882c" />

---

## 👩‍💻 Author

**Aliza**
✨ “Building intelligent apps that simplify data understanding.”
📧 Reach me on GitHub

---

## 🌟 Acknowledgements

* Streamlit — UI framework
* pdfplumber — Text extraction
* pandas — Data processing

```

---

✅ Let me know if you want:
- Badges (MIT, Python, Stars, etc.)
- A live demo link section
- Table of contents
- Collapsible sections

Otherwise, you're good to go!
```
