FROM mongo:latest

ENV MONGO_INITDB_ROOT_USERNAME="root"
ENV MONGO_INITDB_ROOT_PASSWORD="example"
ENV MONGO_INITDB_DATABASE="your_db_name"

ENV TZ="Asia/Tokyo"
RUN echo $TZ > /etc/timezone

COPY ./database/init.js /docker-entrypoint-initdb.d/
