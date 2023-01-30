#bin/bash
python3 manage.py migrate --noinput hr_department
python3 manage.py search_index --rebuild -f
gunicorn -w 2 --threads 2 -b 0.0.0.0:8000 config.wsgi:application