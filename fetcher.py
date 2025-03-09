import requests
import pandas as pd

def fetch_pubmed_papers(query, max_results=10):
    """Fetches research papers from PubMed and retrieves full details."""
    
    # Step 1: Fetch paper IDs
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }

    search_response = requests.get(search_url, params=search_params)
    search_data = search_response.json()

    paper_ids = search_data.get("esearchresult", {}).get("idlist", [])
    
    if not paper_ids:
        print("No papers found.")
        return []

    # Step 2: Fetch detailed information for each paper
    return fetch_paper_details(paper_ids)

def fetch_paper_details(paper_ids):
    """Fetches full details of each paper using PubMed Summary API."""
    
    details_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    details_params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }

    response = requests.get(details_url, params=details_params)
    details_data = response.json()

    papers = []
    for paper_id in paper_ids:
        result = details_data.get("result", {}).get(paper_id, {})

        papers.append({
            "PubmedID": paper_id,
            "Title": result.get("title", "N/A"),
            "Publication Date": result.get("pubdate", "N/A"),
            "Non-academic Authors": extract_non_academic_authors(result.get("authors", [])),
            "Company Affiliation(s)": extract_company_affiliations(result.get("authors", [])),
            "Corresponding Author Email": "N/A"  # PubMed does not provide this directly
        })
    
    return papers

def extract_company_affiliations(authors):
    """Extract company names from author affiliations."""
    return ", ".join(
        [
            author["affiliation"] for author in authors
            if isinstance(author, dict)  # Ensure it's a dictionary
            and "affiliation" in author  # Ensure 'affiliation' key exists
            and isinstance(author["affiliation"], str)  # Ensure affiliation is a string
            and ("pharma" in author["affiliation"].lower() or "biotech" in author["affiliation"].lower())
        ]
    )

def extract_non_academic_authors(authors):
    """Filter authors not affiliated with universities or research institutes."""
    return ", ".join(
        [
            author["name"] for author in authors
            if isinstance(author, dict)  # Ensure it's a dictionary
            and "affiliation" in author  # Ensure 'affiliation' key exists
            and isinstance(author["affiliation"], str)  # Ensure affiliation is a string
            and "university" not in author["affiliation"].lower()
            and "lab" not in author["affiliation"].lower()
        ]
    )



def save_to_csv(paper_list, filename="output.csv"):
    """Saves the fetched papers to a CSV file."""
    df = pd.DataFrame(paper_list)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")
