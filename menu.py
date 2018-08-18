from app import books


USER_CHOICE = ''' Enter one of the following

- 'b' to look at 5-star rating books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the page
- 'q' to quit

Enter your choice: '''


def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


book_generator = (x for x in books)


def get_next_book():
    print(next(book_generator))


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}


def menu():
    user_input = input(USER_CHOICE)

    while user_input != 'q':
        if user_input in ('b','c', 'n'):
            user_choices[user_input]() # new topic to learn
        else:
            print('Please choose a valid command.\n')

        user_input = input(USER_CHOICE)


menu()