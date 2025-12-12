import requests
import pandas as pd
import time

def get_house_legislators(session_number):
    """
    Get all House legislators for a given General Court session
    """
    print(f"\nFetching House legislators for General Court {session_number}...")
    
    # Try to get all legislators at once
    url = f"https://malegislature.gov/api/GeneralCourts/{session_number}/LegislativeMembers"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Debug: print first member to see structure
        if data and len(data) > 0:
            print(f"Sample member data: {data[0]}")
            print(f"Total members returned: {len(data)}")
        
        # Filter for House only
        house_legislators = []
        for member in data:
            branch = member.get('Branch')
            print(f"Found member: {member.get('Name')} - Branch: {branch}")  # Debug
            if branch == 'House':
                full_name = member.get('Name', '')
                name_parts = full_name.split()
                
                house_legislators.append({
                    'First Name': name_parts[0] if name_parts else None,
                    'Last Name': name_parts[-1] if len(name_parts) > 1 else name_parts[0] if name_parts else None,
                    'Full Name': full_name,
                    'District': member.get('District'),
                    'Party': member.get('Party'),
                    'Room': member.get('RoomNumber'),
                    'Phone': member.get('PhoneNumber'),
                    'Email': member.get('EmailAddress'),
                    'General Court': session_number
                })
        
        df = pd.DataFrame(house_legislators)
        print(f"✓ Retrieved {len(df)} House legislators for General Court {session_number}")
        return df
        
    except Exception as e:
        print(f"✗ Error fetching General Court {session_number}: {e}")
        return None


# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("Fetching Historical House Legislator Rosters")
    print("=" * 60)
    
    # Get legislators for each session
    # 191 = 2019-2020
    # 192 = 2021-2022
    # 193 = 2023-2024
    # 194 = 2024