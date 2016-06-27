from datetime import datetime, timedelta

from wsgi.models import Resume, is_empty


def combined_resume(hide_work_experience=True):
    resumes = [r for r in Resume.objects.all()]
    resume = None
    for res in resumes:
        if res.is_primary:
            resume = res
            break
    base = resume
    resumes.remove(resume)
    print('starting')
    for resume in resumes:
        for key, value in resume._fields.items():
            print('key currently is ', key)
            if key in ['reading_list', 'service_links_list']:
                continue
            if key in 'work_experiences':
                print('key in work experiences')

                for experience in resume.work_experiences:
                    print('appending', experience.position_title)
                    base.work_experiences.append(experience)
            if is_empty(getattr(base, key, None)) and not is_empty(getattr(resume, key, None)):
                setattr(base, key, getattr(resume, key))

    if hide_work_experience:
        for experience in list(base.work_experiences):
            if experience.sensitive:
                base.work_experiences.remove(experience)
    base.work_experiences = sort_work_experiences(base.work_experiences)
    return base


def sort_work_experiences(work_experiences):
    def key(val):
        val = val.to_date
        if val in 'present' or val in 'current':
            return datetime.now()
        else:
            try:
                return datetime.strptime(val, '%Y')
            except ValueError:
                try:
                    return datetime.strptime(val, '%B %Y')
                except ValueError:
                    return datetime.now() - timedelta(years=50)

    return sorted(work_experiences, key=key, reverse=True)