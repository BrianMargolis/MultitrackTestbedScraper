import bs4 as bs
import urllib
import json

# grab URLs of every song on a page
def getIDs(page_num):
    sauce = urllib.urlopen('http://multitrack.eecs.qmul.ac.uk/?page='+str(page_num)).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')


    all_urls = []
    relevant_urls = []
    for url in soup.find_all('a'):
        all_urls.append(url)

    for u in all_urls:
        if "query=title" in str(u.get('href')):
            relevant_urls.append(u.get('href'))

    return relevant_urls

def main():
    all_urls = []
    # for i in range(1,25):
    #     all_urls.append(getIDs(i))

    # with open('data.json', 'w') as outfile:
    #     json.dump(all_urls, outfile)
    with open('data.json') as json_file:  # This JSON file contains all of the urls needed to be scraped 
                                          # I've commented out the above code becuase all that does is generate the JSON file.
        pages = json.load(json_file)   


if __name__== "__main__":
    main()