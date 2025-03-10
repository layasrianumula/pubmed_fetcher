# PubMed Fetcher

##  Overview

**PubMed Fetcher** is a Python CLI tool that fetches research papers from PubMed, extracts full details, and filters authors affiliated with pharmaceutical or biotech companies. The results are saved in a CSV file for easy access and analysis.

##  Features

- Fetches research papers from **PubMed API**
- Extracts **Title, Authors, Publication Date, and Affiliations**
- Filters out **non-academic authors & biotech/pharma affiliations**
- Saves results as **CSV file**
- Command-line options for **debug mode** and **custom file output**

##  Installation & Setup

### **1️ Install Dependencies**

Make sure you have **Python 3.9+** installed. Then, install dependencies using **Poetry**:

```sh
poetry install
```

### **2️ Run the Script**

```sh
poetry run get-papers-list "cancer treatment" -f papers.csv
```

 This will fetch research papers related to "cancer treatment" and save them to `papers.csv`.

##  Example Output

| PubMed ID | Title                    | Publication Date | Non-academic Authors | Company Affiliation(s)  | Email |
| --------- | ------------------------ | ---------------- | -------------------- | ----------------------- | ----- |
| 12345678  | AI in Medicine: A Review | 2024-01-15       | Dr. Smith, Dr. Lee   | ABC Pharma, XYZ Biotech | N/A   |

##  Folder Structure

```
pubmed_fetcher/        <- Main project folder
│── poetry.lock        <- Poetry dependency file
│── pyproject.toml     <- Project configuration file
│── README.md          <- Project documentation
│
├── pubmed_fetcher/    <- Python package folder
│   │── __init__.py    <- Makes this folder a package
│   │── fetcher.py     <- Fetches papers & processes details
│   │── cli.py         <- CLI tool for running the script
│
└── tests/             <- (Optional) Folder for test cases
    │── __init__.py
```

##  Future Improvements

- Fetch **abstracts, journal names, and keywords**
- Add **support for JSON and Excel formats**
- Implement **error logging & retry mechanism**
- Build a **web interface using Flask/FastAPI**

##  Contributing

Feel free to fork this repository and submit pull requests for improvements!

##  License

This project is licensed under the **MIT License**.

---






