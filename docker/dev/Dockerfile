FROM python:3.11

RUN mkdir /code

WORKDIR /code

COPY . /code/

RUN apt-get update 
ADD requirements.txt /code/
RUN pip install -r requirements.txt

CMD ["sh", "/code/docker/dev/start-container.sh"]

