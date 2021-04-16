import requests
from bs4 import BeautifulSoup
import re
import datetime

URL_REGEX = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"


def base64(num: int):
    result = ""
    while True:
        remainder = num % 64
        num = num // 64

        if remainder < 9:
            result += str(remainder)
        elif remainder < 36:
            result += chr(remainder + 55)
        else:
            result +=chr(remainder + 60)
        if num == 0:
            break
    return result


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
    
    def create_shortcut(self):
        link = self.link
        form = "%d%m%H%M%S%f"
        time = datetime.datetime.now()
        year = str(int(time.strftime("%Y")) - 2020)
        time = year + time.strftime(form)
        time = int(time)
        return base64(time)

