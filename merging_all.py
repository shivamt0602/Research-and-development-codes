import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import requests
from urllib.parse import urlparse
from urllib.parse import urljoin
import re

# driver path (chrome driver), in ubuntu
driverPath = "/home/shivam/Desktop/selenium_Drivers/folder_cd/chromedriver"

# create a new Chrome browser instance
options = webdriver.ChromeOptions()
# headless mode: run Chrome in the background
options.add_argument("--headless")
# disable-gpu: disable the GPU hardware acceleration
options.add_argument("--disable-gpu")
# no-sandbox: disable the Chrome sandbox
options.add_argument("--no-sandbox")
# disable-dev-shm-usage: disable the /dev/shm usage
options.add_argument("--disable-dev-shm-usage")

# Set up new Chrome browser instance
browser = webdriver.Chrome(service=Service(executable_path=driverPath), options=options)
browser.maximize_window() 

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

def create_directory(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    directory = os.path.join(os.getcwd(), domain)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def scrape_links(curr_url, src_link, directory): 
    
    if curr_url in src_link:
        print('Yes, present')  # It works, further processing
        response = requests.get(src_link, headers=headers)
        js_content = response.text
        filename = src_link.split("/")[-1].replace(".js", "") + ".js"
        filepath = os.path.join(directory, 'javascript', filename)

        with open(filepath, 'w') as f:
            f.write(js_content) 

             
            
def scrape_css(curr_url, href_link, directory):

    if curr_url in href_link:
        print('Yes, present')  # It works, further processing
        response = requests.get(href_link, headers=headers)
        css_content = response.text
        filename = href_link.split("/")[-1].replace(".css", "") + ".css"
        filepath = os.path.join(directory, 'CSS', filename)
        with open(filepath, 'w') as f:
            f.write(css_content)

def scrape_images(curr_url, img_src, directory):
    response = requests.get(img_src, headers=headers)
    if response.status_code == 200:
        img_content = response.content
        filename = img_src.split("/")[-1]
        filepath = os.path.join(directory, 'images', filename)
        with open(filepath, 'wb') as f:
            f.write(img_content)




def begin_process(urls):
    for landing_page_url in urls:
        try:
            r = requests.get(landing_page_url, headers=headers)
            r.raise_for_status()
            html_content = r.content
            soup = BeautifulSoup(html_content, 'html.parser')
            parent_directory = create_directory(landing_page_url)
            html_directory = os.path.join(parent_directory, 'HTML')
            javascript_directory = os.path.join(parent_directory, 'javascript')
            css_directory = os.path.join(parent_directory, 'CSS')
            images_directory = os.path.join(parent_directory, 'images')

            if not os.path.exists(html_directory):
                os.makedirs(html_directory)

            if not os.path.exists(javascript_directory):
                os.makedirs(javascript_directory)

            if not os.path.exists(css_directory):
                os.makedirs(css_directory)

            if not os.path.exists(images_directory):
                os.makedirs(images_directory)

            with open(os.path.join(html_directory, 'landing_page.html'), 'w', encoding='utf-8') as f:
                f.write(soup.prettify())

            script_tags = soup.find_all('script')

            with open(os.path.join(parent_directory, 'script_tags_file.js'), 'a', encoding='utf-8') as f:
                for script_tag in script_tags:
                    script_content = script_tag.string
                    if script_content:
                        f.write(script_content + '\n')
                    else:
                        src_link = script_tag.get('src')
                        if src_link:
                            print("Start of the src is:", src_link[0])
                            print("And the URL is:", src_link)
                            scrape_links(landing_page_url, src_link, parent_directory)
                        else:
                            print("No src attribute found in script tag.")

            css_tags = soup.find_all('link', rel='stylesheet')

            for css_tag in css_tags:
                href_link = css_tag.get('href')
                if href_link:
                    print(href_link)
                    scrape_css(landing_page_url, href_link, parent_directory)

            img_tags = soup.find_all('img')

            for img_tag in img_tags:
                img_src = img_tag.get('src')
                if img_src:
                    print(img_src)
                    scrape_images(landing_page_url, img_src, parent_directory)

        except requests.RequestException as e:
            print(f"Failed to fetch content for {landing_page_url}: {e}")
        except Exception as e:
            print(f"An error occurred while processing {landing_page_url}: {e}")

if __name__ == "__main__":

    # newCounter = 200
    # recursiveCount = 0

    for pageNo in range(1):
        # Send a GET request to the webpage and get the HTML content
        mainPage_URL = f"https://phishtank.org/phish_search.php?page={pageNo}&active=y&valid=y&Search=Search"
        browser.get(mainPage_URL)

        # Wait for the table to be present on the page
        table_present = EC.presence_of_element_located((By.CLASS_NAME, "data"))
        WebDriverWait(browser, 10).until(table_present)

        # Parse the HTML content using BeautifulSoup, driver.page_source is the HTML content of the page
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # Find the table that contains the data
        table = soup.find("table", {"class": "data"})

        # Get the rows in the table
        rows = table.find_all("tr")

        # List of the phishing URLs
        phishingURLs = []

        # Loop row each row in the table
        for row in rows[1:]:
            cells = row.find_all("td")

            # Extract the Phish_ID
            phish_id = cells[0].text.strip()

            # Send a GET request to the webpage and get the HTML content
            phishID_URL = f"https://phishtank.org/phish_detail.php?phish_id={phish_id}"
            browser.get(phishID_URL)

            # Parse the HTML content using BeautifulSoup, driver.page_source is the HTML content of the page
            newSoup = BeautifulSoup(browser.page_source, "html.parser")

            # The required URL of the phishy page is enclosed in a span element with style attribute as 'word-wrap:break-word;'
            spanElement = newSoup.find('span', style='word-wrap:break-word;')
            if spanElement is not None:
                requiredElement = spanElement.find('b')

                if requiredElement is not None:
                    phishyURL = requiredElement.text.strip()
                    print(f"Phishy URL: {phishyURL}")
                    # Append the phishy URL to the list
                    phishingURLs.append(phishyURL)

        begin_process(phishingURLs)

        # Go back to the previous page
        browser.back()
        # Wait for 5 seconds before moving to the next page
        time.sleep(5)

    browser.quit()