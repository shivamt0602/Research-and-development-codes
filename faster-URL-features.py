import pandas as pd
import ipaddress
import re
import urllib.request
from bs4 import BeautifulSoup
import socket
import requests
from urllib.parse import urljoin, urlparse 
from urllib3.exceptions import NameResolutionError

list_url = []
list_len = []
list_ip = []
list_short = []
list_at = []
list_dslash = []
list_prefix_suffix = []
list_standard_port = []
list_ctld = []
list_https_in_domain = []
list_check_sensitive = []
list_has_tilde = []
list_has_port = []

def generateCSV():

    data = {
        'URL': list_url,
        'Length of URL': list_len,
        'Has IP address': list_ip,
        'Shortening Service': list_short,
        'Having @ Symbol' : list_at,
        'Double Slash Redirecting' : list_dslash,
        'Prefix-Suffix' : list_prefix_suffix,
        'Standard Port' : list_standard_port,
        'CTLD': list_ctld,
        'HTTPS in Domain': list_https_in_domain, 
        'Sensitive Words': list_check_sensitive,
        'Has Tilde': list_has_tilde,
        'Has Port': list_has_port
    }

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)

    # Write the DataFrame to a CSV file
    df.to_csv('Faster-URL-Feature-Extracted.csv', index=False)


def url_length(url):

    if (len(url) < 54):
        #legitimate 
        return 1

    elif (54 <= len(url) <= 75):
        # suspicious
        return 0

    else:
        # phishy
        return -1 
    
def domain_is_ip(url):

    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    try:
        ipaddress.ip_address(domain) 
        return -1
    
    except:
        return 1 
    
def is_shortening_services(url):

    match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                      'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                      'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                      'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                      'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                      'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                      'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|tr\.im|link\.zip\.net',
                      url)
    if match:
        return -1
    
    else:
        return 1 
    

def is_at_symbol(url):

    if re.findall("@", url):
        return -1

    else:
        return 1    
    

def redirecting_slash(url):

    if url.startswith("HTTP") or url.startswith("http"):
        double_slash_position = url.find("//", 7)

    elif url.startswith("HTTPS") or url.startswith("https"):
        double_slash_position = url.find("//", 8) 


    if double_slash_position > 7:#phishing
        return -1
    else:#legitimate
        return 1 
    
    
def check_dash(url):

    parsed_url = urlparse(url)
    domain = parsed_url.netloc 

    if("-" in domain):#phishy
        return -1 
    
    else:# legitimate
        return 1
        

def check_StandardPort(url):
    parsedURL = urlparse(url)

    # Extract the port number from the URL
    port = parsedURL.port
        # Check if the port number is in the list of standard ports
    standard_ports_open = [80, 443]
    standard_ports_closed = [21, 22, 23, 445, 1433, 1521, 3306, 3389]

    if port in standard_ports_open:
        # The port is OPEN and standard, consider it phishing
        return -1

    elif port in standard_ports_closed:
        # The port is CLOSED and standard, consider it legitimate
        return 1

    else:
        # The port is neither standard nor open, consider it suscpicious
        return 0


def checkForCTLD(url):
    try:
        # Remove "www." from the URL
        parsed_url = urlparse(url)
        domain_parts = parsed_url.netloc.split('.')

        cctld = domain_parts[-1] if len(domain_parts) > 1 else ''

        known_cctlds = {"uk", "us", "ca", "au", "fr", "eu","in","cn", "tk", "de", "nl","ru","jp","kr","pl","gr","cz","hu","it","es"} # Add more ccTLDs as needed

        if cctld in known_cctlds:
            domain_parts = domain_parts[:-1]
        
        domain = '.'.join(domain_parts) if domain_parts else parsed_url.netloc
        domain = domain.replace("www.", "")
        
        dotCount = domain.count(".")
        
        # Classify the URL based on the number of dots
        if dotCount == 1:
            return 1
        
        elif dotCount == 2:
            return 0
        
        else:
            return -1
        
    except Exception as e:
        # Handle any exceptions or errors during URL classification
        print("Error occurred during URL classification:", e)
        return -999


def checkForHTTPSInDomain(url):
    parsedURL = urlparse(url)
    domain = parsedURL.netloc

    if ("https" in domain or "HTTPS" in domain) or ('http' in domain or 'HTTP' or domain):
        return -1
    
    else:
        return 1


def getNumberOfSubDomain(url):
    parsedURL = urlparse(url)
    subdomain = parsedURL.hostname.split('.')
    num_levels = len(subdomain) - 1  # Subtract 1 for the root domain
    return num_levels

def checkSensitiveWords(url):
    sensitive_words = ['secure', 'account', 'webscr', 'login', 'ebayisapi', 'signin', 'banking', 'confirm']

    for word in sensitive_words:
        if word in url.lower():  # Convert the URL to lowercase for case-insensitive matching
            # if present then classify url as phishy
            return -1
        
    # if not present then classify url as legitimate
    return 1


def checkTilde(url):
    # Check if the URL contains a tilde character, if present then classify it as phishing
    if "~" in url:
        return -1
    
    # If not present then classify it as legitimate
    else:
        return 1


def numberOfDots_inURL(url):
    # Extract the domain from the URL
    parsedURL = urlparse(url)
    domain = parsedURL.netloc

    # Count the number of dots in the domain
    dotCount = domain.count(".")

    # Classify the URL based on the number of dots
    if dotCount == 1:
        return 1
    
    elif dotCount == 2:
        return 0
    
    else:
        return -1


def isHyphenThere(url):
    # Extract the domain from the URL
    parsedURL = urlparse(url)
    domain = parsedURL.netloc

    # Check if the domain contains a hyphen
    if "-" in domain:
        # If present then classify it as phishing
        return -1
    
    else:
        # If not present then classify it as legitimate
        return 1
    
    
def checkForPort(url):
    parsedURL = urlparse(url)
    # If the port is present in the parsed URL then return 1
    if(parsedURL.port):
        return 1
    
    else:
        return -1;

def beginProcess(url):

    # 0: Append the url also in the csv file
    list_url.append(url)

    # 1: Length of URL
    len_of_url = int(url_length(url))
    list_len.append(len_of_url)

    # 2: IP address in URL
    ip_in_domain = int(domain_is_ip(url))
    list_ip.append(ip_in_domain)

    # 3: Shortening Services in URL
    shortening_services = int(is_shortening_services(url))
    list_short.append(shortening_services)

    # 4: @ symbol in URL
    at_symbol = int(is_at_symbol(url))
    list_at.append(at_symbol) 
    
    # 5: Double slash in URL
    dslash_position = int(redirecting_slash(url))
    list_dslash.append(dslash_position)   

    # 6: prefix-suffix in URL
    prefix_suffix = int(check_dash(url))
    list_prefix_suffix.append(prefix_suffix) 
    
    # 7: Does URL have standard port
    standard_port = int(check_StandardPort(url))
    list_standard_port.append(standard_port)

    # 8: check for country code
    ctld = int(checkForCTLD(url))
    list_ctld.append(ctld)

    # 9: Check for https in domain (if https present in domain name-->phishy)
    httpsInDomain = int(checkForHTTPSInDomain(url))
    list_https_in_domain.append(httpsInDomain)

    # 10: Check for sensitive words in the URL
    checkSensitive = int(checkSensitiveWords(url))
    list_check_sensitive.append(checkSensitive)

    # 11: check if the URL has tilde
    hasTilde = int(checkTilde(url)) 
    list_has_tilde.append(hasTilde)

    # 12: Check if the URL has port
    hasPort = int(checkForPort(url))
    list_has_port.append(hasPort)

    # 12: Match the domain of favicon and URL
    # favicon = int(checkForFavicon(url))
    # list_match_favicon.append(favicon)


if __name__ == '__main__':
    
    # Replace 'your_file_path.xlsx' with the actual path to your Excel file
    # ExcelFilePath = '/home/administrator/Desktop/Phishing-Verification/Phase-1 (Web Scrapping and Data collection)/DatasetPreparation/Legitimate-Data.xlsx'
    
    ExcelFilePath = '/home/administrator/Desktop/Phishing-Verification/Phase-1 (Web Scrapping and Data collection)/DatasetPreparation/Phishy-Data.xlsx'

    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(ExcelFilePath) 

    set_of_urls = set()

    count = 0
    # Iterate through the DataFrame and print URLs for rows with 'Status Code' equal to 200
    for index, row in df.iterrows():
        url = row['URL']

        if url not in set_of_urls:
            set_of_urls.add(url)
            if row['Status Code'] == 200:

                # For cross-checking
                with open("urls_in_excel.txt","a") as f:
                    f.write(row['URL'] + "\n") 
                    f.write(f"{count}"+"\n")
                    f.write("--------------------------------------"+"\n")

                print(count)
                count+=1
                beginProcess(row['URL'])

    generateCSV()        
