python manage.py makemigrations && \
python manage.py migrate --noinput  && \
python manage.py collectstatic --noinput  && \
uwsgi --ini /code/docker/dev/uwsgi.ini --enable-threads