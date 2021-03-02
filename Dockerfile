FROM rg.fr-par.scw.cloud/the-uncle/uwsgi-nginx-flask:python3.8

COPY requirements.txt /

RUN pip install -r /requirements.txt
COPY ./app /app