import os
import requests
import pandas as pd

# generalCourtNumber: Current Massachusetts General Court session
# For 2025–2026, the session number is 194
generalCourtNumber = 194
branch = "Senate" 

# Here we check roll calls 1–100 inclusive
rollCallRange = range(1, 101) 
output_dir = os.path.join(os.path.dirname(__file__), "..", "senate_api")
os.makedirs(output_dir, exist_ok=True)


# Function: Fetch a single roll call summary from the MA Legislature API
def get_rollcall_summary(rollCallNumber):
    # Construct API URL for the target roll call number
    url = f"https://malegislature.gov/api/GeneralCourts/{generalCourtNumber}/Branches/{branch}/RollCalls/{rollCallNumber}"
    resp = requests.get(url)
    # If API returns 404, that roll call does not exist for this session
    if resp.status_code == 404:
        return {"rollCallNumber": rollCallNumber, "hasData": False, "yeas": 0, "nays": 0, "absent": 0}

    try:
        # Raise exception for other HTTP errors
        resp.raise_for_status()
        data = resp.json()
        # Extract vote counts
        yeas = len(data.get("Yeas", []))
        nays = len(data.get("Nays", []))
        absent = len(data.get("Absent", []))
        total_votes = yeas + nays + absent
        # Return parsed roll call information
        return {
            "rollCallNumber": rollCallNumber,
            "hasData": total_votes > 0,
            "yeas": yeas,
            "nays": nays,
            "absent": absent,
        }
    except Exception:
        # If any error occurs treat it as missing data.
        return {"rollCallNumber": rollCallNumber, "hasData": False, "yeas": 0, "nays": 0, "absent": 0}


# main: Check API coverage for all roll calls
def main():
    results = []
    for num in rollCallRange:
        summary = get_rollcall_summary(num)
        results.append(summary)

    # Convert results into a DataFrame
    df = pd.DataFrame(results)

    # save to csv
    csv_path = os.path.join(output_dir, "senate_api_coverage.csv")
    df.to_csv(csv_path, index=False)

    # summary
    total = len(df)
    available = df["hasData"].sum()
    coverage = (available / total) * 100

    print("Senate API coverage summary")
    print(f"Total roll calls checked: {total}")
    print(f"Available roll calls with data: {available}")
    print(f"API coverage: {coverage:.1f}%")
    print(f"Saved detailed results to: {csv_path}")


if __name__ == "__main__":
    main()