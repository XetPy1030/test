FROM python:3.10.8-alpine3.16

ENV PYTHONUNBUFFERED=1 \
    mode=production \
    PYTHONDONTWRITEBYTECODE=1 \
    \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN mkdir -p /usr/src/web

COPY . /usr/src/web

WORKDIR /usr/src/web/src

RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev bash && \
    pip install poetry && \
    pip install gunicorn 
RUN pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

RUN apk del .tmp-build-deps

EXPOSE 8000

ENTRYPOINT ["python3", "manage.py", "migrate"]
ENTRYPOINT ["gunicorn", "-w", "2", "--threads", "2", "-b", "0.0.0.0:8000", "config.wsgi:application"]
ENTRYPOINT ["sh", "indexing.sh"]
