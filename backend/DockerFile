FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app
# dependancies of projects
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/

# running the project
CMD python manage.py runserver 0.0.0.0:8000