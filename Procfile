release:python manage.py makemigrations stories_api
release:python manage.py migrate --no-input

web: gunicorn stories_project.wsgi --log-file -
