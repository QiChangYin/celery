开始编程
1、安装django-celery：  
pip install django-celery
python manage.py makemigrations test_celery
python manage.py migrate
celery worker -A test_celery -l info
python manage.py runserver