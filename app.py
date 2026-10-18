from flask import Flask, render_template

app = Flask(__name__)

# Default project placeholders (update links later)
PROJECTS = [
    {
        "title": "Inventory Management System",
        "description": "A full-stack web application for tracking products, stock levels, and generating reports using Flask, MySQL, and modern frontend technologies.",
        "link": "#"
    },
    {
        "title": "Real-time Chat Application",
        "description": "Interactive messaging platform with live updates, user authentication, and responsive design built with Flask and JavaScript.",
        "link": "#"
    },
    {
        "title": "Architectural Cost Calculator (BOQ)",
        "description": "Web-based tool for generating Bill of Quantities and cost estimates for construction projects with dynamic calculations.",
        "link": "#"
    },
    {
        "title": "Sudoku Puzzle Game",
        "description": "Browser-based interactive Sudoku game featuring Ajax-powered UI, difficulty levels, and timer functionality.",
        "link": "#"
    },
    {
        "title": "Offline Medicine Expiry Detector",
        "description": "Android application that uses barcode scanning and OCR to detect expired medicines offline, helping pharmacies and protecting patients.",
        "link": "#"
    },
]

RESEARCH_PAPER = {
    "title": "Offline Android App for Expired Medicine Detection using Barcode Scanning and OCR",
    "description": "An offline Android application that uses barcode scanning and Optical Character Recognition (OCR) to automatically detect expired medicine. The system protects patients and helps pharmacies manage stock without requiring an internet connection.",
    "link": "https://www.isroset.org/pdf_paper_view.php?paper_id=4150&1-ISROSET-IJSRMS-11142.pdf",
    "publisher": "ISROSET - International Journal of Scientific Research in Multidisciplinary Studies"
}

@app.route("/")
def index():
    return render_template(
        "index.html",
        projects=PROJECTS,
        research=RESEARCH_PAPER
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
