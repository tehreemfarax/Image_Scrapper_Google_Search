# Image_Scrapper_Google_Search
This Python script uses Selenium to automate the process of scraping image URLs from Google Image search results. It extracts image URLs based on a specified search term and saves them in a text file.

---

## Prerequisites

- **Python 3.x**: Make sure Python is installed.
- **Selenium**: Install using `pip install selenium`.
- **Webdriver Manager**: Install using `pip install webdriver-manager`.
- **Google Chrome**: The script is configured for Chrome, so Chrome must be installed on your machine.

## Setup

1. **Clone the Repository** (if applicable) or download the script file directly.
2. **Install Requirements**:
   ```bash
   pip install selenium webdriver-manager
   ```

## Script Overview

This script performs the following actions:

1. Opens Google Images in a Chrome browser.
2. Enters a search term (e.g., "kittens") to fetch images.
3. Scrolls through the page to load more images.
4. Collects the URLs of the images displayed on the page.
5. Prints the extracted URLs in the console.

## Usage

1. **Set Search Term**:
   Modify the `search_term` variable in the script to specify the images you want to search for.
   ```python
   search_term = 'kittens'  # Change this term as needed
   ```

2. **Run the Script**:
   Execute the script using:
   ```bash
   python google_image_scraper.py
   ```

3. **Output**:
   - The script will print each image URL in the console.
   - To save URLs in a file, redirect the output as needed.


## Important Notes

- **Rate Limiting**: Be mindful of Google’s rate limits when using this script to avoid being temporarily blocked.
- **Adjust Scroll Range**: Modify the range in the `for _ in range(5)` loop to load more or fewer images.
- **File Saving**: For large-scale scraping, consider saving URLs directly into a file, e.g., a CSV file, instead of printing them.
