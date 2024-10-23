import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode

driver = uc.Chrome(options=chrome_options)

driver.get("https://www.higheredjobs.com/faculty/search.cfm?JobCat=62")

logging.info(driver.page_source)

# get all the links
links = driver.find_elements(By.TAG_NAME, "a")
urls = [link.get_attribute("href") for link in links]
# filter URLs to those that have "details.cfm?JobCode=" in them
urls = [url for url in urls if url and "details.cfm?JobCode=" in url]
logging.info(f"Number of URLs found: {len(urls)}")
logging.info(f"First 5 URLs: {urls[:5]}")
# this seems to get all the URLs across all pages--not just the first page

url_job = urls[5]
driver.get(url_job)

logging.info(driver.page_source)

driver.quit()

logging.info("script run until the end")
