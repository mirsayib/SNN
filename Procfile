web: gunicorn syblog.wsgi --log-file -
web2: daphne app_xxx.routing:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channel_layer -v2