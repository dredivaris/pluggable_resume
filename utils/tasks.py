from config import GOODREADS_DATABASE_NAME
from wsgi.exceptions import NotFoundException
from wsgi.goodreads_api import GoodreadsClient
from wsgi.models import Resume, ReadingList
from wsgi.views import app

shelves_to_pull = {'read-to-share', 'read-to-share-work', 'to-read-work', 'currently-reading-work'}
resume_mapping = {
    'read-to-share': 'finished_reading_general',
    'read-to-share-work': 'finished_reading',
    'to-read-work': 'to_read',
    'currently-reading-work': 'currently_reading'
}


def sync_bookshelves_from_goodreads(resume_model_id):
    resume = Resume.objects.get(id=resume_model_id)
    for sl in resume.service_links_list:
        if sl.name == GOODREADS_DATABASE_NAME:
            break

    gr_client = GoodreadsClient(sl.key, sl.secret, sl.oauth_key, sl.oauth_secret, sl.user_id)

    shelves = set(gr_client.list_shelves_by_name())
    if len(shelves_to_pull) != len(shelves_to_pull & shelves):
        raise NotFoundException('Error: reading list mismatch ', shelves_to_pull & shelves)

    reading_lists = ReadingList()
    for shelf in shelves_to_pull:
        book_list = [book for book in gr_client.get_books_for_shelf(resume_mapping[shelf])]
        setattr(reading_lists, resume_mapping[shelf], book_list)

    resume.reading_list = reading_lists
    resume.save()







