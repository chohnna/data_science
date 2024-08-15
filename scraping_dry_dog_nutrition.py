import requests
from bs4 import BeautifulSoup
import pandas as pd

def read_urls_from_file(filename):
    brand_urls = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split(' - ')
            brand_urls.append((parts[0].strip(), parts[1].strip()))  # Append tuple of (brand name, URL)
    return brand_urls

# Read URLs and corresponding brand names from file
filename = 'dog_food_brand_urls.txt'
brand_urls = read_urls_from_file(filename)

# List to hold all the nutritional data dictionaries
all_nutritional_data = []

# Headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Loop through each brand and URL
for brand_name, url in brand_urls:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # This will raise an HTTPError for bad responses

    soup = BeautifulSoup(response.text, 'html.parser')

    nutritional_data = {
        "Brand": brand_name,
        "Protein": "",
        "Fat": "",
        "Carbs": ""
    }

    # Find all 'dfpd-enc-data' rows
    rows = soup.find_all('tr', class_='dfpd-enc-data')
    for row in rows:
        cells = row.find_all('td')
        method = cells[0].text.strip()
        if 'guaranteed analysis' in method.lower() and len(cells) >= 4:
            nutritional_data['Protein'] = cells[1].text.strip()
            nutritional_data['Fat'] = cells[2].text.strip()
            nutritional_data['Carbs'] = cells[3].text.strip() if cells[3].text.strip() != 'NA' else "Not Available"

    all_nutritional_data.append(nutritional_data)

# Save all data to CSV
df = pd.DataFrame(all_nutritional_data)
df.to_csv('nutritional_data.csv', index=False)

print("Data saved to 'nutritional_data.csv'")
