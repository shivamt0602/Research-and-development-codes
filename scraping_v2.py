import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

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

urls = ['https://infocosevi.co.cr/', 'https://www.google.com/','https://jitsi.debian.social/','https://postch.site/','https://www.youtube.com/']

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

        if not os.path.exists(html_directory):
            os.makedirs(html_directory)

        if not os.path.exists(javascript_directory):
            os.makedirs(javascript_directory)

        if not os.path.exists(css_directory):
            os.makedirs(css_directory)

        with open(os.path.join(html_directory, 'landing_page.html'), 'w', encoding='utf-8') as f:
            f.write(soup.prettify())

        script_tags = soup.find_all('script')

        with open(os.path.join(parent_directory, 'script_tags_file.js'), 'a', encoding='utf-8') as f:
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
                    scrape_links(landing_page_url, src_link, parent_directory)

        css_tags = soup.find_all('link', rel='stylesheet')

        for css_tag in css_tags:
            href_link = css_tag.get('href')
            if href_link:
                print(href_link)
                scrape_css(landing_page_url, href_link, parent_directory)

    except (requests.RequestException, IOError) as e:
        print(f"Failed to fetch content for {landing_page_url}: {e}")


#inline css code