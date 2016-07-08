import pytest

from wsgi.models import Resume, SummaryInfo, Book, ReadingList, ResumeSettings, Skill

"""
    Selenium based system wide tests are included here.  No tests here access the app directly
"""


@pytest.fixture()
def set_window(selenium):
    selenium.set_window_size(1120, 550)

pytestmark = pytest.mark.usefixtures('live_server', 'set_window')


@pytest.fixture(scope='module')
def set_basic_resume(request):
    summary = SummaryInfo(
        summary='test summary')
    book1 = Book(title='testbook1')
    book2 = Book(title='testbook2')
    book3 = Book(title='testbook3')

    reading_list = ReadingList(
        to_read=[book1, book2, book3],
        currently_reading=[book1, book2, book3],
        finished_reading_general=[book1, book2, book3],
        finished_reading=[book1, book2, book3]
    )
    skills = [
        Skill(
            name='django',
            skill_level=5,
            years=1,
            order_by=1,
        ),
        Skill(
            name='python',
            skill_level=9,
            years=8,
            order_by=0,
        ),
        Skill(
            name='javascript',
            skill_level=3,
            years=0,
            order_by=3,
        )
    ]

    resume = Resume(
        title='test resume',
        headline='test headline',
        is_primary=True,
        summary_info=summary,
        reading_list=reading_list,
        skills=skills
    )
    resume_secondary = Resume(
        title='test resume 2',
        headline='test headline2',
        is_primary=False
    )
    resume.save()
    resume_secondary.save()

    rs = ResumeSettings(
        enable_limited_resume=False,
    )
    rs.save()

    def fin():
        resume.delete()
        resume_secondary.delete()

    request.addfinalizer(fin)


def test_live_resume(selenium, live_server, set_basic_resume):
    selenium.get('http://localhost:{}/resume/'.format(live_server.port))
    assert selenium.title == 'test resume'
    assert selenium.\
        find_element_by_class_name('section-inner').\
        find_element_by_class_name('heading').text == 'About Me'


def test_live_admin(selenium, live_server, set_basic_resume):
    selenium.get('http://localhost:{}/admin/'.format(live_server.port))
    assert selenium.find_element_by_id('admin-navbar-collapse').\
        find_element_by_tag_name('li').text == 'Home'


class TestFlaskBasedResumeSection:
    def test_page_loads_properly_named_after_page_title(self, selenium, live_server):
        selenium.get('http://localhost:{}/resume/'.format(live_server.port))
        # TODO

    def test_books_in_a_book_list(self, selenium, live_server):
        selenium.get('http://localhost:{}/resume/'.format(live_server.port))
        book_sections = selenium.find_elements_by_class_name('books')
        assert len(book_sections) > 1
        selenium.implicitly_wait(3)
        first_book_list_items = book_sections[0].find_elements_by_tag_name('li')
        assert first_book_list_items and len(first_book_list_items) > 0

    def test_corrent_number_of_skills_and_in_order(self, selenium, live_server):
        selenium.get('http://localhost:{}/resume/'.format(live_server.port))
        skillset = selenium.find_element_by_class_name('skillset')
        skills = skillset.find_elements_by_tag_name('h3')
        tooltips = skillset.find_elements_by_tag_name('span')
        assert len(skills) == 3
        for skill, expected in zip(skills, ['python', 'django', 'javascript']):
            assert skill.text.split('\n')[0] == expected

        for tip, expected in zip(tooltips, ['8 years ', '1 year ', '< 1 year']):
            text = tip.get_attribute('data-original-title')
            assert expected in text
