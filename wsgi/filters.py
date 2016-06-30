from flask import Blueprint

filters = Blueprint('filters', __name__)


def process_newlines(val):
    vals = val.split('\r\n\r\n')
    return ''.join('<p>{}</p>'.format(v) for v in vals)


def process_newlines_short(val):
    vals = val.split('\r\n')
    return ''.join('<p>{}</p>'.format(v) for v in vals)


def level_to_proficiency(val):
    val = int(val) if val is not None else 5
    proficiency_dict = {
        (10, 10): 'Guru',
        (9, 9): 'Expert',
        (8, 8): 'Pro',
        (7, 6): 'Advanced',
        (5, 5): 'Intermediate',
        (4, 3): 'Skilled',
        (2, 2): 'Beginner',
        (1, 0): 'Novice'
    }
    for k, v in proficiency_dict.items():
        high, low = k
        if high >= val >= low:
            return v


def process_urls(url):
    return url.strip('http://').strip('https://')

filters.add_app_template_filter(process_newlines, 'process_newlines')
filters.add_app_template_filter(level_to_proficiency, 'level_to_proficiency')
filters.add_app_template_filter(process_newlines_short, 'process_newlines_short')
filters.add_app_template_filter(process_urls, 'process_urls')

