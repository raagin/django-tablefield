import json
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def tablefield_render(value):
    if not value:
        return ""
    value = json.loads(value)
    data = value.get('data', None)
    if not data:
        return ""

    first_row_is_table_header = value.get('first_row_is_table_header', False)
    table_header = data.pop(0) if first_row_is_table_header else None

    t = template.loader.get_template("tablefield/table.html")
    return mark_safe(t.render(dict(
        data=data,
        table_header=table_header,
        first_col_is_header=value.get('first_col_is_header', False)
        )))