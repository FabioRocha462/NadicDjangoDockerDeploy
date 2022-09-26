FROM python

COPY Api/ /app/
COPY requeriments.txt /app/ 

RUN (cd /app/ && pip install -r requeriments.txt)
RUN (cd /app/ && pip install requests)

ENV PYTHONUMBUFFERED = 1


CMD python /app/manage.py runserver 0.0.0.0:8000
