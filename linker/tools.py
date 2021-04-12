import requests
from bs4 import BeautifulSoup
import re

URL_REGEX = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"


class Link:
    def __init__(self, link):
        self.link = link

    @staticmethod
    def link_normalize(link):
        compiled_pattern = re.compile(URL_REGEX)
        result = re.match(pattern=compiled_pattern, string=link)
        if result:
            req = requests.get(link)
            if req.ok:
                return link
            return None
        else:
            return None

    def get_title(self):
        link = self.link
        link_page_content = requests.get(link).content
        soup = BeautifulSoup(link_page_content, 'html.parser')
        return str(soup.title.string)


link = Link(link="https://www.google.com/")
print(type(link.get_title()))
print(Link.link_normalize("https://www.google.com/"))
