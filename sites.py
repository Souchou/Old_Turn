from bs4 import BeautifulSoup
import urllib2

class Site():
    def get_urls(self):
        pass

    def get_soup(self, soup):
        pass

class TianYa(Site):
    def get_urls(self):
        enter_url = raw_input('Enter Url Of The Book: ')
        html = urllib2.urlopen(enter_url).read()
        urls = []
        soup = BeautifulSoup(html)
        soup1 = soup.find('dl')
        url_got = soup1.find_all("a", href=True)
        for i in url_got:
            urls.append(enter_url + str(i['href']))
        return urls

    def get_soup(self, soup):
        soup1 = soup.find("div", id="main")
        return soup1
