# Django Tablefield
It uses Handsontable JS library (0.38.1 version. MIT Lisence). It is almost like wagtail's [TableBlock](https://github.com/wagtail/wagtail/tree/master/wagtail/contrib/table_block).\
But for plain Django and **added functional of merge cells and alignment**.

## Installation
```bash
pip install django-tablefield
# or latest version
pip install git+https://github.com/raagin/django-tablefield.git
```

## Using
```python
# settings.py
INSTALLED_APPS = [
    ...
    'tablefield',
    ...
]

# models.py
from tablefield.fields import TableField

class MyModel(models.Model):
    table = TableField(verbose_name='Table')

```
### In templates
```html
{% load tablefield_tags %}
{% tablefield_render mymodel.table %}
```

### Options
Default options is:
```python
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
```
As you see, default renderer is `html`.\
You read about it: https://handsontable.com/docs/1.18.1/Options.html#renderer

You may set your options:
```python
class MyModel(models.Model):
    table = TableField(
        table_options = {
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
        },
        verbose_name='Table'
        )
```
