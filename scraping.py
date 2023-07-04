import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

# urls = ['https://infocosevi.co.cr/','https://www.google.com/','https://cocinaparati.club/products/dt517015-black?...']
urls = ['https://infocosevi.co.cr/']

def scrape_links(tag):

  # print(tag)
  #scrape the links 
  html = str(tag)
  # print(tag)
  soup1 = BeautifulSoup(html, 'html.parser')
  script_tag = soup1.find('script')
  src_link = script_tag['src']
  print(src_link) 
  string_src_link = str(src_link) 

  if(string_src_link[0]!='/'):

    domain = re.findall(r"://([^/]+)/?", src_link)
    #domain found to add to files

    if domain:

     domain = domain[0]
     print(domain) 
     r1 = requests.get(src_link) 
     html_c = r1.content 
     soup2 = BeautifulSoup(html_c, 'html.parser')
     response = requests.get(src_link)
     js_content = response.text

     with open(f"{domain}.js",'w') as f_1:
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

                            f2.write(script_content + '\n') 

                        else:

                          scrape_links(script_tag)    


            except (requests.RequestException, IOError) as e:
                print(f"Failed to fetch content for {url}: {e}")
                continue
