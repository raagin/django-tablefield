# Django Tablefield
It uses Handsontable JS library (0.38.1 version. MIT Lisence). It is almost like wagtail's [TableBlock](https://github.com/wagtail/wagtail/tree/master/wagtail/contrib/table_block).\
But for plain Django.

## Installation
```bash
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
