import re
import logging
from bs4 import BeautifulSoup

from locators.book_page_locators import BooksPageLocators
from parsers.book import BookParser

logger = logging.getLogger('scraping.books_page')


class BooksPage:
    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML Parser.')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = BooksPageLocators.BOOKS
        logger.debug(f'Finding all books in the page using `{locator}`.')
        books = self.soup.select(locator)
        # return books
        return [BookParser(b) for b in books]

    @property
    def page_count(self):
        locator = BooksPageLocators.PAGER
        logger.debug(f'Finding catalogue page count using `{locator}`.')
        pages_count_content = self.soup.select_one(locator).string
        logger.info(f'Found number of catalogue pages available : `{pages_count_content}`.')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, pages_count_content)
        return int(matcher.group(1))