import os
import requests
import pandas as pd

# config
generalCourtNumber = 194  # for current year (2025–26)
branch = "Senate" 
rollCallRange = range(1, 101)  # check roll call numbers 1–100
output_dir = os.path.join(os.path.dirname(__file__), "..", "senate_api")
os.makedirs(output_dir, exist_ok=True)


# function
def get_rollcall_summary(rollCallNumber):
    url = f"https://malegislature.gov/api/GeneralCourts/{generalCourtNumber}/Branches/{branch}/RollCalls/{rollCallNumber}"
    resp = requests.get(url)
    if resp.status_code == 404:
        return {"rollCallNumber": rollCallNumber, "hasData": False, "yeas": 0, "nays": 0, "absent": 0}

    try:
        resp.raise_for_status()
        data = resp.json()
        yeas = len(data.get("Yeas", []))
        nays = len(data.get("Nays", []))
        absent = len(data.get("Absent", []))
        total_votes = yeas + nays + absent
        return {
            "rollCallNumber": rollCallNumber,
            "hasData": total_votes > 0,
            "yeas": yeas,
            "nays": nays,
            "absent": absent,
        }
    except Exception:
        return {"rollCallNumber": rollCallNumber, "hasData": False, "yeas": 0, "nays": 0, "absent": 0}


# main
def main():
    results = []
    for num in rollCallRange:
        summary = get_rollcall_summary(num)
        results.append(summary)

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