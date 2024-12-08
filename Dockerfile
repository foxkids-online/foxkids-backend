FROM python:3.12.0b1-slim-buster

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
RUN apt-get -y install curl

COPY requirements.txt ./
COPY constraints.txt ./

RUN python -m pip install -c constraints.txt -r requirements.txt

COPY ./src/ /src
COPY ./series_settings /series_settings/
WORKDIR /src
CMD python -m foxkids