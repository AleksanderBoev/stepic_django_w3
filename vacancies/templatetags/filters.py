from django import template

register = template.Library()


@register.filter(name='null_to_no')
def null_to_no(value):#отслеживание и замена нулей на "нет"
    if str(value) == '0':
        return 'нет'
    return value

@register.filter(name='rus_plural_endings')
def rus_plural_endings_1(value, arg):
    if 5 <= abs(value) % 100 <= 20 or value == 0:
        return arg + 'ий'
    if abs(value) % 10 == 1:
        return arg+'ия'
    if 2 <= abs(value) % 10 <= 4:
        return arg + 'ии'

@register.filter(name='rus_plural_endings_2')
def rus_plural_endings_2(value, arg):
    if 5 <= abs(value) % 100 <= 20 or value == 0:
        return arg + 'ов'
    if abs(value) % 10 == 1:
        return arg+''
    if 2 <= abs(value) % 10 <= 4:
        return arg + 'а'