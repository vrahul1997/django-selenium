superuser:
	python manage.py createsuperuser

migration: 
	python manage.py makemigrations

migrate: 
	python manage.py migrate

server:
	python manage.py runserver

req_file:
	pip freeze > requirements.txt

worker:
	celery -A mr_vod worker -l info

beat:
	celery -A mr_vod beat -l info

beatDB:
	celery -A mr_vod beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

.PHONY: migration migrate worker_celery req_file