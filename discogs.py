import requests
import json

# your discogs credentials
discogs_username = "murtohilali"
discogs_token = "fJPKYtbTsjKePyhSAfWKlBaJydRIdlyTxCteGLKe" 

# folder 0 is typically your "all" collection
url = f"https://api.discogs.com/users/{discogs_username}/collection/folders/0/releases?token={discogs_token}&per_page=50"

try:
    response = requests.get(url)
    response.raise_for_status()  # raise an error for bad responses
except requests.exceptions.RequestException as e:
    print("error fetching discogs data:", e)
    exit()

data = response.json()
releases = data.get("releases", [])

# build a list with record titles and release ids
records = []
for item in releases:
    basic_info = item.get("basic_information", {})
    title = basic_info.get("title")
    release_id = basic_info.get("id")
    if title and release_id:
        records.append({
            "title": title,
            "release_id": release_id,
            "notes": ""
        })

# save the records to a JSON file
with open("discogs_records.json", "w") as f:
    json.dump(records, f, indent=4)
print(f"Fetched {len(records)} records from Discogs and saved to discogs_records.json.")


