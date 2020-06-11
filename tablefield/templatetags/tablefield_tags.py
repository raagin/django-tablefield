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
    merge_сells = value.get('mergeCells', [])
    cells_meta = value.get('cellsMeta', [])

    data_objects = []
    
    
    # iterate over all table [['1', None, None], ['1', '2', '3']]
    # and replace values with objects with extra data - mergeCells and cellsMeta.    
    # and drop next cells when colspan or rowspan exists.
    colspan_count = 0
    rowspan_count = 0

    for ridx, row in enumerate(data):
        colspan_count += rowspan_count
        rowspan_count = 0
        for cidx, col in enumerate(row):
            colspan, rowspan = 0, 0

            if cidx == 0:
                data_objects.append([])

            # Drop next cells when colspan or rowspan exists.
            if colspan_count > 0 and not col:
                colspan_count = colspan_count - 1
                continue
            
            # find by cells position (row, col) in merge_cells
            merge_сell = next((x for x in merge_сells if x['row'] == ridx and x['col'] == cidx), None)
            if merge_сell:
                colspan = merge_сell.get('colspan', 0)
                colspan_count += colspan - 1
                rowspan = merge_сell.get('rowspan', 0)
                rowspan_count += rowspan - 1

            # find by cells position (row, col) in cells_meta
            cell_meta = next((x for x in cells_meta if x['row'] == ridx and x['col'] == cidx), None)
            class_name = cell_meta['val'] if cell_meta else None
            
            data_objects[ridx].append({
                'value': col,
                'colspan': colspan,
                'rowspan': rowspan,
                'className': class_name
                })


    table_header = data_objects.pop(0) if first_row_is_table_header else None

    t = template.loader.get_template("tablefield/table.html")
    return mark_safe(t.render(dict(
        data=data_objects,
        table_header=table_header,
        first_col_is_header=value.get('first_col_is_header', False),
        merge_сells=merge_сells,
        cells_meta=cells_meta
        )))