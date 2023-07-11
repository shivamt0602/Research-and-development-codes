import os
import time
from selenium import webdriver
import urllib.parse
import shutil
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import requests
from urllib.parse import urlparse
from urllib.parse import urljoin
import re
import pandas as pd

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

# File path for storing the entries
LogFIle = "LogFile.xlsx"

# Create the directory which will have all the web resources for a URL, name the directory as the PhishID
def create_directory(URL, webResource_folder, phishID):

    # Create the directory named after the PhishID
    directory = os.path.join(webResource_folder, phishID)

    # Create the directory if it does not exist at the webResource_folder create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    # return the directory
    return directory


# This function will extract the JavaScript code of the landing page
def scrape_links(curr_url, src_link, directory): 
    
    # Check if the current URL is present in the source link
    if curr_url in src_link:
        print('Yes, present')  # It works, further processing

        # Send a GET request to the source link to retrieve the JavaScript content
        response = requests.get(src_link, headers=headers, verify=False)
        JS_content = response.text

        # Extract the filename from the source link
        JSfilename = src_link.split("/")[-1].replace(".js", "") + ".js"

        # Create the full file path to save the JavaScript file
        JavaScriptFilePath = os.path.join(directory, 'JavaScript', JSfilename)

        # Open the file in write mode and write the JavaScript content
        with open(JavaScriptFilePath, 'w') as JSFile:
            JSFile.write(JS_content) 

# This function will extract the CSS code of the landing page
def scrape_css(curr_url, css_url, directory):
    absolute_css_url = urljoin(curr_url, css_url)

    # Send a GET request to download the CSS file
    css_response = requests.get(absolute_css_url)

    if css_response.status_code == 200:
        css_content = css_response.text
        filename = css_url.split("/")[-1]
        # Check if the filename already has .css extension or not, if not then add
        if not filename.endswith(".css"):
            filename += ".css"
        
        filepath = os.path.join(directory, 'CSS', filename)
                    
        with open(filepath, 'w') as f:
            f.write(css_content)
                    
        print(f"CSS file downloaded: {filename}")
    else:
        print(f"Failed to download CSS file: {absolute_css_url}")

# This function will extract the images of the landing page
def scrape_images(curr_url, directory, imageColumn):
    
    response = requests.get(curr_url, headers=headers, verify=False)

    if response.status_code == 200:
        # Parse the base URL from the given URL
        base_url = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(curr_url))
        
        # Create the output folder if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # Find all image tags in the HTML
        images = response.text.split('<img')

        for img in images[1:]:
            # Extract the image URL from the tag
            img_url = img.split('src="')[1].split('"')[0]

            # Construct the absolute image URL
            if not img_url.startswith('http'):
                img_url = base_url + img_url
            
            # Download the image
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                # Extract the image filename from the URL
                img_filename = os.path.basename(img_url)

                # Save the image to the output folder
                img_path = os.path.join(directory, 'Images', img_filename)
                with open(img_path, 'wb') as f:
                    f.write(img_response.content)
                    imageColumn = 1
                print(f"Downloaded image: {img_url}")
            
            else:
                imageColumn = 0
                print(f"Failed to download image: {img_url}")

        else:
            imageColumn = 0
            print(f"Failed to fetch HTML content from: {curr_url}")


# This function will extract the HTML code of the landing page, and also call the other functions to extract the JavaScript, CSS and images. This function will also create the directory structure for the web resources
def begin_process(landingPage_URL, phishID):

    # Variables for html, js, css, images, not_found, and forbidden columns in xlsx file
    html, js, css, images, not_found, forbidden = 0, 0, 0, 0, 0, 0

    # for landingPage_URL in urls:
    try:
        response = requests.get(landingPage_URL, headers=headers, verify=False)
        response.raise_for_status()

        html_content = response.content

        soup = BeautifulSoup(html_content, 'html.parser')

        parent_directory = create_directory(landingPage_URL, webResource_folder, phishID)

        HTML_Directory = os.path.join(parent_directory, 'HTML')
        JavaScript_Directory = os.path.join(parent_directory, 'JavaScript')
        CSS_Directory = os.path.join(parent_directory, 'CSS')
        Images_Directory = os.path.join(parent_directory, 'Images')

        if not os.path.exists(HTML_Directory):
            os.makedirs(HTML_Directory)

        if not os.path.exists(JavaScript_Directory):
            os.makedirs(JavaScript_Directory)

        if not os.path.exists(CSS_Directory):
            os.makedirs(CSS_Directory)

        if not os.path.exists(Images_Directory):
            os.makedirs(Images_Directory)

        with open(os.path.join(HTML_Directory, 'landing_page.html'), 'w', encoding='utf-8') as landingPage:
            
            if soup.prettify() is not None:
                html = 1
            else:
                html = 0

            landingPage.write(soup.prettify())


        scriptTags = soup.find_all('script')

        with open(os.path.join(JavaScript_Directory, 'Script.js'), 'a', encoding='utf-8') as scriptTags_file:

            for tag in scriptTags:
                script_content = tag.string

                if script_content:
                    scriptTags_file.write(script_content + '\n')
                    
                else:
                    src_link = tag.get('src')

                    if src_link is not None:
                        print("Start of the src is:", src_link[0])
                        print("And the URL is:", src_link)
                        
                        # Check if it is an external JavaScript file or an inline JavaScript
                        if src_link.startswith('http') or src_link.startswith('//'):
                            scrape_links(landingPage_URL, src_link, parent_directory)
                        
                        else:
                            # Write inline JavaScript code to a separate file
                            inlineJSfilename = f"inlineJS_{scriptTags.index(tag)}.js"
                            inlineJSFilePath = os.path.join(JavaScript_Directory, inlineJSfilename)
                            with open(inlineJSFilePath, 'w') as inlineJSFile:
                                inlineJSFile.write(tag.string + '\n')
                        
                    else:
                        print("No src attribute found in script tag.")

            # Check if the landing page contains any JavaScript code
            if scriptTags:
                js = "1"
            else:
                js = "0"

        # Find all <link> tags with rel='stylesheet' to extract CSS file URLs
        css_tags = soup.find_all('link', rel='stylesheet')

        for css_tag in css_tags:
            css_url = css_tag.get('href')

            if css_url:
                print(css_url)
                scrape_css(landingPage_URL, css_url, parent_directory)

        # Check for inline CSS
        inline_css = soup.find('style')

        if inline_css:
            inline_css_content = inline_css.string

            if inline_css_content:
                inline_css_filepath = os.path.join(CSS_Directory, 'inlineCSS.css')

                with open(inline_css_filepath, 'w') as inlineCSS:
                    inlineCSS.write(inline_css_content)

                print("Inline CSS file saved as inlineCSS.css")

        # check if any of the css_tags or inline_css in not empty
        if not css_tags and not inline_css:
            css = "0"
        else:
            css = "1"

        # Call the scrape_images function to download and save the image
        scrape_images(landingPage_URL, parent_directory, images)

        # Append the entry to the DataFrame
        df.loc[len(df)] = [phish_id, landingPage_URL, html or 0, js or 0, css or 0, images or 0, not_found or 0, forbidden or 0]

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            not_found = 1
        elif e.response.status_code == 403:
            forbidden = 1
        else:
            # Handle other HTTP errors if needed
            pass

        # Append the entry to the DataFrame
        df.loc[len(df)] = [phish_id, landingPage_URL, html, js, css, images, not_found, forbidden]

    except (requests.RequestException, requests.ConnectionError) as e:
        with open("logs1.txt",'a') as errors1:
            errors1.write(f"Failed to fetch content for {landingPage_URL}: {e}\n")
            
    except Exception as e:
        with open("logs2.txt", "a") as errors2:
            errors2.write(f"An error occurred while processing {landingPage_URL}: {e}\n")

            

if __name__ == "__main__":

    # Create a folder to store all the subfolders containing the web-resources
    webResource_folder = "Resources"
    current_directory = os.getcwd()


    # Check if the output file already exists
    if os.path.exists(LogFIle):
        df = pd.read_excel(LogFIle)
    else:
        df = pd.DataFrame(columns=["PhishID", "URL", "HTML", "JS", "CSS", "Images", "Not Found", "Forbidden"])

    resourcePath = os.path.join(current_directory, webResource_folder)

    if not os.path.isdir(resourcePath):
        os.makedirs(resourcePath)
        print(f"Folder created with name: {webResource_folder}")
    
    else:
        print(f"Folder already exists with name: {webResource_folder}")

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

                    begin_process(phishyURL, phish_id)

            # Save the DataFrame to the output file after each iteration
            df.to_excel(LogFIle, index=True)

        # Go back to the previous page
        browser.back()
        # Wait for 5 seconds before moving to the next page
        time.sleep(5)

    browser.quit()
