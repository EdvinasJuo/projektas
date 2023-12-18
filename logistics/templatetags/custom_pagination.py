from django import template

register = template.Library()

@register.inclusion_tag('pagination_template.html')
def show_pagination_links(queryset, parameter_name='page'):
    return {'current_list': queryset, 'parameter_name': parameter_name}