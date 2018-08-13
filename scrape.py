import json
import urllib.request

import bs4


def get_title_urls(n_pages):
    urls = []
    base_domain = 'http://multitrack.eecs.qmul.ac.uk/'
    for page_num in range(1, n_pages + 1):
        sauce = urllib.request.urlopen(base_domain + '/?page={0}'.format(page_num)).read()
        soup = bs4.BeautifulSoup(sauce, 'lxml')

        all_urls_on_page = []
        for url in soup.find_all('a'):
            all_urls_on_page.append(url)

        for url in all_urls_on_page:
            href = url.get('href')
            if href and "query=title" in href:
                urls.append(base_domain + url.get('id'))

    return urls


def main():
    json_path = 'urls.json'
    regenerate_title_urls = True

    if regenerate_title_urls:
        with open(json_path, 'w') as outfile:
            urls = get_title_urls(24)
            json.dump(urls, outfile)
    else:
        with open(json_path) as json_file:
            urls = json.load(json_file)


if __name__ == "__main__":
    main()
