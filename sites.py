from bs4 import BeautifulSoup
import urllib2

class Site():
    def __init__(
                 self,
                 id,
                 name,
                 root_ele,
                 root_attr,
                 root_value,
                 link_ele,
                 link_attr,
                 link_value,
                 ele,
                 attr,
                 value,
                 son_ele,
                 son_attr,
                 son_value,
                 ):
        self.id = id
        self.name = name
        self.root_ele = root_ele
        self.root_attr = root_attr
        self.root_value = root_value
        self.link_ele = link_ele
        self.link_attr = link_attr
        self.link_value = link_value
        self.ele = ele
        self.attr = attr
        self.value = value
        self.son_ele = son_ele
        self.son_attr = son_attr
        self.son_value = son_value

    def url_selector(self):
        enter_url = raw_input('Enter Url Of The Book: ')
#         self.root_ele = None
#         self.root_attr = None
#         self.root_value = None
#         self.link_ele = None
#         self.link_attr = None
#         self.link_value = None
        return enter_url

#     def chapter_selector(self):
#         self.ele = None
#         self.attr = None
#         self.value = None

    def get_urls(self):
        root_url = self.url_selector()
        html = urllib2.urlopen(root_url).read()
        urls = []
        soup = BeautifulSoup(html)
        soup1 = soup.find_all(self.root_ele, attrs={self.root_attr:self.root_value})
        url_got = []
        for i in soup1:
            url_got.append(i.find_all(self.link_ele, attrs={self.link_attr:self.link_value}, href=True))
        for i in url_got:
            for a in i:
                urls.append(root_url + str(a['href']))
        return urls

    def get_soup(self, soup):
#         self.chapter_selector()
        soup_list = soup.find_all(self.ele, attrs={self.attr:self.value})
        if self.son_ele:
            i = []
            for item in soup_list:
                p = item.find_all(self.son_ele, attrs={self.son_attr:self.son_value})
                for a in p:
                    i.append(a)
            soup1 = i
        else:
            soup1 = soup_list
        return soup1


# class TianYa(Site):
#     def url_selector(self):
#         enter_url = raw_input('Enter Url Of The Book: ')
#         self.root_ele = "dl"
#         self.link_ele = "a"
#         return enter_url
#
#     def chapter_selector(self):
#         self.ele = "div"
#         self.attr = "id"
#         self.value = "main"
#         self.son_ele = "p"



