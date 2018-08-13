import json
import urllib.request

import bs4
import requests


def mock_http(url_id):
    url = "http://multitrack.eecs.qmul.ac.uk/search_linked"

    querystring = {"query": "title", "id": url_id}

    headers = {  # copied from a real browser request (in Chrome), probably not all necessary for functionality
        'dnt': "1",
        'accept-encoding': "gzip, deflate",
        'accept-language': "en-US,en;q=0.9",
        'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36",
        'content-type': "application/json",
        'accept': "application/json",
        'referer': "http://multitrack.eecs.qmul.ac.uk/search?query=title&id=2",
        'x-requested-with': "XMLHttpRequest",
        'connection': "keep-alive",
        'cache-control': "no-cache",
        'postman-token': "5417c086-edb4-8039-bf5c-2154a72e6e5b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response = json.loads(response.text)
    return response


def get_title_urls(n_pages):
    ids = []
    base_domain = 'http://multitrack.eecs.qmul.ac.uk/'
    for page_num in range(1, n_pages + 1):
        sauce = urllib.request.urlopen(base_domain + '/?page={0}'.format(page_num)).read()
        soup = bs4.BeautifulSoup(sauce, 'lxml')

        all_urls = []
        for url in soup.find_all('a'):
            all_urls.append(url)
            href = url.get('href')
            if href and "query=title" in href:
                ids.append(url.get('id'))

    return ids


def main():
    json_path = 'url_ids.json'
    regenerate_title_urls = False

    if regenerate_title_urls:
        with open(json_path, 'w') as outfile:
            url_ids = get_title_urls(24)
            json.dump(url_ids, outfile)
    else:
        with open(json_path) as json_file:
            url_ids = json.load(json_file)

    for url_id in url_ids:
        mock_http(url_id)


if __name__ == "__main__":
    main()
