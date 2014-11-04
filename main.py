import os
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
import urllib2
from sites import TianYa

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def get_site():
    select = raw_input('Which website is the book from?\n1, tianya; 2, douban: ')
    if select == '1':
        site = TianYa()
        return site
    else:
        print 'this site is not supported yet'
        exit(0)

def out_put_in_chapters(urls, site):
    for i in urls:
        html = urllib2.urlopen(i).read()
        soup = BeautifulSoup(html)
        soup1 = site.get_soup(soup)
        filename = '%s/chapter_%d.txt' % (book_name, (urls.index(i) + 1))
        f = file(filename, 'w')
        text = strip_tags(str(soup1))
        f.write(text)
        f.close

def out_put_in_one(urls, site):
    filename = '%s/%s' % (book_name, book_name)
    f = file(filename, 'a')
    for i in urls:
        html = urllib2.urlopen(i).read()
        soup = BeautifulSoup(html)
        soup1 = site.get_soup(soup)
        text = strip_tags(str(soup1))
        f.write(text)
    f.close()

def get_text():
    global book_name
    book_name = raw_input('Enter name of the book: ')
    try:
        os.mkdir(book_name)
    except OSError:
        pass
    how_to_save = raw_input('How to save?\n1,in one file; 2,in chapters: ')
    if how_to_save != '1' and how_to_save != '2':
        print 'Enter 1 or 2.'
        exit(0)
    site = get_site()
    try:
        urls = site.get_urls()
    except ValueError:
        print 'Wrong URL.'
        exit(0)
    if how_to_save == '1':
        out_put_in_one(urls, site)
    else:
        out_put_in_chapters(urls, site)
    print 'done'

if __name__ == '__main__':
    get_text()
