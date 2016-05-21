from mongoengine import *


# Resume models follow:
class BasicInfo(EmbeddedDocument):
    location = StringField()
    email = EmailField()
    website = URLField()
    industry = StringField()


class Skill(EmbeddedDocument):
    name = StringField()
    url = URLField()


class Language(EmbeddedDocument):
    name = StringField()
    proficiency_level = StringField()


class Experience(EmbeddedDocument):
    company_title = StringField(required=True)
    position_location = StringField()
    company_url = URLField()
    time_at_position = StringField(required=True)
    position_title_url = URLField()
    position_title = StringField(required=True)
    company_image_url = URLField()
    from_date = StringField()
    to_date = StringField()
    description = StringField()


class Certification(EmbeddedDocument):
    title = StringField(required=True)
    license = StringField()
    issuer_url_or_certificate_url = URLField()
    issuer_url = URLField()
    date = StringField()
    issuer_image_url = StringField()
    cert_url = URLField()
    institution = StringField(required=True)


class SummaryInfo(EmbeddedDocument):
    current_position = StringField()
    previous_positions = ListField(StringField())
    previous_position = ListField(StringField())
    summary = StringField()


class School(EmbeddedDocument):
    name = StringField(required=True)
    image = URLField()
    to_date = StringField()
    from_date = StringField()
    degree = StringField(required=True)
    url = URLField()


class Other(EmbeddedDocument):
    opportunities = ListField(StringField())
    organizations = ListField(StringField())
    causes = ListField(StringField())


class Book(EmbeddedDocument):
    goodreads_id = IntField()
    isbn = StringField()
    isbn13 = StringField()
    title = StringField()
    image_url = URLField()
    small_image_url = URLField()
    link = URLField()
    num_pages = IntField()
    publisher = StringField()
    average_rating = StringField()
    description = StringField()
    authors = ListField(StringField())
    rating = StringField()
    started_at = DateTimeField()
    read_at = DateTimeField()
    date_added = DateTimeField()
    date_updated = DateTimeField()
    review_body = StringField()


class ReadingList(EmbeddedDocument):
    to_read = ListField(EmbeddedDocumentField(Book))
    currently_reading = ListField(EmbeddedDocumentField(Book))
    finished_reading_general = ListField(EmbeddedDocumentField(Book))
    finished_reading = ListField(EmbeddedDocumentField(Book))


# link to code eval github etc
class ServiceLink(EmbeddedDocument):
    name = StringField()
    user_id = StringField()
    key = StringField()
    secret = StringField()
    oauth_key = StringField()
    oauth_secret = StringField()


class Resume(Document):
    '''
    About me +
    Basic Info +
    Skills
    Testimonials
    Education
    Courses
    Languages -
    Latest Blog Posts -
    Latest Projects -
    Other Projects -
    Work Experience
    My Github
    CodeEval (maybe) -
    Favorite Coding Music -
    Conferences -
    Credits (look into requirements)
    -------
    certifications
    summary_info
    top_skills
    other_skills
    organizations
    locality?
    name
    industry
    connections
    experiences
    headline
    school
    causes
    '''

    is_primary = BooleanField(default=True)

    title = StringField()
    headline = StringField()
    name = StringField()
    industry = StringField()
    connections = StringField()
    basic_info = EmbeddedDocumentField(BasicInfo)
    summary_info = EmbeddedDocumentField(SummaryInfo)
    top_skills = ListField(EmbeddedDocumentField(Skill))
    other_skills = ListField(EmbeddedDocumentField(Skill))
    work_experiences = ListField(EmbeddedDocumentField(Experience))
    certifications = ListField(EmbeddedDocumentField(Certification))
    schools = ListField(EmbeddedDocumentField(School))
    other = EmbeddedDocumentField(Other)
    languages = ListField(EmbeddedDocumentField(Language))
    reading_list = EmbeddedDocumentField(ReadingList)
    service_links_list = ListField(EmbeddedDocumentField(ServiceLink))


class ResumeSettings(Document):
    enable_limited_resume = BooleanField(default=False)
    limited_resume_url_specifier = StringField()
    hidden_experiences = ListField(StringField())