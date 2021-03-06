from collections import namedtuple
import requests
from bs4 import BeautifulSoup

Document = namedtuple('Document', ['filename', 'link', 'title'])


def get_next_page(page):
    if page.find('li', {'class': "pager-next"}):
        if page.find('li', {'class': "pager-next"}).find('a'):
            return page.find('li', {'class': "pager-next"}).find('a').get('href')


def get_page_content(url, attempts=3):
    if attempts < 0:
        raise Exception('No attempts')

    response = requests.get(url)
    if not response.ok:
        return get_page_content(url, attempts - 1)

    return BeautifulSoup(response.content, 'html.parser')


class GetDocFromPage:
    def __init__(self, soup):
        self.soup = soup
        self.date, self.links = self.get_document_links(self.soup)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.links)-1:
            raise StopIteration
        link = self.links[self.index].find('a', {'class': "field-content"}).get('href')
        title = self.links[self.index].find('span', {'class': "field-content"}).text
        filename = link.split('/')[-1]
        self.index += 1
        return Document(filename, link, title)

    @staticmethod
    def get_document_links(soup):
        links = soup.findAll('div', {'class': "views-field views-field-title"})
        dates = soup.findAll('span', {'class': "date-display-single"})
        return dates, links


class GetKmrDocuments:
    def __init__(self, url='https://kmr.gov.ua/uk/stenogramu'):
        self.url = url
        self.docs = []
        while url:
            page = get_page_content(url)
            self.docs.append(GetDocFromPage(page))
            url = get_next_page(page)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.docs)-1:
            raise StopIteration
        doc = self.docs[self.index]
        self.index += 1
        return doc
