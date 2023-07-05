import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

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
        response = requests.get(src_link)
        js_content = response.text
        filename = src_link.split("/")[-1].replace(".js", "") + ".js"
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as f:
            f.write(js_content)

urls = ['https://infocosevi.co.cr/', 'https://www.google.com/']

for landing_page_url in urls:
    try:
        r = requests.get(landing_page_url)
        r.raise_for_status()
        html_content = r.content
        soup = BeautifulSoup(html_content, 'html.parser')
        directory = create_directory(landing_page_url)

        if(soup):
            landing_directory = create_directory(f'HTML_content')

        os.path.join(directory,landing_directory)# directory in directory

        with open(os.path.join(landing_directory, 'landing_page.html'), 'w', encoding='utf-8') as f:
            f.write(soup.prettify())

        script_tags = soup.find_all('script')

        with open(os.path.join(directory, 'script_tags_file.js'), 'a', encoding='utf-8') as f:
            for script_tag in script_tags:
                script_content = script_tag.string
                if script_content:
                    f.write(script_content + '\n')
                else:
                    tag = script_tag
                    html = str(tag)
                    soup1 = BeautifulSoup(html, 'html.parser')
                    script_tag1 = soup1.find('script')
                    src_link = script_tag1['src']
                    print(src_link)
                    scrape_links(landing_page_url, src_link, directory)

    except (requests.RequestException, IOError) as e:
        print(f"Failed to fetch content for {landing_page_url}: {e}")
