FROM python:3.7
ARG ENV
ENV ENVIRONMENT ${ENV}
ENV PYTHONUNBUFFERED 1

ENV APP_HOME /usr/src/app
WORKDIR /$APP_HOME
COPY . $APP_HOME/

RUN pip3 install -r requirements.txt

EXPOSE 4000
CMD ["python3", "HoeWarmIsHetInDelft.py"]
