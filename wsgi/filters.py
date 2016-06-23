from flask import Blueprint

filters = Blueprint('filters', __name__)


def process_newlines(val):
    vals = val.split('\r\n\r\n')
    return ''.join('<p>{}</p>'.format(v) for v in vals)


def process_newlines_short(val):
    vals = val.split('\r\n')
    return ''.join('<p>{}</p>'.format(v) for v in vals)


def level_to_proficiency(val):
    val = int(val)
    proficiency_dict = {
        (10,10): 'Expert',
        (9, 8): 'Pro',
        (7, 6): 'Advanced',
        (5, 5): 'Intermediate',
        (4, 4): 'Skilled',
        (3, 2): 'Beginner',
        (1, 0): 'Novice'
***REMOVED***
    for k, v in proficiency_dict.items():
        high, low = k
        if high >= val >= low:
            return v

filters.add_app_template_filter(process_newlines, 'process_newlines')
filters.add_app_template_filter(level_to_proficiency, 'level_to_proficiency')
filters.add_app_template_filter(process_newlines_short, 'process_newlines_short')

