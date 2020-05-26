# Django Tablefield
It uses Handsontable JS library. It is almost like wagtail's [TableBlock](https://github.com/wagtail/wagtail/tree/master/wagtail/contrib/table_block).\
But for plan Django.

## Installation
```bash
pip install git+https://github.com/raagin/django-tablefield.git
```

## Using
```python
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
