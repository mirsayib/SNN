web: gunicorn syblog.wsgi --log-file -
web2: daphne syblog.asgi:application --port $PORT --bind 0.0.0.0
chatworker: python manage.py runworker --settings=syblog.settings -v2