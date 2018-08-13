from bs4 import BeautifulSoup

from locators.book_page_locators import BooksPageLocators
from parsers.book import BookParser


class BooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = BooksPageLocators.BOOKS
        books = self.soup.select(locator)
        # return books
        return [BookParser(b) for b in books]