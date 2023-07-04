import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

# urls = ['https://infocosevi.co.cr/','https://www.google.com/','https://cocinaparati.club/products/dt517015-black?...']
urls = ['https://infocosevi.co.cr/']

def scrape_links(curr_url,src_link):

  #these first three lines only applicable for certain js files
  # string_src_link = str(src_link) 
  # response = requests.get(src_link)
  # js_content = response.text
  if(curr_url in src_link):

    print('yes,present')# so this works , process on it further
    response = requests.get(src_link) 
    js_content = response.text 

    with open('all_src_links.js','a') as f_1:
      f_1.write(js_content)



for url in urls:

            try:
                r = requests.get(url)
                r.raise_for_status()  # Check for any HTTP request errors

                html_content = r.content
                soup = BeautifulSoup(html_content, 'html.parser')

                with open('landing_page.html', 'w', encoding='utf-8') as f:

                    f.write(soup.prettify())

                script_tags = soup.find_all('script')

                # print("all script tags are",script_tags)

                with open('script_tags_file.js', 'a', encoding='utf-8') as f2:

                    for script_tag in script_tags:
                        script_content = script_tag.string

                        if script_content:
                          # append the whole script thing to one single html script tag and then add a file name something.js
                            f2.write(script_content + '\n')

                        else:

                          tag = script_tag

                          html = str(tag)
                          # print(tag)
                          soup1 = BeautifulSoup(html, 'html.parser')
                          script_tag1 = soup1.find('script')
                          src_link = script_tag1['src']
                          print(src_link)
                          # print(src_link)
                          # string_src_link = str(src_link) 
                          # response = requests.get(src_link)
                          # js_content = response.text
                          # print(js_content)

                          scrape_links(url,src_link)#function call

            except (requests.RequestException, IOError) as e:
                print(f"Failed to fetch content for {url}: {e}")
                continue
