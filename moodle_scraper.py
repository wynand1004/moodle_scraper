import requests
from bs4 import BeautifulSoup

class Moodle(object):

    def __init__(self, url, username, password):
        self.url = url
        self.login_url = "{}{}".format(self.url, "login/index.php")
        self.session = requests.Session()
        self.session.headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"
        self.payload = {'username': username, 'password': password}
        
        # Login
        p = self.session.post(self.login_url, data=self.payload)
        soup = BeautifulSoup(p.text, "html.parser")
        print(soup.title.string)       

    def get_soup(self, text):
        """Converts HTML text into a BeautifulSoup object"""
        soup = BeautifulSoup(text, "html.parser")
        return soup

    def get_page_soup(self, path):
        """Returns a BeautifulSoup object from the given relative path"""
        response = self.session.get('{}{}'.format(self.url, path)) 
        soup = self.get_soup(response.text)
        return soup