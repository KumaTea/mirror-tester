import sys
import requests
from bs4 import BeautifulSoup


# Get all files in an url
def recurse_search(url):
    sys.stdout.write("\rSearching: {}".format(url))
    files = []

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for tr in soup.find_all('tr'):
        is_file = False
        is_dir = False
        link = ''
        link_text = ''
        size_str = ''
        no_size = False
        has_slash = False
        for td in tr.find_all('td'):
            if td.get('class') == ['size'] and ('KiB' in td.text or 'MiB' in td.text):
                is_file = True
                size_str = td.text
                break
            elif td.get('class') == ['size'] and td.text == '-':
                no_size = True
            elif td.get('class') == ['link'] and td.text.endswith('/'):
                has_slash = True
        is_dir = no_size and has_slash

        for td in tr.find_all('td'):
            if td.get('class') == ['link']:
                if td.find('a').get('href'):
                    link = td.find('a').get('href')
                    link_text = td.find('a').text
        if link and link_text:
            if is_file:
                assert size_str
                files.append((url + link, size_str))
            elif is_dir:
                if '..' not in link and 'parent' not in link_text.lower():
                    files.extend(recurse_search(url + link))
    return files
