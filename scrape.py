import json
import urllib.request

import bs4
import requests
from progress.bar import Bar

from utils import dump_json, load_json


def mock_http_requests(url_ids):
    url = "http://multitrack.eecs.qmul.ac.uk/search_linked"
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

    # using a session speeds things up because we don't need a fresh HTTP connection on each request
    s = requests.Session()
    s.headers.update(headers)

    responses = {}
    bar = Bar("Mocking HTTP calls...", max=len(url_ids))
    for url_id in url_ids:
        querystring = {"query": "title", "id": url_id}
        response = s.get(url, params=querystring)
        responses[url_id] = json.loads(response.text)['0']

        bar.next()
    bar.finish()
    return responses


def get_title_urls(n_pages):
    ids = []
    base_domain = 'http://multitrack.eecs.qmul.ac.uk/'
    bar = Bar("Scraping for IDs...", max=n_pages)
    for page_num in range(1, n_pages + 1):
        sauce = urllib.request.urlopen(base_domain + '/?page={0}'.format(page_num)).read()
        soup = bs4.BeautifulSoup(sauce, 'lxml')

        all_urls = []
        for url in soup.find_all('a'):
            all_urls.append(url)
            href = url.get('href')
            if href and "query=title" in href:
                ids.append(url.get('id'))

        bar.next()

    bar.finish()
    return ids


def main():
    ids_path = 'url_ids.json'
    responses_path = 'responses.json'
    cache_ids = True
    cache_responses = True

    if cache_ids:
        url_ids = load_json(ids_path)
    else:
        url_ids = get_title_urls(24)
        dump_json(ids_path, url_ids)

    if cache_responses:
        responses = load_json(responses_path)
    else:
        responses = mock_http_requests(url_ids)
        dump_json(responses_path, responses)

    print(responses)


if __name__ == "__main__":
    main()
