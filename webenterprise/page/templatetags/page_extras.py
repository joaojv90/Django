from ..models import Page
from django import template

# registar template
register = template.Library()

# decortador
@register.simple_tag

# consultar las paáginas secundarias
def get_pages_lis():
    pages = Page.objects.all()
    return pages