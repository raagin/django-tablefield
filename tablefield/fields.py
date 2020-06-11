import json
from django.db.models import TextField
from django.forms.widgets import Widget
from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS

DEFAULT_TABLE_OPTIONS = {
    'minSpareRows': 0,
    'startRows': 3,
    'startCols': 3,
    'colHeaders': False,
    'rowHeaders': False,
    'mergeCells': True,
    'contextMenu': [
        'row_above',
        'row_below',
        '---------',
        'col_left',
        'col_right',
        '---------',
        'remove_row',
        'remove_col',
        '---------',
        'mergeCells',
        '---------',
        'alignment',
        '---------',
        'undo',
        'redo'
    ],
    'editor': 'text',
    'stretchH': 'all',
    'height': 200,
    'renderer': 'html',
    'autoColumnSize': False,
}


class TableField(TextField):
    def __init__(self, *args, **kwargs):
        kwargs['blank'] = True
        kwargs['default'] = dict
        self.table_options = kwargs.pop('table_options', DEFAULT_TABLE_OPTIONS)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        widget_class = kwargs.get('widget', TableFieldWidget)
        attrs = {}
        attrs["table_options_json"] = json.dumps(self.table_options)
        defaults = {
            'widget': widget_class(attrs=attrs),
        }
        return super().formfield(**defaults)

    def get_prep_value(self, value):
        return str(json.dumps(value))

    def from_db_value(self, value, expression, connection):
        return value

    def to_python(self, value):
        return json.loads(value)


class TableFieldWidget(Widget):
    template_name = 'tablefield/table_field.html'
    
    class Media:
        js = (
            '/static/tablefield/handsontable/handsontable.min.js',
            '/static/tablefield/table.js',
        )
        css = {
            'all': ('/static/tablefield/handsontable/handsontable.min.css',)
            }

FORMFIELD_FOR_DBFIELD_DEFAULTS[TableField] = {
        'widget': TableFieldWidget
    }