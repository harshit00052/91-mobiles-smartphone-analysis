import requests
import json
import time

url = 'https://www.91mobiles.com/api/v1/guest/category/products-with-filters'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.91mobiles.com/phonefinder.php',
    'X-Requested-With': 'XMLHttpRequest'
}

all_data = []

# Fetch rows 0 up to 4800, stepping by 20
for start_row in range(0, 4800, 20):
    print(f"Fetching phones from row {start_row} to {start_row + 20}...")

    params = {
        'startRow': start_row,
        'catId': '553',
        'currentPath': '/phonefinder.php',
        'pageType': 'ListPage',
        'filters[rngFl][product_status.price.wap][]': '0-300000',
    }

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            page_data = response.json()

            # SAFETY SWITCH: Check if the 'products' string is totally empty
            if not page_data.get("products") or page_data.get("products").strip() == "":
                print("No more phones found! Reached the end of the database.")
                break  # This instantly stops the loop

            all_data.append(page_data)

        else:
            print(f"Blocked by server! Status code: {response.status_code}")
            break  # Stop looping if we get blocked so we don't lose our progress

    except Exception as e:
        print(f"A connection error occurred: {e}")
        break

    # Crucial: Wait 2 seconds so they don't block your IP address
    time.sleep(2)

# Save the massive list to your computer
print("\nSaving data to file...")
with open("all_phones_data.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=4)

print(f"Complete! Saved {len(all_data)} pages (roughly {len(all_data) * 20} phones) to JSON.")