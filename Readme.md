Activate
    python manage.py runserver
    celery -A maidokun beat -l info
    celery -A maidokun.celery worker -l info