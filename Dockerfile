FROM python:3.8
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src
COPY . /opt/services/djangoapp/src
RUN pip3 install -r requirements.txt gunicorn
EXPOSE 8000
CMD ["gunicorn", "--chdir", "zbyt", "--bind", ":8000", "zbyt.wsgi:application"]
