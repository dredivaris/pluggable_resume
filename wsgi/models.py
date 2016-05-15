from mongoengine import *
from wsgi.views import engine_db as db


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

    title = StringField(required=True)
    headline = StringField(required=True)
    name = StringField(required=True)
    industry = StringField(required=True)
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


class BasicInfo(EmbeddedDocument):
    location = StringField()
    email = EmailField(required=True)
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
    current_position = StringField(required=True)
    previous_position = ListField(StringField)
    summary = StringField(required=True)


class School(EmbeddedDocument):
    name = StringField(required=True)
    image = URLField()
    to_date = StringField()
    from_date = StringField()
    degree = StringField(required=True)
    url = URLField()


class Other(EmbeddedDocument):
    opportunities = ListField(StringField)
    organizations = ListField(StringField)
    causes = ListField(StringField)


class ReadingList(EmbeddedDocument):
    to_read = ListField(DynamicField)
    currently_reading = ListField(DynamicField)
    finished_reading = ListField(DynamicField)


# link to code eval github etc
class OuterServiceLink:
    pass

