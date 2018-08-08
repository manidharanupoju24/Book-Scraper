from locators.book_locators import BookLocators


class BookParser:

    def __init__(self,parent):
        self.parent = parent

    def __repr__(self):
        return f'{self.title} : {self.price}, Availability : {self.stock}'

    @property
    def title(self):
        locator = BookLocators.TITLE_LOCATOR
        return self.parent.select_one(locator).string

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        return self.parent.select_one(locator).string

    @property
    def stock(self):
        locator = BookLocators.IN_STOCK_LOCATOR
        return self.parent.select_one(locator).string

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        return self.parent.select_one(locator).string

