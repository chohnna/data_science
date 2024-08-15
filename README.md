# Kibble Nutritional Data Analyzer

This project scrapes nutritional data (protein and fat content) from various kibble brands and visualizes it to help dog owners find the best fit for their pets. The data is collected from provided URLs and plotted to compare different kibbles based on their nutritional content.

## Features

- **Web Scraping**: Extracts nutritional information from kibble brand websites.
- **Data Visualization**: Creates interactive plots to compare protein and fat content across different brands.
- **Interactive URLs**: Allows users to click on data points in the plot to open the corresponding kibble brand's website for more information.

## Prerequisites

- Python 3.
- `requests` for web scraping
- `beautifulsoup4` for HTML parsing
- `pandas` for data manipulation
- `matplotlib` for plotting
- `plotly` for interactive plots

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/chohnna/dry_dogfood.git

- scrape_data.py: Script for scraping nutritional data.
- plot_data.py: Script for plotting the data and making the plot interactive.
- nutritional_data.csv: CSV file storing the scraped data.
- dog_food_brand_urls.txt: Text file with brand names and their corresponding URLs.

Feel free to fork this repository and submit pull requests if you'd like to contribute to the project.