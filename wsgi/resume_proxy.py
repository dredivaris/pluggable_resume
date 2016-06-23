from wsgi.models import Resume, is_empty


def combined_resume(hide_work_experience=False):
    resumes = [r for r in Resume.objects.all()]
    for resume in resumes:
        if resume.is_primary:
            break
    base = resume
    resumes.remove(resume)

    for resume in resumes:
        for key, value in resume._fields.items():
            if key in ['reading_list', 'service_links_list']:
                continue
            if key in 'work_experience':
                for experience in resume.work_experiences:
                    base.work_experiences.append(experience)
            if is_empty(getattr(base, key, None)) and not is_empty(getattr(resume, key, None)):
                print('setting: ', key)
                setattr(base, key, getattr(resume, key))

    if hide_work_experience:
        for experience in base.work_experiences:
            if experience.sensitive:
                base.work_experiences.remove(experience)
    return base
