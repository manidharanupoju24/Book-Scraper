from locators.book_locators import BookLocators
import re
import logging

logger = logging.getLogger('scraping.book')

class BookParser:

    RATINGS = {
        'One' : 1,
        'Two' : 2,
        'Three' : 3,
        'Four' : 4,
        'Five' : 5
    }

    def __init__(self,parent):
        logger.debug(f'New book parser created from `{parent}`')
        self.parent = parent

    def __repr__(self):
        return f'{self.title} : £{self.price}, {self.rating} stars'

    @property
    def title(self):
        logger.debug('Finding book name...')
        locator = BookLocators.TITLE_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        logger.debug(f'Found book name title as `{item_name}`')
        return item_name

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        float_price = float(matcher.group(1))
        logger.debug(f'Found book price as `{float_price}`')
        return float_price

    @property
    def stock(self):
        logger.debug('Finding if in stock...')
        locator = BookLocators.IN_STOCK_LOCATOR
        item_in_stock = self.parent.select_one(locator).string
        logger.debug(f'Found in_stock as `{item_in_stock}`')
        return item_in_stock

    @property
    def rating(self):
        logger.debug('Finding rating...')
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes =  star_rating_tag.attrs['class'] # ['star rating', 'Three']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])  # None if not found
        # return rating_classes[0]
        logger.debug(f'Found rating as `{rating_number}` stars.')
        return rating_number

