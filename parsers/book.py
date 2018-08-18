from locators.book_locators import BookLocators
import re


class BookParser:

    RATINGS = {
        'One' : 1,
        'Two' : 2,
        'Three' : 3,
        'Four' : 4,
        'Five' : 5
    }

    def __init__(self,parent):
        self.parent = parent

    def __repr__(self):
        return f'{self.title} : £{self.price}, {self.rating} stars'

    @property
    def title(self):
        locator = BookLocators.TITLE_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return float(matcher.group(1))

    @property
    def stock(self):
        locator = BookLocators.IN_STOCK_LOCATOR
        return self.parent.select_one(locator).string

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes =  star_rating_tag.attrs['class'] # ['star rating', 'Three']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])  # None if not found
        # return rating_classes[0]
        return rating_number

