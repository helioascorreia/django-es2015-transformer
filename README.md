# Django ES2015 Transformer

Do you want to use the latest JavaScript generation on your django project without any pain of setup? This package is for you.

## Setup

### Install package with pip
```bash
pip install django-es2015-transformer
```

### Active the package in django

```python
# settings.py
INSTALLED_APPS = [
    ...
    'es2015_transformer',
]
```

### Edit STATICFILES_STORAGE
```python
# settings.py
STATICFILES_STORAGE = 'es2015_transformer.storage.BabelStaticFileStorage'
```

## Result

In your deploy server when you run the collectstatic command, your js files will be transformed in a ECMAScript5 code.
