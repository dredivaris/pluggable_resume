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
    if resume is not None:
        resumes.remove(resume)
    else:
        return None
    for resume in resumes:
        for key, value in resume._fields.items():
            if key in ['reading_list', 'service_links_list']:
                continue
            if key in 'work_experiences':
                for experience in resume.work_experiences:
                    base.work_experiences.append(experience)
            if is_empty(getattr(base, key, None)) and not is_empty(getattr(resume, key, None)):
                setattr(base, key, getattr(resume, key))
            elif not is_empty(getattr(base, key, None)) and \
                    not is_empty(getattr(resume, key, None)) and \
                    hasattr(getattr(base, key), '_fields'):
                current, other = getattr(base, key), getattr(resume, key)
                for field in getattr(base, key)._fields:
                    if is_empty(getattr(current, field, None)) and not \
                            is_empty(getattr(other, field, None)):
                        setattr(current, field, getattr(other, field))

    if base.skills:
        try:
            base.skills = sorted(base.skills, key=lambda skill: skill.order_by)
        except TypeError:
            # if order_by hasn't been filled in; just don't do the sort
            pass

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