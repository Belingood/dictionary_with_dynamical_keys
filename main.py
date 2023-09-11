def elements_classification_by_ifs(element):
    """The solution with a cascade of ifs"""

    if 0 <= element <= 300:
        return f'{element} is small'

    if 301 <= element <= 600:
        return f'{element} is medium'

    if 601 <= element <= 1000:
        return f'{element} is big'

    return f'{element} is outside the parameters'


def elements_classification_by_dict(element):
    """The solution with a dictionary with dynamical keys"""

    return {
        0 <= element <= 300: f'{element} is small',
        301 <= element <= 600: f'{element} is medium',
        601 <= element <= 1000: f'{element} is big',
        element < 0 or element > 1000: f'{element} is outside the parameters'
    }[True]


array = [-100, 0, 100, 500, 999, 1050, 5000]
funcs = ['elements_classification_by_ifs', 'elements_classification_by_dict']

for el in array:
    for func in funcs:
        print(f'{func.ljust(32)}: {globals()[func](el)}')
    print()
