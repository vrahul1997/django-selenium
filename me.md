==>

## pipenv lock -r requirement.txt

**_ to create trq.text from pipFile _**

==>

## pip freeze > requirements.txt

**_ for creating req.text from pip freeze _**

==>
broker for celery must be up and running, else it will show error like ampq: connection refused

## celery -A dj_selenium worker -l info

**_ running celery for the project _**

==>
For initiating the the celery job stored in the DB

## celery -A dj_selenium beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

**_ running celery beat job stored in the DB _**
