FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py collectstatic \

EXPOSE 8000

CMD ["gunicorn", "web_backend.wsgi:application", "-w", "2", "-b", ":8000","--reload"]
