import os
import requests
import pandas as pd
from datetime import datetime

# config
output_dir = os.path.join(os.path.dirname(__file__), "..", "api_check")
os.makedirs(output_dir, exist_ok=True)

# general courts 2001 - 2025
general_courts = range(182, 195)
branches = ["House", "Senate"]
base_url = "https://malegislature.gov/api"

# session level endpoints
session_endpoints = [
    "/GeneralCourts/{gc}/Documents",
    "/GeneralCourts/{gc}/Branches/{branch}/RollCalls",
    "/GeneralCourts/{gc}/LegislativeMembers",
]

# document level endpoints
doc_endpoints = [
    "/GeneralCourts/{gc}/Documents/{doc}/RollCalls",
    "/GeneralCourts/{gc}/Documents/{doc}/History",
    "/GeneralCourts/{gc}/Documents/{doc}/Committees",
]

# Test API endpoint
def test_endpoint(url, retries=2):
    """
    Attempt to GET a URL and return a human-readable status label.
    Includes retry logic for timeouts and network instability.

    Parameters:
        url (str): API endpoint URL to test.
        retries (int): Number of retry attempts allowed after a timeout.

    Returns:
        str: Status message ("200 OK", "404 Not Found", "Timeout", etc.)
    """
    for attempt in range(retries + 1):
        try:
            resp = requests.get(url, timeout=10)
            # HTTP 200: endpoint works
            if resp.status_code == 200:
                return "200 OK"
            # HTTP 404: endpoint exists but the resource does not
            elif resp.status_code == 404:
                return "404 Not Found"
            # Any other status codex
            else:
                return f"{resp.status_code} Error"
        except requests.exceptions.ReadTimeout:
            # Retry on timeout if attempts remain
            if attempt < retries:
                continue  # try again if timed out
            return "Timeout (Server too slow)"
        except requests.exceptions.ConnectionError:
            return "Connection Error (Unreachable)"
        except requests.exceptions.RequestException as e:
            return f"Failed: {e.__class__.__name__}"


def main():
    results = []

    # Iterate through each General Court session
    for gc in general_courts:
        # Test endpoints for both branches
        for branch in branches:
            for ep in session_endpoints:
                url = base_url + ep.format(gc=gc, branch=branch)
                status = test_endpoint(url)
                results.append({
                    "GeneralCourt": gc,
                    "Branch": branch,
                    "Endpoint": ep,
                    "URL": url,
                    "Status": status
                })

             # To test document-level endpoints, we must first fetch a list of documents
            docs_url = f"{base_url}/GeneralCourts/{gc}/Documents"
            try:
                doc_resp = requests.get(docs_url, timeout=10)
                if doc_resp.status_code == 200:
                    # Extract up to 2 bill numbers
                    docs = [d.get("BillNumber") for d in doc_resp.json() if d.get("BillNumber")][:2]
                     # Test each document-dependent endpoint
                    for doc in docs:
                        for dep in doc_endpoints:
                            durl = base_url + dep.format(gc=gc, doc=doc)
                            status = test_endpoint(durl)
                            results.append({
                                "GeneralCourt": gc,
                                "Branch": branch,
                                "Endpoint": dep,
                                "URL": durl,
                                "Status": status
                            })
                else:
                    # Could not load document list
                    results.append({
                        "GeneralCourt": gc,
                        "Branch": branch,
                        "Endpoint": "/GeneralCourts/{gc}/Documents",
                        "URL": docs_url,
                        "Status": f"Could not fetch doc list ({doc_resp.status_code})"
                    })
            except Exception as e:
                results.append({
                    "GeneralCourt": gc,
                    "Branch": branch,
                    "Endpoint": "Document Fetch Error",
                    "URL": docs_url,
                    "Status": f"Failed: {e.__class__.__name__}"
                })

    # Convert final results into a DataFrame
    df = pd.DataFrame(results)
    csv_path = os.path.join(output_dir, f"api_audit_results_{datetime.now().strftime('%Y%m%d_%H%M')}.csv")
    df.to_csv(csv_path, index=False)

     # Save audit to CSV
    total = len(df)
    ok = df[df["Status"].str.contains("200 OK")].shape[0]
    failed = df[df["Status"].str.contains("Error|Failed")].shape[0]
    not_found = df[df["Status"].str.contains("404")].shape[0]

    # Summary
    print("API Endpoint Audit Summary")
    print(f"Total tests run: {total}")
    print(f"Successful (200 OK): {ok}")
    print(f"Failed endpoints (400): {failed}")
    print(f"Endpoints not found (404): {not_found}")

if __name__ == "__main__":
    main()
