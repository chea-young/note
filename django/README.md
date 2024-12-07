## Django

### Setting

```
python -m venv {venv-name}
source {venv-name}/Scripts/activate

pip install django
django-admin startproject {project-name}
python manage.py startapp {app-name}

python manage.py migrate

python manage.py runserver # start

# setting.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]
```