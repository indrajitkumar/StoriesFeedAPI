release:python manage.py makemigrations stories_api
release:python manage.py migrate

web: gunicorn stories_project.wsgi --log-file -
