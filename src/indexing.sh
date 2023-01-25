#bin/bash
python3 manage.py migrate --noinput hr_department
yes | python3 manage.py search_index --rebuild
gunicorn -w 2 --threads 2 -b 0.0.0.0:8000 config.wsgi:application