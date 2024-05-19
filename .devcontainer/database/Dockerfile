FROM mongo:latest

ENV TZ="Asia/Tokyo"
RUN echo $TZ > /etc/timezone

COPY ./database/init.js /docker-entrypoint-initdb.d/
