FROM python:3.9

# set work directory
WORKDIR /usr/src/API_CRUD

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/API_CRUD
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/API_CRUD

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]