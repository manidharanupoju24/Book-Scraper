import requests

from pages.books_page import BooksPage

page_content = requests.get('http://books.toscrape.com').content

page = BooksPage(page_content)

books = page.books

for page_num in range(2,page.page_count):  # multiple pages
    url = f'http://books.toscrape.com/catalogue/page-{page_num}.html'
    page_content = requests.get(url).content
    page = BooksPage(page_content)
    books.extend(page.books)
