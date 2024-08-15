import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://www.dogfoodadvisor.com/dog-food-reviews/dry/all/'

def get_reviews_with_brand_names(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all links within the specified class
    review_links = soup.find_all('div', class_='reviews-archive__review')
    
    # List to store brand names and URLs
    brand_details = []
    
    # Extract brand name and URL from each 'a' tag
    for link in review_links:
        a_tag = link.find('a')
        if a_tag and 'href' in a_tag.attrs:
            # Extract the text (brand name and product name) and the URL
            brand_name = a_tag.get_text(strip=True)
            url = a_tag['href']
            brand_details.append((brand_name, url))
    
    return brand_details

# Get the list of brand names and URLs
reviews_with_brands = get_reviews_with_brand_names(url)

# Save brand names and URLs to a text file
with open('dog_food_brand_urls.txt', 'w') as file:
    for brand_name, url in reviews_with_brands:
        file.write(f"{brand_name} - {url}\n")

print("Brand names and URLs have been saved to dog_food_brand_urls.txt")
