FROM python:3.8
LABEL maintainer="SANIC_VIDEO_BALANSER"
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install --upgrade pip -r requirements.txt
COPY . /app
EXPOSE 8000