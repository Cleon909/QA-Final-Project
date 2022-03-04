FROM mysql
COPY . .
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=appdb
COPY create_table.sql /docker-entrypoint-initdb.d/

