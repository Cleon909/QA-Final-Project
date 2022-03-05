FROM mysql
ENV MYSQL_ROOT_PASSWORD=$SQLPWD
ENV MYSQL_DATABASE=appdb
COPY create_tables.sql /docker-entrypoint-initdb.d/