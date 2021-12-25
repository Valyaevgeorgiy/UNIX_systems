FROM python:3.9
WORKDIR /code
COPY . /code
RUN pip3 install -r requirements.txt
CMD gunicorn MicroService.wsgi:application --bind 0.0.0.0:8000