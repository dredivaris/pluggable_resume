import pytest
import re
import jsonpickle as jsonpickle

from utils.sync_goodreads_to_resume import sync_bookshelves_from_goodreads
from wsgi.setup import engine_db
from wsgi.models import Resume, ResumeSettings


@pytest.fixture(scope="module")
def resume(request):
    '''
        create test resume setup location
    '''

    settings = ResumeSettings.objects.all()[0]
    resume_to_sync_old = settings.resume_to_sync
    res = Resume(
        title='goodreads testing',
        service_links_list=[sl for sl in resume_to_sync_old.service_links_list])
    print('new test res')
    print(['%s' % i.name for i in res.service_links_list])
    res.save()
    settings.resume_to_sync = res
    settings.save()


    def fin():
        res.delete()
        settings.resume_to_sync = resume_to_sync_old
        settings.save()
    request.addfinalizer(fin)
    return res


def test_verify_settings_are_setup(resume):
    try:
        settings = ResumeSettings.objects.all()[0]
    except IndexError:
        assert False


def test_goodreads_sync(resume):
    # activate sync
    assert resume.service_links_list

    sync_bookshelves_from_goodreads(resume)

    res_to_check = ResumeSettings.objects.all()[0].resume_to_sync

    assert len(res_to_check.reading_list.currently_reading) > 0
    assert len(res_to_check.reading_list.finished_reading) > 0
    assert len(res_to_check.reading_list.finished_reading_general) > 0
    assert len(res_to_check.reading_list.to_read) > 0

