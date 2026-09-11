import json
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd  # Optional: for exporting to Excel/CSV

# 1. Load the JSON file
with open("all_phones_data.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

brand_name = []
performance = []
storage = []
back_camera = []
front_camera = []
battery = []
display = []
anTuTu_score = []
price = []



# 2. Loop through each page fetched
for page in pages:
    # Get the raw HTML string stored inside the "products" key
    html_content = page.get("products", "")

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    for product in soup.find_all('article', class_='listing'):
        header = product.find('div', class_='widget_lst_head')
        if header:
            h2_tag = header.find('h2', class_='check-closest')
            if h2_tag and h2_tag.find('a'):
                brand_name.append(h2_tag.find('a').text.strip())
            else:
                brand_name.append(np.nan)

        phone_list = product.find('ul', class_='spec_hgt')
        if phone_list:
            if phone_list.find('li', class_='icn_performance'):
                performance.append(phone_list.find('li', class_='icn_performance').text.strip())
            else:
                performance.append(np.nan)

            if phone_list.find('li', class_='icn_storage'):
                storage.append(phone_list.find('li', class_='icn_storage').text.strip())
            else:
                storage.append(np.nan)

            if phone_list.find('li', class_='icn_camera'):
                back_camera.append(phone_list.find('li', class_='icn_camera').text.strip())
            else:
                back_camera.append(np.nan)

            if phone_list.find('li', class_='icn_frontcamera'):
                front_camera.append(phone_list.find('li', class_='icn_frontcamera').text.strip())
            else:
                front_camera.append(np.nan)

            if phone_list.find('li', class_='icn_battery'):
                battery.append(phone_list.find('li', class_='icn_battery').text.strip())
            else:
                battery.append(np.nan)

            if phone_list.find('li', class_='icn_display'):
                display.append(phone_list.find('li', class_='icn_display').text.strip())
            else:
                display.append(np.nan)

            if phone_list.find('li', class_='icn_antutuscore'):
                anTuTu_score.append(phone_list.find('li', class_='icn_antutuscore').text.strip())
            else:
                anTuTu_score.append(np.nan)
        else:
            brand_name.append(np.nan)
            performance.append(np.nan)
            storage.append(np.nan)
            back_camera.append(np.nan)
            front_camera.append(np.nan)
            battery.append(np.nan)
            display.append(np.nan)
            anTuTu_score.append(np.nan)

        price_tag = product.find('span', class_='store_prc')
        if price_tag:
            price.append(price_tag.text.strip())
        else:
            price.append(np.nan)



df = pd.DataFrame({
    'brand_name':brand_name,
    'processor':performance,
    'storage':storage,
    'back_camera':back_camera,
    'fron_camera':front_camera,
    'battery':battery,
    'display':display,
    'anTuTu_score':anTuTu_score,
    'price':price
})

df.to_csv("final_ds.csv", index=False)
print("completed")