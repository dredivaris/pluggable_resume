from config import GOODREADS_DATABASE_NAME
from wsgi.exceptions import NotFoundException
from wsgi.goodreads_api import GoodreadsClient
from wsgi.models import Resume, ReadingList, ResumeSettings

from wsgi import create_app
app = create_app()

shelves_to_pull = {'read-to-share', 'read-to-share-work', 'to-read-work', 'currently-reading-work'}
resume_mapping = {
    'read-to-share': 'finished_reading_general',
    'read-to-share-work': 'finished_reading',
    'to-read-work': 'to_read',
    'currently-reading-work': 'currently_reading'
}

***REMOVED*** goodreads sync.

Handles sync of goodreads book list data from goodreads to a user resume object specified in the
database
***REMOVED***


def sync_bookshelves_from_goodreads(resume):
    service_link = None
    for sl in resume.service_links_list:
        if sl.name == GOODREADS_DATABASE_NAME:
            service_link = sl
            break

    gr_client = GoodreadsClient(service_link.key,
                                service_link.secret,
                                service_link.oauth_key,
                                service_link.oauth_secret,
                                service_link.user_id)

    shelves = set(gr_client.list_shelves_by_name())
    if len(shelves_to_pull) != len(shelves_to_pull & shelves):
        raise NotFoundException('Error: reading list mismatch ', shelves_to_pull & shelves)

    reading_lists = ReadingList()
    for shelf in shelves_to_pull:
        book_list = [book for book in gr_client.get_books_for_shelf(shelf)]
        setattr(reading_lists, resume_mapping[shelf], book_list)

    resume.reading_list = reading_lists
    resume.save()


if __name__ == '__main__':
    try:
        resume_setting = ResumeSettings.objects.all()[0]
    except IndexError:
        raise NotFoundException('Error: no ResumeSettings model object describing goodreads '
                                'to resume linkage exists.')
    sync_bookshelves_from_goodreads(resume_setting.resume_to_sync)
