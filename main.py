from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open Google Images
    driver.get('https://images.google.com')

    # Find the search box and enter the search term
    search_box = driver.find_element(By.NAME, 'q')
    search_term = 'kittens'
    search_box.send_keys(search_term + Keys.RETURN)

    # Wait for the search results to load
    time.sleep(2)

    # Scroll down to load more images
    for _ in range(5):  # Adjust the range for more/less scrolling
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

    # Find image elements
    image_elements = driver.find_elements(By.CLASS_NAME, 'YQ4gaf')

    # Extract the URLs
    image_urls = []
    for image in image_elements:
        src = image.get_attribute('src')
        if src:
            image_urls.append(src)
        else:
            src = image.get_attribute('data-src')
            if src:
                image_urls.append(src)

    # Print the image URLs
    for url in image_urls:
        if url.startswith("http"):
            print(url)

finally:
    # Close the WebDriver
    driver.quit()
