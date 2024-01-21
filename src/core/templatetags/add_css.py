from django import template

register = template.Library()


@register.filter
def add_css(field, css):
    return field.as_widget(attrs={'class': css})
