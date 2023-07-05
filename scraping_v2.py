import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import os

urls = ['https://infocosevi.co.cr/']

def scrape_links(curr_url, src_link):
    if curr_url in src_link:
        print('Yes, present')  # It works, further processing
        response = requests.get(src_link)
        js_content = response.text

        # Extract the filename from the src_link
        filename = src_link.split("/")[-1].replace(".js", "") + ".js"

        with open(filename, 'w') as f:
            f.write(js_content)

for url in urls:
    try:
        r = requests.get(url)
        r.raise_for_status()  # Check for any HTTP request errors

        html_content = r.content
        soup = BeautifulSoup(html_content, 'html.parser')

        with open('landing_page.html', 'w', encoding='utf-8') as f:
            f.write(soup.prettify())

        script_tags = soup.find_all('script')

        with open('script_tags_file.js', 'a', encoding='utf-8') as f2:
            for script_tag in script_tags:
                script_content = script_tag.string

                if script_content:
                    f2.write(script_content + '\n')
                else:
                    tag = script_tag
                    html = str(tag)
                    soup1 = BeautifulSoup(html, 'html.parser')
                    script_tag1 = soup1.find('script')
                    src_link = script_tag1['src']
                    print(src_link)

                    scrape_links(url, src_link)  # Function call

    except (requests.RequestException, IOError) as e:
        print(f"Failed to fetch content for {url}: {e}")
        continue
