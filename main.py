import os
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
import urllib2
import json
from sites import Site

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

def newsite():
    print "enter rules to get text of your book, empty for 'None' for each information."
    name = raw_input('name: ')
    if name == "":
        name = None
    root_ele = raw_input('parent element of the chapter links: ')
    if root_ele == "":
        root_ele = None
    root_attr = raw_input('attr of the element: ')
    if root_attr == "":
        root_attr = None
    root_value = raw_input('value of the attr: ')
    if root_value == "":
        root_value = None
    link_ele = raw_input('element of the chapter links: ')
    if link_ele == "":
        link_ele = None
    link_attr = raw_input('attr of the element: ')
    if link_attr == "":
        link_attr = None
    link_value = raw_input('value of the attr: ')
    if link_value == "":
        link_value = None
    ele = raw_input('parent element of the chapter: ')
    if ele == "":
        ele = None
    attr = raw_input('attr of the element: ')
    if attr == "":
        attr = None
    value = raw_input('value of the attr: ')
    if value == "":
        value = None
    son_ele = raw_input('element(s) of the chapter: ')
    if son_ele == "":
        son_ele = None
    son_attr = raw_input('attr of the element: ')
    if son_attr == "":
        son_attr = None
    son_value = raw_input('value of the attr: ')
    if son_value == "":
        son_value = None
    jsonfile = open('sites.json')
    jsondata = json.load(jsonfile)
    jsonfile.close()
    sites = jsondata["sites"]
    count = len(sites)
    num = count + 1
    dic = {
                  "id":num,
                  "name": name,
                  "root_ele": root_ele,
                  "root_attr": root_attr,
                  "root_value": root_value,
                  "link_ele": link_ele,
                  "link_attr": link_attr,
                  "link_value": link_value,
                  "ele": ele,
                  "attr": attr,
                  "value": value,
                  "son_ele": son_ele,
                  "son_attr": son_attr,
                  "son_value": son_value
                  }
    sites.append(dic)
    newjson = json.dumps(jsondata)
    jsfile = open("sites.json", 'w')
    jsfile.write(newjson)
    jsfile.close()
    get_text()

def get_site():
    jsonfile = open('sites.json')
    jsondata = json.load(jsonfile)
    jsonfile.close()
    all_sites = ""
    sites = jsondata["sites"]
    for site in sites:
        all_sites += "%d:%s, " % (site["id"], site["name"])
    print all_sites
    select = raw_input('input a number in the sites to select, or enter 0 to create a new one: ')
    try:
        num = int(select)
        if num <= len(sites) and num > 0:
            sitedata = sites[num - 1]
            site = Site(**sitedata)
            return site
        elif num == 0:
            newsite()
        else:
            print 'number is not in the sites list.'
            exit(0)
    except:
        print 'enter a number in the sites list.'
        exit(0)

def out_put_in_chapters(urls, site):
    for i in urls:
        html = urllib2.urlopen(i).read()
        soup = BeautifulSoup(html)
        soup1 = site.get_soup(soup)
        filename = '%s/chapter_%d.txt' % (book_name, (urls.index(i) + 1))
        f = file(filename, 'a')
        for i in soup1:
            text = strip_tags(str(i))
            f.write(text)
        f.close()

def out_put_in_one(urls, site):
    filename = '%s/%s' % (book_name, book_name)
    f = file(filename, 'a')
    for i in urls:
        html = urllib2.urlopen(i).read()
        soup = BeautifulSoup(html)
        soup1 = site.get_soup(soup)
        for i in soup1:
            text = strip_tags(str(i))
            f.write(text)
    f.close()

def get_text():
    site = get_site()
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
