FROM mysql
COPY . .
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=appdb
COPY create_tables.sql /docker-entrypoint-initdb.d/