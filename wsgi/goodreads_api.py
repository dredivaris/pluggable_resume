from goodreads import client

from wsgi.models import Book
import requests
from lxml import html


class GoodreadsClient:

    def __init__(self, key, secret, oauth_access_token, oauth_secret, user_id):
        self.gc = client.GoodreadsClient(key, secret)
        self.gc.authenticate(oauth_access_token, oauth_secret)
        self.user = self.gc.user(user_id)

    def list_shelves_by_name(self):
        return [shelf['name'] for shelf in self.user.shelves()]

    def get_books_for_shelf(self, shelf_name):
        books = self.user.shelf(shelf_name)
        for doc in books:
            book_record = self.gc.book(doc['book']['id']['#text'])

            if 'nophoto' in book_record.image_url:
                try:
                    page = requests.get(book_record.link).text
                    doc = html.fromstring(page)
                    image_url = doc.get_element_by_id('coverImage').get('src')
                except:
                    image_url = book_record.image_url
            else:
                image_url = book_record.image_url

            book = Book(
                goodreads_id=int(doc['book']['id']['#text']),
                isbn=str(doc['book']['isbn']),
                isbn13=str(doc['book']['isbn13']),
                title=doc['book']['title'],
                image_url=image_url,
                small_image_url=book_record.small_image_url,
                link=book_record.link,
                num_pages=book_record.num_pages,
                publisher=book_record.publisher,
                average_rating=book_record.average_rating,
                description=book_record.description,
                authors=[a.name for a in book_record.authors],
                rating=doc['rating'],
                started_at=doc['started_at'],
                read_at=doc['read_at'],
                date_added=doc['date_added'],
                date_updated=doc['date_updated'],
            )
            if doc['body']:
                book.review_body = doc['body']

            yield book
